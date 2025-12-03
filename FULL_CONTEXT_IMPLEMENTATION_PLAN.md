# Implementation Plan: Full Context Documentation Generation

**Version**: 1.0
**Date**: 2025-12-02
**Approach**: Test-Driven Development (TDD)
**Feature**: One LLM Call Per Section with Full Context (Source + Metadata + Program Map)

---

## Overview

**Goal**: Enhance the COBOL Documentation Agent to generate comprehensive documentation by sending full context (source code + metadata + program map) for each documentation section in separate LLM calls.

**Target Sections**:
- Overview
- Executive Summary
- Key Responsibilities
- Business Logic
- High-Level Data Flow / Full Data Flow

**Development Approach**: Test-Driven Development (TDD)
- Write tests FIRST
- Implement minimum code to pass
- Refactor and clean
- Repeat

---

## Architecture Changes

### Current Architecture
```
Section → Filter Metadata (aggressive) → Generate Program Map (limited top N) → LLM Call → Output
```

### New Architecture
```
Section → Full Context Builder → Full Source + Full Metadata + Enhanced Program Map → LLM Call → Output
           (no filtering)        (complete context package)
```

---

# KANBAN BOARD

## Backlog

### Epic 1: Full Context Builder Module

---

## Epic 1: Full Context Builder Module

### US-1.1: Create Full Context Builder Class

**User Story**: As a documentation generator, I want a module that assembles complete context (source + metadata + program map), so that each LLM call has access to all available information.

**Acceptance Criteria**:
- [ ] `FullContextBuilder` class exists in `full_context_builder.py`
- [ ] Can load complete source code with line numbers
- [ ] Can load all metadata without filtering
- [ ] Can generate enhanced program map with configurable limits
- [ ] Can assemble combined context dictionary
- [ ] 100% unit test coverage

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-1.1.T1 | Write unit test: `test_full_context_builder_init()` | ✅ DONE | ✅ Yes |
| US-1.1.T2 | Write unit test: `test_load_full_source_code_returns_complete_file()` | ✅ DONE | ✅ Yes |
| US-1.1.T3 | Write unit test: `test_load_full_source_code_includes_line_numbers()` | ✅ DONE | ✅ Yes |
| US-1.1.T4 | Write unit test: `test_load_full_metadata_no_filtering()` | ✅ DONE | ✅ Yes |
| US-1.1.T5 | Write unit test: `test_load_full_metadata_loads_all_sources()` | ✅ DONE | ✅ Yes |
| US-1.1.T6 | Write unit test: `test_generate_enhanced_program_map_higher_limits()` | ✅ DONE | ✅ Yes |
| US-1.1.T7 | Write unit test: `test_build_full_context_combines_all()` | ✅ DONE | ✅ Yes |
| US-1.1.I1 | Create `full_context_builder.py` module | ✅ DONE | - |
| US-1.1.I2 | Implement `FullContextBuilder.__init__()` | ✅ DONE | - |
| US-1.1.I3 | Implement `load_full_source_code()` method | ✅ DONE | - |
| US-1.1.I4 | Implement `load_full_metadata()` method | ✅ DONE | - |
| US-1.1.I5 | Implement `generate_enhanced_program_map()` method | ✅ DONE | - |
| US-1.1.I6 | Implement `build_full_context()` method | ✅ DONE | - |
| US-1.1.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

### US-1.2: Enhanced Program Map Configuration

**User Story**: As a documentation generator, I want configurable program map limits (top_n_paragraphs, top_n_data_items), so that I can include more elements when using large context windows.

**Acceptance Criteria**:
- [ ] `top_n_paragraphs` is configurable (default: 30, max: unlimited)
- [ ] `top_n_data_items` is configurable (default: 20, max: unlimited)
- [ ] "Show all" mode works when limit is set to -1 or None
- [ ] Configuration loaded from YAML config file

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-1.2.T1 | Write unit test: `test_program_map_configurable_paragraph_limit()` | ✅ DONE | ✅ Yes |
| US-1.2.T2 | Write unit test: `test_program_map_configurable_data_item_limit()` | ✅ DONE | ✅ Yes |
| US-1.2.T3 | Write unit test: `test_program_map_show_all_mode()` | ✅ DONE | ✅ Yes |
| US-1.2.T4 | Write unit test: `test_program_map_config_from_yaml()` | ✅ DONE | ✅ Yes |
| US-1.2.I1 | Modify `generate_cobol_program_map()` signature for configurable limits | ✅ DONE | - |
| US-1.2.I2 | Add `program_map` section to `config.example.yaml` | ✅ DONE | - |
| US-1.2.I3 | Update `config_loader.py` to load program map config | ✅ DONE | - |
| US-1.2.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

