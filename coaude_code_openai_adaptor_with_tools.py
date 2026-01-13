#!/usr/bin/env python3
"""
Claude Code OpenAI-Compatible Adapter Server WITH DYNAMIC TOOL LOADING

Enhanced version that supports dynamically loading custom tools via API.

Usage:
    # Start server
    python3 claude_code_openai_adapter_with_tools.py

    # Register a tool
    curl -X POST http://localhost:8889/v1/tools \
      -H "Content-Type: application/json" \
      -d '{
        "name": "get_weather",
        "description": "Get weather for a city",
        "input_schema": {"city": "str"},
        "code": "async def get_weather(args):\\n    return {\\"content\\": [{\\"type\\": \\"text\\", \\"text\\": f\\"Weather in {args[\\"city\\"]}: Sunny\\"}]}"
      }'

    # Use tools in chat completion
    POST /v1/chat/completions with tools parameter
"""

import asyncio
import time
import uuid
import sys
from typing import Optional, List, Dict, Any, Callable
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
import uvicorn
import json

try:
    from claude_agent_sdk import (
        ClaudeSDKClient,
        ClaudeAgentOptions,
        AssistantMessage,
        ResultMessage,
        TextBlock,
        ToolUseBlock,
        tool,
        create_sdk_mcp_server
    )
    CLAUDE_SDK_AVAILABLE = True
except ImportError:
    CLAUDE_SDK_AVAILABLE = False


# ============================================================================
# Request/Response Models
# ============================================================================

class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 4096
    stream: Optional[bool] = False
    tools: Optional[List[str]] = None  # Tool names to use


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: str


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[Choice]
    usage: Usage


class StreamChoice(BaseModel):
    index: int
    delta: Dict[str, Any]
    finish_reason: Optional[str] = None


class ChatCompletionChunk(BaseModel):
    id: str
    object: str = "chat.completion.chunk"
    created: int
    model: str
    choices: List[StreamChoice]


# ============================================================================
# Tool Management Models
# ============================================================================

class ToolDefinition(BaseModel):
    name: str
    description: str
    input_schema: Dict[str, Any]
    code: str  # Python code for the tool function


class ToolInfo(BaseModel):
    name: str
    description: str
    input_schema: Dict[str, Any]
    registered_at: float


# ============================================================================
# Global Tool Registry
# ============================================================================

class ToolRegistry:
    """Manages dynamically loaded tools."""

    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        self.tool_info: Dict[str, ToolInfo] = {}
        self.mcp_server = None
        self._lock = asyncio.Lock()

    async def register_tool(self, definition: ToolDefinition) -> dict:
        """Register a new tool from code."""
        async with self._lock:
            # Validate tool name
            if definition.name in self.tools:
                raise ValueError(f"Tool '{definition.name}' already exists")

            # Create namespace for tool execution
            namespace = {
                'tool': tool,
                '__builtins__': __builtins__,
            }

            try:
                # Execute the tool code
                exec(definition.code, namespace)

                # Find the tool function (should be the last defined function)
                tool_func = None
                for name, obj in namespace.items():
                    if callable(obj) and not name.startswith('_') and name != 'tool':
                        tool_func = obj
                        break

                if tool_func is None:
                    raise ValueError("No callable function found in tool code")

                # Wrap with @tool decorator
                decorated_func = tool(
                    name=definition.name,
                    description=definition.description,
                    input_schema=definition.input_schema
                )(tool_func)

                # Store the tool
                self.tools[definition.name] = decorated_func
                self.tool_info[definition.name] = ToolInfo(
                    name=definition.name,
                    description=definition.description,
                    input_schema=definition.input_schema,
                    registered_at=time.time()
                )

                # Recreate MCP server with all tools
                await self._rebuild_mcp_server()

                return {
                    "status": "success",
                    "message": f"Tool '{definition.name}' registered successfully",
                    "tool": self.tool_info[definition.name].model_dump()
                }

            except Exception as e:
                raise ValueError(f"Failed to register tool: {str(e)}")

    async def unregister_tool(self, tool_name: str) -> dict:
        """Remove a registered tool."""
        async with self._lock:
            if tool_name not in self.tools:
                raise ValueError(f"Tool '{tool_name}' not found")

            del self.tools[tool_name]
            del self.tool_info[tool_name]

            # Recreate MCP server
            await self._rebuild_mcp_server()

            return {
                "status": "success",
                "message": f"Tool '{tool_name}' removed"
            }

    async def _rebuild_mcp_server(self):
        """Rebuild the MCP server with current tools."""
        if self.tools:
            self.mcp_server = create_sdk_mcp_server(
                name="dynamic_tools",
                version="1.0.0",
                tools=list(self.tools.values())
            )
        else:
            self.mcp_server = None

    def get_tool_names(self) -> List[str]:
        """Get list of all tool names for ClaudeAgentOptions."""
        return [f"mcp__dynamic_tools__{name}" for name in self.tools.keys()]

    def list_tools(self) -> List[ToolInfo]:
        """List all registered tools."""
        return list(self.tool_info.values())


