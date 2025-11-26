# Clarification for the doubts:

## Reuquirements:
### Orchestrator Responsibilities
1. Read project directory using Tree MCP server
2. Generate Tree structure of the project using MCP Tree MCP Server
    - Write the tree structure to a centralized location from where Projects filename and path would be
    read by other MCP Servers in next-steps.
    - Create progress tracking file with all processing steps
4. Run Metadata generation MCP Servers (SuperBol, GnuCobol) 
    - Plan invoking MCP Tools on different source files( Depending on `Batch` or `all`, and `batch number` if `batch` strategy define referring to filepath and filename in Tree MCP output)
    - Finally run pre-defined MCP Tools that should run on project level to generate inter-file and
    intra-file relationships
    - Save the metadata in a centralized location that all agents can fetch and use for doc gen.
    Call that directory `./metadata`

## Orchestrator requirements
5. Spawn N agents in parallel (where N = number of files to document)
    4.a Coordinate batch execution based on configuration `batch` OR `all`
    4.b Handle resource allocation to agents using Ray
6. Assign unique agent IDs and map to file IDs
7. Monitor agent progress and update tracking file
    6.b Handle agent failures and retries
8. Coordinate batch execution based on configuration
9. Ensure all agents complete successfully
### Agent Enhancement Requirements
- Remove existing MCP step from the currect Agent flow ( It's would be a one time operation befoire
   Agents start working)
- Each agent remains identical to current single-file documentation agent (Except MCP step)
- Add capability to document inter-file relationships from project-level metadata
- Add new "Inter-File Relationships" section to output document
- Maintain all existing functionality (three-pass generation, chunking, tracing, etc.)
- Create a `reports` dir where all the logs, metrics, tracing of all agents progress should be written.
Manage the project level progress-tracker in the same directory.
### Configuration Requirements
- New orchestrator configuration section or file
- Specify batch mode (batch vs all-at-once)
- Specify batch size (10/20/30/custom)
- Specify parallel execution framework (Ray)
- Maintain backward compatibility with existing single-file mode

---
## Clarifications:

## Metadata generator MCP Workflow
- As now we will be dealing with a project (multiple files in sub-dirs). We should run these MCP
Tools iteratively on each file. and once all the files are completed, we need to run some Tools that
work on project level once on the entire project to generate project level metadata for
relationships.
- Tools that need to run on project level:
**CTags** NONE
**SuperBol** `cobol_generate_cfg_project`
**GnuCobol**: `extract_relationship`, and `extract_cross_references_tool`

All the above tools also need to run on per-file basis as well.

- What is the **exact tool name/method** exposed by your Tree MCP server?

The source code for Tree MCP Server is available at `~/mcp-servers/tree-mcp-server/src`

It has multiple tools. We can choose based on the workflow requirements:
    - `tree_basic` - Display basic directory tree structure
    Args:
        `path`: Directory to display (default: current directory)
        `output_file`: Optional file to save output
    - `tree_json_output` - Output in JSON format
    Args:
       `path`: Directory path
       `p`max_depth`: Maximum depth
       `p`output_file`: Optional output file

    - `tree_xml_output` - Output in XML/HTML format
    Args:
        `path`: Directory path
        `max_depth`: Maximum depth
        `output_file`: Optional output file

- Should we **filter by file extensions**?
    The filtering should be based on file extensions

- Does the Tree MCP server run in **Docker** like the other MCP servers?

    Yes

---
- - What **additional tools/methods** are available for project-level analysis?

Additional Tools in SuperBol MCP Server:
    name= `cobol_generate_cfg_project`,
    description="Generate Control-Flow Graphs (CFG) for all COBOL files in the project"

Additional Tools for GnuCobol:
-   name: `extract_relationship`
    **Advanced relationship extraction tool** that provides comprehensive inter-file and intra-file analysis for COBOL 74/85 source code. This tool goes beyond basic analysis to extract detailed program structure, control flow, data dependencies, and cross-program relationships. **This Tool Need to run on Individual File and finallyon Whole project level as well**

    **What it extracts:**
    - **Program Identifiers** (PROGRAM-ID)
    - **External Program Calls** (CALL statements with library information)
    - **Copybook Dependencies** (COPY statements from code and comments)
    - **Internal Control Flow** (PERFORM statements, paragraph calls)
    - **File Dependencies** (SELECT and FD statements)
    - **Data Structures** (01 level data items)

    **Modes:**
    - **Single File Mode**: Detailed relationship extraction for one COBOL file
    - **Directory Mode**: Cross-file relationship analysis across entire project with call graphs and copybook usage maps

    **Arguments:**
    - `file_path` (string, optional): Path to single COBOL source file (mutually exclusive with `directory`)
    - `directory` (string, optional): Directory path to scan for COBOL files (mutually exclusive with `file_path`)
    - `recursive` (boolean, optional): Search subdirectories when using `directory` mode (default: true)
    - `copybook_paths` (array, optional): List of directories to search for COPY files
    - `max_files` (integer, optional): Maximum files to analyze in directory mode (default: 100)