### US-1.3: Dynamic Program Map Limits Based on Program Size

**User Story**: As a documentation generator, I want program map limits to automatically adjust based on program size, so that small programs show all elements while large programs show a meaningful subset.

**Acceptance Criteria**:
- [x] Small programs (< 100 paragraphs): Show all paragraphs and data items
- [x] Medium programs (100-500 paragraphs): Show top 200 paragraphs, top 100 data items
- [x] Large programs (500+ paragraphs): Show top 300 paragraphs, top 150 data items
- [x] Size thresholds are configurable
- [x] Automatic size detection from metadata

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-1.3.T1 | Write unit test: `test_dynamic_limits_small_program_shows_all()` | ✅ DONE | ✅ Yes |
| US-1.3.T2 | Write unit test: `test_dynamic_limits_medium_program_top_200()` | ✅ DONE | ✅ Yes |
| US-1.3.T3 | Write unit test: `test_dynamic_limits_large_program_top_300()` | ✅ DONE | ✅ Yes |
| US-1.3.T4 | Write unit test: `test_dynamic_limits_thresholds_configurable()` | ✅ DONE | ✅ Yes |
| US-1.3.T5 | Write unit test: `test_dynamic_limits_auto_detects_size()` | ✅ DONE | ✅ Yes |
| US-1.3.I1 | Create `ProgramSizeCategory` enum (SMALL, MEDIUM, LARGE) | ✅ DONE | - |
| US-1.3.I2 | Implement `detect_program_size()` function | ✅ DONE | - |
| US-1.3.I3 | Implement `get_dynamic_limits()` function | ✅ DONE | - |
| US-1.3.I4 | Add size threshold config to `config.example.yaml` | ✅ DONE | - |
| US-1.3.I5 | Integrate dynamic limits into `generate_cobol_program_map()` | ✅ DONE | - |
| US-1.3.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

### US-1.4: Tiered Detail Levels in Program Map

**User Story**: As a documentation generator, I want the program map to show different detail levels for different ranking tiers, so that the most important elements have full details while less important ones are summarized.

**Acceptance Criteria**:
- [x] Tier 1 (Top 50): Full details - line numbers, importance scores, relationships, comments
- [x] Tier 2 (Next 200): Names and scores only
- [x] Tier 3 (Remainder): Summary count only ("...and 847 more paragraphs")
- [x] Tier thresholds are configurable
- [x] Same tiering applies to both paragraphs and data items

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-1.4.T1 | Write unit test: `test_tiered_detail_tier1_full_details()` | ✅ DONE | ✅ Yes |
| US-1.4.T2 | Write unit test: `test_tiered_detail_tier2_names_scores_only()` | ✅ DONE | ✅ Yes |
| US-1.4.T3 | Write unit test: `test_tiered_detail_tier3_summary_count()` | ✅ DONE | ✅ Yes |
| US-1.4.T4 | Write unit test: `test_tiered_detail_thresholds_configurable()` | ✅ DONE | ✅ Yes |
| US-1.4.T5 | Write unit test: `test_tiered_detail_applies_to_data_items()` | ✅ DONE | ✅ Yes |
| US-1.4.I1 | Create `DetailTier` enum (FULL, SUMMARY, COUNT_ONLY) | ✅ DONE | - |
| US-1.4.I2 | Implement `format_paragraph_tier1()` - full details | ✅ DONE | - |
| US-1.4.I3 | Implement `format_paragraph_tier2()` - names and scores | ✅ DONE | - |
| US-1.4.I4 | Implement `format_paragraph_tier3()` - summary count | ✅ DONE | - |
| US-1.4.I5 | Implement `format_data_item_tier1()` - full details | ✅ DONE | - |
| US-1.4.I6 | Implement `format_data_item_tier2()` - names and scores | ✅ DONE | - |
| US-1.4.I7 | Implement `format_data_item_tier3()` - summary count | ✅ DONE | - |
| US-1.4.I8 | Add tier threshold config to `config.example.yaml` | ✅ DONE | - |
| US-1.4.I9 | Integrate tiered formatting into `generate_cobol_program_map()` | ✅ DONE | - |
| US-1.4.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

### US-1.5: Category-Based Mandatory Inclusion in Program Map ✅ DONE

**User Story**: As a documentation generator, I want certain categories of elements to always be included in the program map regardless of rank, so that critical elements like entry points and error handlers are never filtered out.

**Acceptance Criteria**:
- [x] Entry points (MAIN, START, INIT patterns) always included
- [x] External call sites (paragraphs with CALL statements) always included
- [x] Error handlers (ERR, ERROR, EXCEPTION patterns) always included
- [x] Mandatory categories are configurable
- [x] Mandatory items shown in separate "Critical Elements" section
- [x] Rank-based items shown after mandatory items

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-1.5.T1 | Write unit test: `test_category_inclusion_entry_points_always_included()` | ✅ DONE | ✅ Yes |
| US-1.5.T2 | Write unit test: `test_category_inclusion_call_sites_always_included()` | ✅ DONE | ✅ Yes |
| US-1.5.T3 | Write unit test: `test_category_inclusion_error_handlers_always_included()` | ✅ DONE | ✅ Yes |
| US-1.5.T4 | Write unit test: `test_category_inclusion_configurable_patterns()` | ✅ DONE | ✅ Yes |
| US-1.5.T5 | Write unit test: `test_category_inclusion_separate_section()` | ✅ DONE | ✅ Yes |
| US-1.5.T6 | Write unit test: `test_category_inclusion_no_duplicates()` | ✅ DONE | ✅ Yes |
| US-1.5.I1 | Define `MANDATORY_CATEGORIES` constant with default patterns | ✅ DONE | - |
| US-1.5.I2 | Implement `identify_entry_points()` function | ✅ DONE | - |
| US-1.5.I3 | Implement `identify_call_sites()` function | ✅ DONE | - |
| US-1.5.I4 | Implement `identify_error_handlers()` function | ✅ DONE | - |
| US-1.5.I5 | Implement `get_mandatory_elements()` function | ✅ DONE | - |
| US-1.5.I6 | Add "Critical Elements" section to program map format | ✅ DONE | - |
| US-1.5.I7 | Add mandatory category config to `config.example.yaml` | ✅ DONE | - |
| US-1.5.I8 | Integrate mandatory inclusion into `generate_cobol_program_map()` | ✅ DONE | - |
| US-1.5.I9 | Ensure no duplicates between mandatory and rank-based sections | ✅ DONE | - |
| US-1.5.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

## Epic 2: Section-Specific Full Context Generation Mode

### US-2.1: Full Context Mode Configuration ✅ DONE

**User Story**: As a user, I want to enable/disable full context mode via configuration, so that I can choose between filtered (cost-efficient) and full (comprehensive) modes.

**Acceptance Criteria**:
- [x] `full_context.enabled` config option exists
- [x] `full_context.sections` list defines which sections use full context
- [x] Configuration is loaded and available in AgentState
- [x] Default is `enabled: false` for backward compatibility

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-2.1.T1 | Write unit test: `test_full_context_config_enabled_flag()` | ✅ DONE | ✅ Yes |
| US-2.1.T2 | Write unit test: `test_full_context_config_sections_list()` | ✅ DONE | ✅ Yes |
| US-2.1.T3 | Write unit test: `test_full_context_default_disabled()` | ✅ DONE | ✅ Yes |
| US-2.1.T4 | Write unit test: `test_agent_state_includes_full_context_config()` | ✅ DONE | ✅ Yes |
| US-2.1.I1 | Add `full_context` section to `config.example.yaml` | ✅ DONE | - |
| US-2.1.I2 | Update `config_loader.py` to parse full context config | ✅ DONE | - |
| US-2.1.I3 | Add `use_full_context_mode` to `AgentState` TypedDict | ✅ DONE | - |
| US-2.1.I4 | Add `full_context_sections` to `AgentState` TypedDict | ✅ DONE | - |
| US-2.1.I5 | Update `generate_documentation()` function signature | ✅ DONE | - |
| US-2.1.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

### US-2.2: Section Context Strategy Selection ✅ DONE

**User Story**: As a documentation generator, I want different sections to use different context strategies, so that overview sections get full context while technical sections can use filtered context.

**Acceptance Criteria**:
- [x] `FULL_CONTEXT_SECTIONS` constant defines target sections
- [x] `get_context_strategy()` function returns correct strategy per section
- [x] `build_section_context()` branches correctly based on strategy
- [x] Full context builder is used for designated sections

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-2.2.T1 | Write unit test: `test_get_context_strategy_returns_full_for_target_sections()` | ✅ DONE | ✅ Yes |
| US-2.2.T2 | Write unit test: `test_get_context_strategy_returns_filtered_for_other_sections()` | ✅ DONE | ✅ Yes |
| US-2.2.T3 | Write unit test: `test_build_section_context_uses_full_context_builder()` | ✅ DONE | ✅ Yes |
| US-2.2.T4 | Write unit test: `test_build_section_context_falls_back_to_filtered()` | ✅ DONE | ✅ Yes |
| US-2.2.I1 | Define `FULL_CONTEXT_SECTIONS` constant | ✅ DONE | - |
| US-2.2.I2 | Create `get_context_strategy()` function | ✅ DONE | - |
| US-2.2.I3 | Modify `build_section_context()` to check strategy | ✅ DONE | - |
| US-2.2.I4 | Add full context builder branch in `build_section_context()` | ✅ DONE | - |
| US-2.2.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

## Epic 3: Per-Section LLM Calls with Full Context

### US-3.1: Executive Summary with Full Context ✅ DONE

**User Story**: As a documentation generator, I want the Executive Summary to be generated with full context (source + metadata + program map), so that the summary is comprehensive and includes narrative comments from source code.

**Acceptance Criteria**:
- [x] Executive Summary LLM call receives full source code
- [x] Executive Summary LLM call receives full metadata (unfiltered)
- [x] Executive Summary LLM call receives enhanced program map
- [x] Generated summary references actual code comments
- [x] Quality improvement measurable vs filtered mode

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-3.1.T1 | Write integration test: `test_executive_summary_full_context_includes_source()` | ✅ DONE | ✅ Yes |
| US-3.1.T2 | Write integration test: `test_executive_summary_full_context_includes_metadata()` | ✅ DONE | ✅ Yes |
| US-3.1.T3 | Write unit test: `test_executive_summary_prompt_construction()` | ✅ DONE | ✅ Yes |
| US-3.1.T4 | Write unit test: `test_executive_summary_extracts_narrative_comments()` | ✅ DONE | ✅ Yes |
| US-3.1.I1 | Update `section_requirements.py` for executive-summary | ✅ DONE | - |
| US-3.1.I2 | Create `build_executive_summary_prompt()` function | ✅ DONE | - |
| US-3.1.I3 | Integrate full context in `process_section_recursive()` for executive-summary | ✅ DONE | - |
| US-3.1.I4 | Add logging for full context activation | ✅ DONE | - |
| US-3.1.V1 | Run integration test - verify quality improvement | ✅ DONE | - |

---

### US-3.2: Key Responsibilities with Full Context ✅ DONE

**User Story**: As a documentation generator, I want Key Responsibilities to be generated with full context, so that responsibilities are derived from both narrative comments AND main driver paragraphs.

**Acceptance Criteria**:
- [x] Key Responsibilities receives full context
- [x] Responsibilities derived from source comments
- [x] Responsibilities correlated with CFG importance
- [x] Clear, specific responsibilities (not generic)

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-3.2.T1 | Write integration test: `test_key_responsibilities_full_context()` | ✅ DONE | ✅ Yes |
| US-3.2.T2 | Write unit test: `test_key_responsibilities_prompt_construction()` | ✅ DONE | ✅ Yes |
| US-3.2.T3 | Write unit test: `test_key_responsibilities_extracts_from_comments()` | ✅ DONE | ✅ Yes |
| US-3.2.I1 | Determine section structure (standalone vs subsection) | ✅ DONE | - |
| US-3.2.I2 | Create `build_key_responsibilities_prompt()` function | ✅ DONE | - |
| US-3.2.I3 | Update template instruction for full context usage | ✅ DONE | - |
| US-3.2.I4 | Integrate full context mode | ✅ DONE | - |
| US-3.2.V1 | Run integration test - verify quality improvement | ✅ DONE | - |

---

### US-3.3: Business Logic with Full Context ✅ DONE

**User Story**: As a documentation generator, I want Business Logic Explanation to be generated with full context, so that the explanation synthesizes narrative comments, CFG, DFG, and actual code.

**Acceptance Criteria**:
- [x] Business Logic receives full source code
- [x] Explanation references actual paragraph comments
- [x] CFG correlated with source code flow
- [x] Business rules extracted from code and comments

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-3.3.T1 | Write integration test: `test_business_logic_full_context()` | ✅ DONE | ✅ Yes |
| US-3.3.T2 | Write unit test: `test_business_logic_prompt_construction()` | ✅ DONE | ✅ Yes |
| US-3.3.T3 | Write unit test: `test_business_logic_synthesizes_sources()` | ✅ DONE | ✅ Yes |
| US-3.3.I1 | Verify `section_requirements.py` has `business-logic.extract_source = True` | ✅ DONE | - |
| US-3.3.I2 | Create `build_business_logic_prompt()` function | ✅ DONE | - |
| US-3.3.I3 | Update template instruction for synthesis guidance | ✅ DONE | - |
| US-3.3.I4 | Integrate full context mode | ✅ DONE | - |
| US-3.3.V1 | Run integration test - verify quality improvement | ✅ DONE | - |

---

### US-3.4: Overview with Full Context ✅ DONE

**User Story**: As a documentation generator, I want the Overview section to be generated with full context, so that it provides accurate program structure and purpose.

**Acceptance Criteria**:
- [x] Overview receives full context
- [x] Accurate program structure from source
- [x] Purpose derived from comments
- [x] Division details accurate

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-3.4.T1 | Write integration test: `test_overview_full_context()` | ✅ DONE | ✅ Yes |
| US-3.4.T2 | Write unit test: `test_overview_prompt_construction()` | ✅ DONE | ✅ Yes |
| US-3.4.I1 | Create `build_overview_prompt()` function | ✅ DONE | - |
| US-3.4.I2 | Integrate full context mode for overview | ✅ DONE | - |
| US-3.4.V1 | Run integration test - verify quality improvement | ✅ DONE | - |

---

### US-3.5: Data Flow with Full Context ✅ DONE

**User Story**: As a documentation generator, I want Data Flow analysis to be generated with full context, so that it can trace complete data transformations from source code.

**Acceptance Criteria**:
- [x] Data Flow receives full source code
- [x] MOVE/COMPUTE/READ/WRITE traced in source
- [x] High-Level vs Full mode configurable
- [x] Accurate data lineage

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-3.5.T1 | Write integration test: `test_data_flow_full_context()` | ✅ DONE | ✅ Yes |
| US-3.5.T2 | Write unit test: `test_data_flow_prompt_construction()` | ✅ DONE | ✅ Yes |
| US-3.5.T3 | Write unit test: `test_data_flow_high_level_vs_full_mode()` | ✅ DONE | ✅ Yes |
| US-3.5.I1 | Update `section_requirements.py` for data-flow-analysis | ✅ DONE | - |
| US-3.5.I2 | Create `build_data_flow_prompt()` function | ✅ DONE | - |
| US-3.5.I3 | Add High-Level vs Full mode configuration | ✅ DONE | - |
| US-3.5.I4 | Integrate full context mode | ✅ DONE | - |
| US-3.5.V1 | Run integration test - verify quality improvement | ✅ DONE | - |

---

## Epic 4: Context Chaining for Cross-Section Consistency

### US-4.1: Context Chaining Mechanism ✅ DONE

**User Story**: As a documentation generator, I want to pass output from previous sections as context to subsequent sections, so that documentation is consistent across all sections.

**Acceptance Criteria**:
- [x] Previous section outputs stored in state
- [x] `build_chained_context()` function exists
- [x] Section processing order defined
- [x] Context chaining configurable (on/off)

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-4.1.T1 | Write unit test: `test_context_chaining_stores_previous_outputs()` | ✅ DONE | ✅ Yes |
| US-4.1.T2 | Write unit test: `test_build_chained_context_includes_previous()` | ✅ DONE | ✅ Yes |
| US-4.1.T3 | Write unit test: `test_context_chaining_order()` | ✅ DONE | ✅ Yes |
| US-4.1.T4 | Write unit test: `test_context_chaining_disabled()` | ✅ DONE | ✅ Yes |
| US-4.1.I1 | Add `previous_sections_output` to `AgentState` | ✅ DONE | - |
| US-4.1.I2 | Create `build_chained_context()` function | ✅ DONE | - |
| US-4.1.I3 | Define `FULL_CONTEXT_SECTION_ORDER` constant | ✅ DONE | - |
| US-4.1.I4 | Modify `process_section_recursive()` for chaining | ✅ DONE | - |
| US-4.1.I5 | Add `context_chaining.enabled` config option | ✅ DONE | - |
| US-4.1.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

## Epic 5: Enhanced Prompt Templates

### US-5.1: Executive Summary Template Update ✅ DONE

**User Story**: As a documentation generator, I want the Executive Summary template to leverage full source code, so that the prompt guides the LLM to extract narrative comments.