# ============================================================================
# Claude Agent SDK Adapter
# ============================================================================

class ClaudeCodeAdapter:
    """Adapter with dynamic tool support."""

    MODEL_MAP = {
        "claude-sonnet-4.5": "claude-sonnet-4-5",
        "claude-haiku-4.5": "claude-haiku-4-5",
        "claude-3-5-sonnet-20241022": "claude-sonnet-4-5",
        "claude-3-haiku-20240307": "claude-haiku-4-5",
        "gpt-4o": "claude-sonnet-4-5",
        "gpt-4": "claude-sonnet-4-5",
        "gpt-4o-mini": "claude-haiku-4-5",
    }

    def __init__(self, tool_registry: ToolRegistry):
        if not CLAUDE_SDK_AVAILABLE:
            raise RuntimeError("Claude Agent SDK not installed")
        self.tool_registry = tool_registry

    def _map_model(self, model: str) -> str:
        return self.MODEL_MAP.get(model, "claude-haiku-4-5")

    def _format_messages(self, messages: List[Message]) -> str:
        prompt_parts = []
        for msg in messages:
            if msg.role == "system":
                prompt_parts.append(f"System: {msg.content}")
            elif msg.role == "user":
                prompt_parts.append(f"User: {msg.content}")
            elif msg.role == "assistant":
                prompt_parts.append(f"Assistant: {msg.content}")
        return "\n\n".join(prompt_parts)

    async def create_completion(
        self,
        request: ChatCompletionRequest
    ) -> ChatCompletionResponse:
        """Create chat completion with optional tools."""
        claude_model = self._map_model(request.model)
        prompt = self._format_messages(request.messages)

        # Build options
        options_kwargs = {
            "model": claude_model,
            "max_turns": 10  # Allow multiple turns for tool use
        }

        # Add tools if requested
        if request.tools:
            # Filter requested tools
            available_tools = self.tool_registry.get_tool_names()
            requested_tools = [
                f"mcp__dynamic_tools__{t}" for t in request.tools
            ]
            tools_to_use = [t for t in requested_tools if t in available_tools]

            if tools_to_use and self.tool_registry.mcp_server:
                options_kwargs["mcp_servers"] = {
                    "dynamic_tools": self.tool_registry.mcp_server
                }
                options_kwargs["allowed_tools"] = tools_to_use
        else:
            options_kwargs["allowed_tools"] = []

        options = ClaudeAgentOptions(**options_kwargs)

        # Call Claude
        response_text = ""
        prompt_tokens = 0
        completion_tokens = 0

        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)

            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            response_text += block.text
                        elif isinstance(block, ToolUseBlock):
                            # Include tool use info in response
                            response_text += f"\n[Tool used: {block.name}]"

                elif isinstance(message, ResultMessage):
                    prompt_tokens = len(prompt) // 4
                    completion_tokens = len(response_text) // 4

        return ChatCompletionResponse(
            id=f"chatcmpl-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=claude_model,
            choices=[
                Choice(
                    index=0,
                    message=Message(role="assistant", content=response_text),
                    finish_reason="stop"
                )
            ],
            usage=Usage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens
            )
        )

    async def create_completion_stream(
        self,
        request: ChatCompletionRequest
    ):
        """Create streaming completion with optional tools."""
        claude_model = self._map_model(request.model)
        prompt = self._format_messages(request.messages)

        # Build options (same as non-streaming)
        options_kwargs = {
            "model": claude_model,
            "max_turns": 10
        }

        if request.tools:
            available_tools = self.tool_registry.get_tool_names()
            requested_tools = [f"mcp__dynamic_tools__{t}" for t in request.tools]
            tools_to_use = [t for t in requested_tools if t in available_tools]

            if tools_to_use and self.tool_registry.mcp_server:
                options_kwargs["mcp_servers"] = {
                    "dynamic_tools": self.tool_registry.mcp_server
                }
                options_kwargs["allowed_tools"] = tools_to_use
        else:
            options_kwargs["allowed_tools"] = []

        options = ClaudeAgentOptions(**options_kwargs)

        completion_id = f"chatcmpl-{uuid.uuid4().hex[:8]}"
        created = int(time.time())

        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)

            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            chunk = ChatCompletionChunk(
                                id=completion_id,
                                created=created,
                                model=claude_model,
                                choices=[
                                    StreamChoice(
                                        index=0,
                                        delta={"content": block.text}
                                    )
                                ]
                            )
                            yield f"data: {chunk.model_dump_json()}\n\n"

        # Final chunk
        final_chunk = ChatCompletionChunk(
            id=completion_id,
            created=created,
            model=claude_model,
            choices=[
                StreamChoice(
                    index=0,
                    delta={},
                    finish_reason="stop"
                )
            ]
        )
        yield f"data: {final_chunk.model_dump_json()}\n\n"
        yield "data: [DONE]\n\n"