-   name: `extract_cross_references_tool`
    **What it extracts:**
    - **Data Items**: Where each variable is defined and all line numbers where it's referenced
    - **Paragraphs**: Where each paragraph is defined and all line numbers where it's performed or called
    - **Reference Counts**: How many times each item is used

    **Arguments:**
    - `file_path` (string, required): Path to COBOL source file
    - `copybook_paths` (array, optional): List of directories to search for COPY files
    - `options` (array, optional): Additional compiler options
    - `skip_compiler` (boolean, optional): If `true`, skip GnuCOBOL compiler and use regex-only extraction. **Recommended for Unisys, IBM, Micro Focus dialects** for much faster processing.

---

- Progress tracker file:
    - The project tracker should be in markdown format
    - The example format is fine.
    - Should track in real-time and update the log file after completion
    - Exact Token usage using `tiktoken`.
    - Yes. It should track batch information as well
---
- Ray Setup:
    - We need to add it in `requirements.txt`
    - Always use latest version for 2025
    - Ray should be always available

- Ray Cluster config:
    - Currently configure for Local single-machine Ray cluster only. But keep options to support
    disyributed structure through user config.

---
- Resource management:

---
- Failure handling:
    - retry the failed agent automatically with a sleep of 3 sec with 3 max retries attemps.

---
- Ray Task structure
    - Follow a basic single machine structure 
    - As most of the Agent instances will read the Metadata, and every instance will update the
    progress tracker. This is one are we need to carefully handle to avoid any race-conditions.
    - Please follow Error handling from `./error-handling-design.md`s "Ray-Specific Error Handling"
      section.

---
- Batching strategy:
    -   orchestrator:
          batch_mode: batch  # Options: 'batch' or 'all'
          batch_size: 10     # Ignored if batch_mode = 'all'
    - Batches should be run sequentially. Batch 1 -> Batch 2


---

- Inter-file Repationships Section:
    - The section should be called `Inter-file relationships`
    - The content should capture Full dependency graph and all inter-file relationships relevant
      for any programming language.
    - The data source for this would be Project wide SuperBol Callflow graph, and `GnuCobol` Project
      level analysis.

---

- Agent Identity and File mapping:
    - Option B with File name based mapping looks appropriate.
    - Yes. The Agent-File mapping should be stored in progress tracking file.
    - Yes. The Agent IDs persist across runs.

---

- Test Coverage:
    - 90% test coverage should be sufficient ( But, Always Aim for 100%)
    - Unit and Integration tests should be fine. End to End tests would be always done by me
    manually and provide you the feedback.

---
- Configuration file structure:
    - Extend the existing config file structure

---

-  Error Handling & Retry Logic
    Retry Automatically with exponential backoff strategy:, with 3 retry attempts. If still fails mark it as failed and continue and generate failure report at the end.

---
- Is Project-level summary document required?
    - Yes. 

- Cost estimation / dry-run mode required?
    - currently not required

- Token budget redundancy - Accept duplicate info across files?
    - This would be happening as in some cases we would be passing same metadata files to all Agent
    instances. Choose and Implement an effiective and efficient strategy for this.

- Retry delay?
    - Implement exponential backoff starting at 3 seconds

- Project-level summary document - Should we generate one?
    Yes. Once all the docs are generated we should generate a Project level document explain the
core components of the project, business logic and the intra-file relationships along with a
summary.

- Output organization - Flat or mirror source directory structure?
    The final markdown output files should be organized aligning with the source directory structure

- Cost estimation / dry-run mode - Should we implement?
    Currently not required

- Retry delay - Fixed 3 seconds OR exponential backoff starting at 3 seconds?
    First retry with a sleep of 3 seconds, the follow exponential backoff strategy 