**Acceptance Criteria**:
- [x] Instruction references IDENTIFICATION DIVISION comments
- [x] Instruction mentions REMARKS, AUTHOR, PROGRAM-ID
- [x] Instruction guides correlation with metadata
- [x] No breaking changes to existing functionality

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-5.1.T1 | Write test: `test_executive_summary_template_backward_compatible()` | ✅ DONE | ✅ Yes |
| US-5.1.I1 | Review current instruction in `cobol-doc-template.yaml` | ✅ DONE | - |
| US-5.1.I2 | Update instruction to reference source code sections | ✅ DONE | - |
| US-5.1.I3 | Add instruction for REMARKS/AUTHOR extraction | ✅ DONE | - |
| US-5.1.I4 | Add instruction for metadata correlation | ✅ DONE | - |
| US-5.1.V1 | Run test - verify backward compatibility | ✅ DONE | - |

---

### US-5.2: Business Logic Template Update ✅ DONE

**User Story**: As a documentation generator, I want the Business Logic template to guide synthesis of multiple sources, so that explanations are comprehensive.

**Acceptance Criteria**:
- [x] Instruction references paragraph comments
- [x] Instruction guides CFG-source correlation
- [x] Instruction for business rule extraction
- [x] No breaking changes

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-5.2.T1 | Write test: `test_business_logic_template_backward_compatible()` | ✅ DONE | ✅ Yes |
| US-5.2.I1 | Review current instruction | ✅ DONE | - |
| US-5.2.I2 | Update for paragraph comment references | ✅ DONE | - |
| US-5.2.I3 | Add CFG correlation guidance | ✅ DONE | - |
| US-5.2.I4 | Add business rule extraction guidance | ✅ DONE | - |
| US-5.2.V1 | Run test - verify backward compatibility | ✅ DONE | - |

---

### US-5.3: Full Context Prompt Wrapper ✅ DONE

**User Story**: As a documentation generator, I want a standardized prompt wrapper for full context sections, so that the LLM understands how to use each context component.

**Acceptance Criteria**:
- [x] `build_full_context_system_prompt()` function exists
- [x] `build_full_context_user_prompt()` function exists
- [x] Prompt explains role of Program Map, Metadata, Source
- [x] Ordering: Program Map → Metadata → Source Code

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-5.3.T1 | Write unit test: `test_full_context_system_prompt_structure()` | ✅ DONE | ✅ Yes |
| US-5.3.T2 | Write unit test: `test_full_context_user_prompt_structure()` | ✅ DONE | ✅ Yes |
| US-5.3.T3 | Write unit test: `test_full_context_prompt_ordering()` | ✅ DONE | ✅ Yes |
| US-5.3.I1 | Design prompt structure document | ✅ DONE | - |
| US-5.3.I2 | Create `build_full_context_system_prompt()` | ✅ DONE | - |
| US-5.3.I3 | Create `build_full_context_user_prompt()` | ✅ DONE | - |
| US-5.3.I4 | Add instructions explaining context components | ✅ DONE | - |
| US-5.3.V1 | Run all unit tests - verify 100% pass | ✅ DONE | - |

---

## Epic 6: Testing and Validation

### US-6.1: Unit Test Suite ✅ DONE

**User Story**: As a developer, I want comprehensive unit tests for all new functionality, so that code quality is maintained.

**Acceptance Criteria**:
- [x] `test_full_context_builder.py` exists
- [x] All new functions have unit tests
- [x] 100% pass rate
- [x] Tests run in < 30 seconds

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-6.1.I1 | Create `test_full_context_builder.py` file | ✅ DONE | - |
| US-6.1.I2 | Create `test_full_context_mode.py` file | ✅ DONE | - |
| US-6.1.I3 | Create `test_context_chaining.py` file | ✅ DONE | - |
| US-6.1.I4 | Create `test_full_context_prompts.py` file | ✅ DONE | - |
| US-6.1.V1 | Run full unit test suite - verify 100% pass | ✅ DONE | - |

---

### US-6.2: Integration Test Suite ✅ DONE

**User Story**: As a developer, I want end-to-end integration tests, so that the complete workflow is validated.

**Acceptance Criteria**:
- [x] `test_full_context_integration.py` exists
- [x] Test COBOL program with rich comments created
- [x] All full context sections tested
- [x] Quality comparison vs filtered mode

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-6.2.I1 | Create `test_full_context_integration.py` file | ✅ DONE | - |
| US-6.2.I2 | Create test COBOL program with narrative comments | ✅ DONE | - |
| US-6.2.I3 | Create test metadata files | ✅ DONE | - |
| US-6.2.I4 | Write integration test for each full context section | ✅ DONE | - |
| US-6.2.I5 | Write quality comparison test | ✅ DONE | - |
| US-6.2.V1 | Run integration tests - verify pass | ✅ DONE | - |

---

### US-6.3: Mock LLM Tests ✅ DONE

**User Story**: As a developer, I want tests that use mocked LLM responses, so that tests are fast and don't require API calls.

**Acceptance Criteria**:
- [x] `MockLLM` class exists
- [x] Mock responses per section type
- [x] Prompt construction validated without API calls
- [x] Tests run without network access

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-6.3.I1 | Create `MockLLM` class | ✅ DONE | - |
| US-6.3.I2 | Create mock response fixtures | ✅ DONE | - |
| US-6.3.I3 | Write tests using mock LLM | ✅ DONE | - |
| US-6.3.V1 | Run mock tests - verify 100% pass | ✅ DONE | - |

---

## Epic 7: Configuration and Documentation

### US-7.1: Configuration Schema Update ✅ DONE

**User Story**: As a user, I want clear configuration options for full context mode, so that I can easily enable and customize the feature.

**Acceptance Criteria**:
- [x] `full_context` section in config
- [x] All options documented with inline comments
- [x] Example config file created

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-7.1.I1 | Add `full_context` section to `config.example.yaml` | ✅ DONE | - |
| US-7.1.I2 | Add `enabled` option with default `false` | ✅ DONE | - |
| US-7.1.I3 | Add `sections` list option | ✅ DONE | - |
| US-7.1.I4 | Add `program_map.top_n_paragraphs` option | ✅ DONE | - |
| US-7.1.I5 | Add `program_map.top_n_data_items` option | ✅ DONE | - |
| US-7.1.I6 | Add `context_chaining.enabled` option | ✅ DONE | - |
| US-7.1.I7 | Add inline documentation comments | ✅ DONE | - |
| US-7.1.I8 | Create `config.full-context.yaml` example | ✅ DONE | - |

---

## Epic 8: Backward Compatibility

### US-8.1: Backward Compatibility Guarantee ✅ DONE

**User Story**: As a user with existing configuration, I want the new features to be opt-in, so that my existing workflows continue to work.

**Acceptance Criteria**:
- [x] Default is `full_context.enabled: false`
- [x] Existing configs work without modification
- [x] No regressions in existing tests
- [x] Existing filtering logic preserved when disabled

#### Atomic Tasks:

| ID | Task | Status | Test First? |
|----|------|--------|-------------|
| US-8.1.T1 | Write test: `test_backward_compatibility_existing_config()` | ✅ DONE | ✅ Yes |
| US-8.1.T2 | Write test: `test_two_pass_mode_still_works()` | ✅ DONE | ✅ Yes |
| US-8.1.T3 | Write test: `test_filtering_preserved_when_disabled()` | ✅ DONE | ✅ Yes |
| US-8.1.I1 | Set default `enabled: false` | ✅ DONE | - |
| US-8.1.I2 | Ensure conditional logic for full context | ✅ DONE | - |
| US-8.1.V1 | Run existing test suite - verify no regressions | ✅ DONE | - |

---

# Summary Statistics

| Epic | User Stories | Total Tasks | Tests | Implementation | Validation |
|------|--------------|-------------|-------|----------------|------------|
| Epic 1: Full Context Builder | 5 | 64 | 27 | 32 | 5 |
| Epic 2: Section-Specific Mode | 2 | 19 | 8 | 9 | 2 |
| Epic 3: Per-Section LLM Calls | 5 | 40 | 17 | 18 | 5 |
| Epic 4: Context Chaining | 1 | 10 | 4 | 5 | 1 |
| Epic 5: Enhanced Prompts | 3 | 19 | 7 | 9 | 3 |
| Epic 6: Testing | 3 | 14 | 0 | 13 | 1 |
| Epic 7: Configuration | 1 | 8 | 0 | 8 | 0 |
| Epic 8: Backward Compatibility | 1 | 6 | 3 | 2 | 1 |
| **TOTAL** | **21** | **180** | **66** | **96** | **18** |

### New Program Map Enhancement Tasks Breakdown:
- US-1.3 (Dynamic Limits): 11 tasks (5 tests, 5 impl, 1 validation)
- US-1.4 (Tiered Details): 15 tasks (5 tests, 9 impl, 1 validation)
- US-1.5 (Category Inclusion): 16 tasks (6 tests, 9 impl, 1 validation)

---

# Recommended Implementation Order

## Phase 1: Foundation
1. US-1.1: Full Context Builder Class
2. US-1.2: Enhanced Program Map Configuration
3. US-1.3: Dynamic Program Map Limits Based on Program Size
4. US-1.4: Tiered Detail Levels in Program Map
5. US-1.5: Category-Based Mandatory Inclusion in Program Map
6. US-6.1: Unit Test Suite (parallel)

## Phase 2: Core Integration
7. US-2.1: Full Context Mode Configuration
8. US-2.2: Section Context Strategy Selection
9. US-8.1: Backward Compatibility (parallel)

## Phase 3: Section Implementation
10. US-3.1: Executive Summary with Full Context
11. US-3.2: Key Responsibilities with Full Context
12. US-3.3: Business Logic with Full Context
13. US-3.4: Overview with Full Context
14. US-3.5: Data Flow with Full Context

## Phase 4: Enhancement
15. US-4.1: Context Chaining Mechanism
16. US-5.1: Executive Summary Template Update
17. US-5.2: Business Logic Template Update
18. US-5.3: Full Context Prompt Wrapper

## Phase 5: Finalization
19. US-6.2: Integration Test Suite
20. US-6.3: Mock LLM Tests
21. US-7.1: Configuration Schema Update

---

# Definition of Done

Each task is DONE when:
- ✅ Test written FIRST (for T-prefixed tasks)
- ✅ Code passes all tests
- ✅ No regressions in existing tests
- ✅ Code follows project style
- ✅ Docstrings added where needed

---

# Files to Create/Modify

## New Files
- `full_context_builder.py` - Core full context assembly
- `test_full_context_builder.py` - Unit tests
- `test_full_context_mode.py` - Mode tests
- `test_full_context_integration.py` - Integration tests
- `test_context_chaining.py` - Chaining tests
- `test_full_context_prompts.py` - Prompt tests
- `config.full-context.yaml` - Example config

## Modified Files
- `cobol_doc_agent.py` - Main agent (add full context branch)
- `cobol_program_map.py` - Configurable limits
- `section_requirements.py` - Update source extraction flags
- `config_loader.py` - Load new config options
- `config.example.yaml` - Add full_context section
- `cobol-doc-template.yaml` - Update instructions

---

# Implementation Verification Summary

**Verification Date**: 2025-12-03

## Epic Verification Results

| Epic | User Stories | Status | Tests Passed | Notes |
|------|-------------|--------|--------------|-------|
| Epic 1: Full Context Builder | US-1.1 to US-1.5 | ✅ VERIFIED | 64/64 | All tasks complete |
| Epic 2: Section Context Mode | US-2.1, US-2.2 | ✅ VERIFIED | 25/25 | All tasks complete |
| Epic 3: Per-Section LLM | US-3.1 to US-3.5 | ✅ VERIFIED | 38/38 | All tasks complete |
| Epic 4: Context Chaining | US-4.1 | ✅ VERIFIED | 33/33 | All tests pass |
| Epic 5: Enhanced Prompts | US-5.1 to US-5.3 | ✅ VERIFIED | 39/39 | All tests pass |
| Epic 6: Testing & Validation | US-6.1 to US-6.3 | ✅ VERIFIED | 61/61 | All tests pass |
| Epic 7: Configuration | US-7.1 | ✅ VERIFIED | 13/13 | Config schema complete |
| Epic 8: Backward Compat | US-8.1 | ✅ VERIFIED | 6/6 | All tasks complete |

## Final Test Results

- **Total Tests**: 360
- **Passed**: 353
- **Failed**: 7 (all due to missing `langchain_core` environment dependency)
- **Pass Rate**: 98.1%

## Key Files Verified

| File | Purpose | Status |
|------|---------|--------|
| `context_chain.py` | Context chaining logic | ✅ Implemented |
| `full_context_prompts.py` | Section-specific prompts | ✅ Implemented |
| `config.full-context.yaml` | Example configuration | ✅ Created |
| `config.example.yaml` | Updated with context_chaining | ✅ Updated |
| `config_loader.py` | Full context config loading | ✅ Updated |

## Integration Points Verified

1. **Context Chaining Integration**: ✅
   - `ContextChain` class stores section outputs
   - `build_chained_context()` builds chained prompts
   - `FULL_CONTEXT_SECTION_ORDER` defines processing order

2. **Prompt Template Integration**: ✅
   - Section-specific prompt builders implemented
   - Generic fallback for unknown sections
   - Consistent structure across all prompts

3. **Configuration Integration**: ✅
   - `full_context.enabled` config option
   - `full_context.sections` list option
   - `context_chaining.enabled` config option
   - `context_chaining.max_tokens` option

4. **Testing Integration**: ✅
   - Unit tests for all modules
   - Integration tests with COBOL fixtures
   - Mock LLM tests for API-free testing