# ============================================================================
# FastAPI Server
# ============================================================================

app = FastAPI(
    title="Claude Code Adapter with Dynamic Tools",
    description="OpenAI-compatible API with dynamic tool loading",
    version="2.0.0"
)

tool_registry = ToolRegistry()
adapter = None


@app.on_event("startup")
async def startup():
    global adapter
    if not CLAUDE_SDK_AVAILABLE:
        raise RuntimeError("Claude Agent SDK required")

    adapter = ClaudeCodeAdapter(tool_registry)
    print("✅ Claude Code Adapter with Dynamic Tools ready")


@app.get("/")
async def root():
    return {
        "message": "Claude Code Adapter with Dynamic Tools",
        "endpoints": {
            "chat_completions": "/v1/chat/completions",
            "models": "/v1/models",
            "tools_list": "/v1/tools",
            "tools_register": "POST /v1/tools",
            "tools_delete": "DELETE /v1/tools/{tool_name}"
        }
    }


@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "claude-sonnet-4.5",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "claude-code"
            },
            {
                "id": "claude-haiku-4.5",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "claude-code"
            }
        ]
    }


@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest):
    """OpenAI-compatible chat completions with optional tools."""
    if not adapter:
        raise HTTPException(status_code=500, detail="Adapter not initialized")

    try:
        if request.stream:
            return StreamingResponse(
                adapter.create_completion_stream(request),
                media_type="text/event-stream"
            )
        else:
            response = await adapter.create_completion(request)
            return response.model_dump()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Tool Management Endpoints
# ============================================================================

@app.get("/v1/tools")
async def list_tools():
    """List all registered tools."""
    tools = tool_registry.list_tools()
    return {
        "object": "list",
        "data": [t.model_dump() for t in tools]
    }


@app.post("/v1/tools")
async def register_tool(definition: ToolDefinition):
    """Register a new tool."""
    try:
        result = await tool_registry.register_tool(definition)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/v1/tools/{tool_name}")
async def delete_tool(tool_name: str):
    """Remove a registered tool."""
    try:
        result = await tool_registry.unregister_tool(tool_name)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import os

    port = int(os.getenv("CLAUDE_ADAPTER_PORT", "8889"))

    print("=" * 70)
    print("CLAUDE CODE ADAPTER WITH DYNAMIC TOOLS")
    print("=" * 70)
    print(f"\n🚀 Starting server on http://localhost:{port}")
    print("\n📝 Features:")
    print("  • OpenAI-compatible chat completions")
    print("  • Dynamic tool loading via API")
    print("  • Tool registration: POST /v1/tools")
    print("  • Tool listing: GET /v1/tools")
    print("  • Tool deletion: DELETE /v1/tools/{name}")
    print("\n💡 Register tools at runtime - no restart needed!")
    print("=" * 70)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )

