---
id: gemini_dd8c80acc24213f1
title: Organizing Obsidian Vaults with Gemini
source: gemini
url: "https://gemini.google.com/app/dd8c80acc24213f1"
created: "2026-10-06T09:08:44+08:00"
modified: "2026-10-06T09:08:44+08:00"
tags:
  - ai-conversation
  - gemini
message_count: 10
---

> [!QUESTION] User
> I have an Obsidian knowledge base with around 1700 markdown files. I am planning to use Gemini CLI to organize my knowledge base. Do you have any tips?

> [!NOTE] Gemini
> Organizing 1,700 Markdown files with an LLM CLI is very doable, but running bulk automated operations across a live personal knowledge base can quickly break internal wiki links, corrupt YAML frontmatter, or hallucinate taxonomies.
> 
> Here are the practical tips and a recommended pipeline to do this safely and cleanly.
> 
> ### 1\. Safety & Vault Integrity First
> 
> -   **Initialize Git before touching anything:** Run `git init`, stage all files, and commit. If a script mangles formatting or breaks relative links, `git reset --hard` will instantly save your vault.
>     
> -   **Work in a sandbox clone:** Do not run experimental batch scripts directly on your live Obsidian directory. Copy the vault to an isolated working directory (e.g., `vault-staging/`) and disable Obsidian background syncing (Obsidian Sync, iCloud, or OneDrive) during the batch runs.
>     
> -   **Keep your `.obsidian/` folder excluded:** Ensure all globbing, searching, and batch operations exclude hidden directories (`.obsidian`, `.trash`, `.git`) so you don’t corrupt internal workspace settings or plugin caches.
>     
> 
> ### 2\. Don’t Let the CLI Move Files (Let It Suggest Metadata)
> 
> -   **Moving files breaks links:** If you have Obsidian set to relative paths or shortest path without Obsidian actively open to track link refactors, moving files via bash will orphan your `[[wikilinks]]`.
>     
> -   **Use YAML frontmatter instead of physical folders:** Let Gemini CLI suggest or update standardized frontmatter fields (`category`, `tags`, `type`, `status`) rather than rearranging directory trees. Once the metadata is clean, you can use Dataview, Obsidian tags, or the Auto Note Mover plugin to reorganize physically if needed.
>     
> -   **Preserve existing frontmatter:** Use headless prompts that output strict, valid YAML blocks or use a wrapper script with Python's `python-frontmatter` to inject new attributes without overwriting custom dates, aliases, or IDs.
>     
> 
> ### 3\. Establish a Context File (`GEMINI.md`)
> 
> Gemini CLI looks hierarchically for project instructions via `GEMINI.md`. Placing one at the root of your working vault keeps every query grounded to your personal taxonomy.
> 
> Gemini CLI
> 
> Define strict constraints in `GEMINI.md`:
> 
> -   **Fixed taxonomy:** Provide a closed list of allowable parent tags/categories (e.g., `#math`, `#dev`, `#finance`, `#reading`, `#journal`). If you leave it open-ended, the model will invent hundreds of near-synonyms (`#machine-learning`, `#ml`, `#deep-learning`).
>     
> -   **Preserve syntax:** Explicitly forbid rewriting Obsidian-specific elements such as math blocks (`$...$` and `$$...$$`), callouts (`> [!note]`), and `[[wikilinks]]`.
>     
> -   **Output format:** Instruct it to output only raw, valid JSON or YAML without conversational preamble.
>     
> 
> ### 4\. Two-Pass Strategy: Catalog First, Modify Second
> 
> Never attempt to read and rewrite 1,700 notes in a single command. Split the project into two distinct passes:
> 
> #### Pass 1: Build a Lightweight Manifest (Global View)
> 
> Before modifying individual notes, build an index of the entire vault to discover global themes and duplicate concepts.
> 
> -   Extract just the filename, existing frontmatter, headings, and first 10 lines of each note into a single summary file (`vault_index.jsonl`).
>     
> -   Use Gemini CLI with its large context window to inspect the entire index and output a unified, consistent taxonomy proposal and Map of Content (MOC) structure.
>     
> 
> #### Pass 2: Batch Enrich in Controlled Chunks
> 
> Once your target taxonomy is defined, run headless batch calls against individual notes or batches of 20–50 notes using a shell script or Python wrapper:
> 
> Bash
> 
> ```
> # Example headless processing loop
> for note in notes/*.md; do
>   # Extract tags/metadata into structured JSON
>   gemini --output-format json -p \
>     "Analyze @$note against the taxonomy defined in GEMINI.md. Return a JSON object with: {tags: [...], category: '...', summary: '...'}" \
>     > "metadata/$(basename "$note" .md).json"
>   
>   # Small sleep to respect rate limits if running against API tiers
>   sleep 0.5
> done
> ```
> 
> ### 5\. Automated Link & MOC Generation
> 
> -   **Identify orphan notes:** Write a quick script to find notes with zero backlinks or forward links. Feed these orphan notes into Gemini CLI along with your major index notes and ask: *"Which of these existing index files should link to this note, and under what context?"*
>     
> -   **Generate Maps of Content (MOCs):** Group notes by category and pass the list of note titles to Gemini CLI to generate curated index notes with logical subsections (e.g., *Core Concepts*, *Methods*, *References*).
>     
> 
> ### 6\. Edge Cases to Guard Against
> 
> -   **Large attachments and canvas files:** Filter out `.canvas`, images, PDFs, and binary attachments from your file list so you don't feed binary data into CLI prompts.
>     
> -   **Token spikes on long notes:** Some notes (e.g., pasted logs, long reading highlights) might be tens of thousands of words. Truncate inputs to the first ~3,000 words or only feed headers and summaries for categorization tasks to keep processing fast and cost-effective.
>     
> -   **Diff verification:** Always run `git diff` after processing a test batch of 20 files. Inspect the changes in VS Code or your terminal to verify that line breaks, LaTeX notation, and frontmatter separators (`---`) remained intact before running the rest of the 1,700 files.
>     
> 
> Want a Python wrapper script to safely batch process and inject YAML frontmatter?
> 
> Yes

> [!QUESTION] User
> I also wanted to use Gemini CLI to recall specific topic/theme and create an MOC. Do you have any other tips?

> [!NOTE] Gemini
> Using Gemini CLI to recall themes across 1,700 notes and generate Maps of Content (MOCs) works best when you treat the CLI as an indexer and synthesizer rather than a raw search engine. Passing all 1,700 full markdown files directly into one query introduces noise, degrades attention, and wastes tokens.
> 
> The following tips and workflows make thematic recall and MOC generation fast, accurate, and Obsidian-native.
> 
> ### 1\. Two-Tier Retrieval (Filter Before Synthesizing)
> 
> A Map of Content should link to notes that actually exist, using clean `[[wikilinks]]`. To make synthesis reliable:
> 
> 1.  **Surface Candidates First:** Use fast local file-search tools (`rg` or `grep`) to pull note candidates based on keywords, tags, or frontmatter rather than reading the entire vault.
>     
> 2.  **Feed File References to Gemini CLI:** Use the CLI's file reference syntax (`@path/to/file.md` or piped content) so the model gets exact context from relevant notes.
>     
>     Medium
>     
> 
> Bash
> 
> ```
> # Example: Find all notes mentioning 'volatility' or tagged #finance/risk
> rg -l -i "(volatility|garch|value at risk)" notes/ > topic_notes.txt
> 
> # Pass the candidate files into Gemini CLI to synthesize an MOC
> gemini -p "You are an expert PKM curator. Read the notes listed below and generate a structured Map of Content (MOC). Use standard Obsidian [[Note Title]] links. Categorize by Foundations, Models & Methods, and Applied Use Cases. Notes: $(cat topic_notes.txt | sed 's/^/@/')" > "MOC - Volatility Modeling.md"
> ```
> 
> ### 2\. Standardize Your MOC Prompt Structure
> 
> Provide Gemini CLI with a strict template so the output requires zero manual cleanup before opening it in Obsidian. Add this prompt recipe to your workflow or project instructions:
> 
> Markdown
> 
> ```
> Generate an Obsidian Map of Content (MOC) for the topic "[TOPIC]".
> 
> Guidelines:
> 1. Every entry MUST use exact Obsidian wikilink syntax: [[Filename Without Extension]].
> 2. Include a 1-sentence contextual summary next to each link explaining what the note contributes to the topic.
> 3. Organize into logical conceptual hierarchies (e.g., Core Principles, Techniques, References/Datasets, Open Questions), NOT alphabetical dumps.
> 4. Add an "Identified Gaps" section at the end pointing out logical missing steps or conceptual holes in my current knowledge base.
> 5. Do not include markdown code block backticks around the whole file; output pure markdown with YAML frontmatter.
> ```
> 
> ### 3\. Maintain a "Vault Ledger" (`vault_manifest.tsv`)
> 
> For high-level thematic queries where you don't know the exact keywords beforehand (e.g., *"Find all notes that deal with habit formation or routine design, even if they don't explicitly use those words"*), maintain a lightweight manifest file.
> 
> Generate a single compact text file containing:
> 
> ```
> filepath | title | tags | first_heading | short_summary
> ```
> 
> Because this file is only 1,700 lines (roughly 50,000 to 80,000 tokens), it easily fits within Gemini's context window. You can ask Gemini CLI high-level recall queries against just this single ledger:
> 
> Bash
> 
> ```
> gemini -p "Using @vault_manifest.tsv, find all note titles relevant to 'time series analysis and forecasting'. Group them by maturity/depth based on their summaries and output a draft MOC."
> ```
> 
> Once it picks the top 20 candidate notes from the manifest, you can feed only those 20 full notes to generate the detailed synthesis.
> 
> ### 4\. Interactive Refining via CLI REPL
> 
> Instead of running a one-off headless command, use the CLI's interactive REPL:
> 
> GitHub
> 
> Bash
> 
> ```
> gemini -i "I want to build an MOC for my notes on Numerical Optimization. Let's look at the candidate notes first."
> ```
> 
> During the interactive session:
> 
> -   **Inspect & prune:** Ask Gemini: *"List the 15 most relevant files you found. Which ones seem tangential or redundant?"*
>     
> -   **Refine hierarchy:** Direct it: *"Combine the 'Stochastic Methods' and 'Heuristics' sections, and add a quick Dataview query block at the bottom."*
>     
> -   **Checkpoint your session:** If you are exploring deep connections across multiple topics, use `/chat save moc-brainstorm` so you can resume the exact context later.
>     
>     Medium
>     
> 
> ### 5\. Add Dynamic Dataview Blocks to the MOC
> 
> A static MOC gets outdated as soon as you create new notes. Instruct Gemini CLI to blend curated manual links with automated Dataview queries:
> 
> -   **Curated core:** Gemini lists the definitive foundational notes you already wrote.
>     
> -   **Dynamic tracking:** Gemini adds a Dataview block at the bottom of the MOC to capture future incoming notes:
>     
> 
> Markdown
> 
> ````
> ## Recently Added / Unsorted
> ```dataview
> TABLE file.mtime AS "Modified"
> FROM #topic/tag
> WHERE !contains(file.outlinks, this.file.link)
> SORT file.mtime DESC
> LIMIT 10
> \```
> ````
> 
> ### 6\. Gap Discovery (The Real Value of LLM MOCs)
> 
> The most valuable part of using Gemini for MOCs is discovering blind spots. After it drafts the links, prompt it:
> 
> > *"Based on the concepts covered in this MOC, what fundamental theorems, counter-arguments, or prerequisite concepts are completely missing from my vault? Output them as a list of stub note recommendations (`[[Suggested Note Title]]`) with a 1-sentence prompt for each."*
> 
> This turns your MOC from a simple bookmark list into an active research agenda.
> 
> Want a bash/Python script to auto-generate the lightweight vault manifest (vault\_manifest.tsv)?
> 
> Yes

> [!QUESTION] User
> I wanted to explore workflows involving the use of Gemini CLI with an Obsidian knowledge base. Give me best use cases and recommendations.

> [!NOTE] Gemini
> Pairing **Gemini CLI** with an Obsidian vault bridges terminal-based automation with a local-first personal knowledge base. Because Obsidian vaults are plain-text Markdown files, you can treat your notes as a code repository—using Unix tools, git, and LLM processing pipelines without relying on heavy graphical plugins.
> 
> GitHub\+ 1
> 
> ### Core Architecture & Recommended Setup
> 
> 1.  **Vault Configuration via `GEMINI.md`:**
>     
>     Place a `.gemini/GEMINI.md` file in the root of your vault. This acts as a persistent system prompt, setting ground rules for every command:
>     
>     GitHub
>     
>     -   Never alter Obsidian syntax (e.g., `[[wikilinks]]`, `![[embeds]]`, Dataview blocks, LaTeX math blocks `$...$`).
>         
>     -   Preserve frontmatter schema (`tags`, `aliases`, `created`, `status`).
>         
>     -   Specify preferred note style (e.g., atomic, Zettelkasten, evergreen).
>         
> 2.  **Custom Slash Commands (`.gemini/commands/`):**
>     
>     Create reusable prompts as TOML or Markdown definitions in `.gemini/commands/`. For example, a command file `/synthesize` or `/moc` lets you invoke common routines directly from the interactive REPL without retyping prompt constraints.
>     
> 
> ### High-Impact Use Cases
> 
> #### 1\. Automated "Inbox" Triage & Atomic Extraction
> 
> -   **Problem:** Dumping raw meeting notes, read-it-later article clippings, or transcripts into an `Inbox/` folder creates a backlog that is tedious to process manually.
>     
> -   **Workflow:** Run a headless CLI script to parse new notes in `Inbox/`, summarize key insights into atomic permanent notes, and link them to existing relevant files.
>     
> -   **CLI Pattern:**
>     
>     Bash
>     
>     ```
>     for f in Inbox/*.md; do
>       gemini -p "Read @$f and split it into atomic concept notes following the instructions in GEMINI.md. Output each concept note with standard [[wikilinks]] and frontmatter."
>     done
>     ```
>     
> 
> #### 2\. Cross-Vault Synthetic Reviews (Weekly / Monthly Rollups)
> 
> -   **Problem:** Periodic reviews often turn into passive reading of daily logs without extracting longitudinal patterns.
>     
> -   **Workflow:** Feed a week's or month's worth of daily notes into Gemini CLI to extract recurring themes, completed milestones, blockers, and project shifts.
>     
> -   **CLI Pattern:**
>     
>     Bash
>     
>     ```
>     # Concatenate the past 7 daily notes and generate a structured retrospective
>     cat Daily/2026-09-*.md | gemini -p "Analyze these daily logs. Group accomplishments by project, identify friction points mentioned more than twice, and suggest 3 high-priority focus areas for next week." \> "Reviews/2026-W39 Review.md"
>     ```
>     
> 
> #### 3\. Dynamic Map of Content (MOC) & Cluster Generation
> 
> -   **Problem:** As topic clusters grow to 50+ notes, manually curating an MOC takes significant time, and notes become orphaned.
>     
> -   **Workflow:** Pipe search results from `ripgrep` or a metadata filter into Gemini CLI to build an annotated index with logical hierarchies and identify gaps.
>     
> -   **CLI Pattern:**
>     
>     Bash
>     
>     ```
>     # Find notes containing specific concepts and generate an index
>     rg -l -t md "(GARCH|volatility|stochastic)" notes/ \> /tmp/risk_notes.txt
>     gemini -p "Using the note files listed in @/tmp/risk_notes.txt, draft a structured Map of Content. Format every reference as [[Note Title]] and add a 1-sentence note on its conceptual purpose." \> "MOC - Volatility Modeling.md"
>     ```
>     
> 
> #### 4\. Orphan Auditing & Link Suggestion Engine
> 
> -   **Problem:** Notes without inbound or outbound links become dead ends in a knowledge graph.
>     
> -   **Workflow:** Identify notes with zero `[[...]]` links using a lightweight Python or bash script, then pass the note's summary and a list of your top 20 core index files to Gemini CLI:
>     
>     Bash
>     
>     ```
>     gemini -p "Given the orphan note @notes/concept-a.md and the index files in @MOCs/, identify the 2 most relevant MOCs this note should belong to and write the precise markdown bullet point to insert."
>     ```
>     
> 
> #### 5\. Literature & Source Synthesis
> 
> -   **Problem:** Reading notes from books, research papers, or documentation need to be translated into your own conceptual framework.
>     
> -   **Workflow:** Use Gemini's multimodal/large-window capability to digest long papers or book summaries and extract them into your personal Zettelkasten format:
>     
>     Bash
>     
>     ```
>     gemini -p "Read @sources/paper_attention.pdf. Extract: 1. Core thesis. 2. Practical trade-offs. 3. Three [[Concept Note]] ideas linking to my existing deep learning notes." \> "Sources/Attention Mechanism Summary.md"
>     ```
>     
> 
> ### Best Practices & Operational Recommendations
> 
> | Area | Best Practice | Rationale |
> | --- | --- | --- |
> | Safety | Always run git commit before running batch CLI updates. | If a model hallucinates a file rewrite or strips markdown syntax, git checkout . will instantly recover your vault. |
> | File I/O | Prefer appending or creating new staging notes over in-place overwrites. | In-place edits risk wiping out custom Dataview queries, canvas embeds, or manual marginalia. |
> | Execution | Use -p (headless mode) for automated bash/cron pipelines, and -i (interactive) for conceptual MOC curation. | Headless is fast for batch classification; interactive allows iterative pruning of suggested links. |
> | Context | Use @file.md references rather than dumping full vault text. | Targeted @ file inclusions keep response latency low and prevent the model from drifting into unrelated topics. |
> | Obsidian Sync | Pause background sync clients while running heavy batch CLI operations. | Prevents sync conflict files (Note (1).md) while scripts write to multiple files rapidly. |
> 
> ### Recommended Automation Pipeline: Quick-Capture CLI Alias
> 
> To quickly capture ideas from anywhere in your terminal directly into your vault:
> 
> Bash
> 
> ```
> # Add to your ~/.zshrc or ~/.bashrc
> vault_log() {
>   local vault_path="$HOME/Documents/ObsidianVault"
>   local today=$(date +'%Y-%m-%d')
>   local input="$*"
>   
>   # Polish the raw thought and append it to today's daily log
>   gemini -p "Format this thought into a clean markdown log item with relevant [[concept]] wikilinks: $input" \
>     >> "$vault_path/Daily/$today.md"
> }
> ```
> 
> Usage:
> 
> Bash
> 
> ```
> vault_log "Read about GARCH conditional variance forecasting; need to check how it handles student-t error distributions."
> ```
> 
> Want a sample .gemini/GEMINI.md file tailored specifically to Obsidian PKM workflows?
> 
> Yes

> [!QUESTION] User
> Generate an optimized .gemini/GEMINI.md context file designed for managing an Obsidian knowledge base with strict link and frontmatter rules.

> [!NOTE] Gemini
> Here is an optimized, production-ready `.gemini/GEMINI.md` context file designed to enforce strict link integrity, clean YAML frontmatter, and standard Obsidian markdown conventions.
> 
> Place this file in the root of your vault at `.gemini/GEMINI.md` (or simply `GEMINI.md` at the vault root).
> 
> Markdown
> 
> ````
> # Gemini CLI Context: Obsidian Vault Manager
> 
> You are an expert Personal Knowledge Management (PKM) assistant operating inside an Obsidian markdown knowledge base. Your primary responsibilities are classifying notes, suggesting connections, generating Maps of Content (MOCs), and processing raw inbox material without corrupting note integrity or syntax.
> 
> ---
> 
> ## 1. Non-Negotiable Syntax & Safety Rules
> 
> - **Zero Link Corruption:** Never alter, rename, or drop existing internal wikilinks (`[[Note Name]]`, `[[Note Name|Alias]]`, or `![[Embed]]`).
> - **Standard Wikilink References:** When referencing other notes, always use exact Obsidian wikilink syntax: `[[Note Name]]`. Never use standard web markdown links (e.g., `[Note Name](note-name.md)`) for internal vault notes.
> - **Preserve Math & Technical Blocks:**
>   - Leave all LaTeX blocks (`$...$` inline and `$$...$$` display) completely untouched unless explicitly instructed to edit the math.
>   - Preserve all code blocks (```` ```lang ... ``` ````) and Dataview query blocks (```` ```dataview ... ``` ````).
>   - Preserve all Obsidian callout syntax (`> [!note]`, `> [!tip]`, `> [!warning]`, etc.).
> - **No Conversational Filler:** When executing headless (`-p`) file processing, output only the requested markdown or structured JSON/YAML payload. Do not add introductory remarks ("Here is your note:") or sign-offs.
> 
> ---
> 
> ## 2. YAML Frontmatter Specification
> 
> Every note modified or created must include standard YAML frontmatter bounded by triple-dashes (`---`). 
> 
> ### Schema Requirements:
> ```yaml
> ---
> title: "Exact Note Title"
> date: YYYY-MM-DD
> type: concept | source | moc | daily | project
> tags:
>   - domain/subtopic
> status: seedling | growing | evergreen
> aliases: []
> ---
> ````
> 
> ### Frontmatter Rules:
> 
> -   **Preserve Existing Keys:** Never remove or overwrite custom existing YAML keys (e.g., `id`, `created`, `author`, `source_url`). Only append or update fields explicitly targeted by the prompt.
>     
> -   **Clean Tag Taxonomy:**
>     
>     -   Always use lowercase alphanumeric characters with forward slashes for nested hierarchies (e.g., `math/statistics`, `dev/python`, `finance/volatility`).
>         
>     -   Do not prefix tags with `#` inside the YAML array.
>         
>     -   Restrict tags to concise, existing conceptual domains. Do not invent redundant tags (e.g., choose one of `dev/python`, not `python`, `py`, and `python3`).
>         
> 
> ## 3\. Note Types & Structure Guidelines
> 
> ### Atomic Concept Notes (`type: concept`)
> 
> -   Focus on a single idea per note.
>     
> -   Title must be a concise, declarative statement or concept name (e.g., `GARCH Volatility Modeling` or `Separation of Concerns`).
>     
> -   Structure:
>     
>     1.  YAML Frontmatter.
>         
>     2.  Summary / Core Thesis (1–2 sentences).
>         
>     3.  Context & Elaboration (bullet points or short paragraphs).
>         
>     4.  Related Concepts (bulleted list of contextual `[[wikilinks]]`).
>         
> 
> ### Maps of Content (`type: moc`)
> 
> -   Structure logically into conceptual tiers (e.g., *Core Foundations*, *Methods & Implementations*, *Applied Cases*, *Open Questions*).
>     
> -   Every linked note must include a concise 1-sentence descriptor explaining its role in the cluster:
>     
>     -   `- [[Arch Model Estimation]]: Conditional heteroskedasticity estimation using maximum likelihood.`
>         
> -   Add an `## Identified Gaps` section at the end flagging logical next steps or missing prerequisite notes as stub links (`[[Suggested Note Name]]`).
>     
> 
> ## 4\. Operation Modes
> 
> -   **When analyzing a file (`@file.md`):** Inspect the arguments and metadata first. If suggesting new links, verify relevance based only on explicit content rather than broad thematic guessing.
>     
> -   **When outputting JSON metadata:** Provide strict, parseable JSON with keys matching: `{"title": "...", "tags": [...], "category": "...", "suggested_links": [...]}`.
>     
> -   **When writing inline:** Maintain the author's voice: direct, structured, and clear. Avoid flowery corporate jargon or redundant summaries.
>     
> 
> ```
> ---
> 
> ### Tips for Customizing This File:
> 
> 1. **Tag Allowlist:** If your vault uses a closed set of top-level tags, add an explicit list under Section 2 (e.g., `Allowed parent tags: [math, dev, finance, reading, meta]`) so the CLI never invents new top-level categories.
> 2. **Status Vocab:** Adjust `status: seedling | growing | evergreen` to match your note maturity scale (e.g., `raw | draft | refined`).
> 3. **Folder Scopes:** If you keep literature and daily notes separate, add folder conventions to Section 3 (e.g., *“Daily notes live under `Daily/` and require no aliases”*).
> ```

> [!QUESTION] User
> Write a script to extract frontmatter, titles, and first headings from my Obsidian vault into a clean vault_manifest.tsv for Gemini CLI context.

**Gemini:**

This Python script parses every Markdown file in your Obsidian vault, safely extracts the title, tags, first heading, and a clean text summary, and exports the result into a tab-delimited `vault_manifest.tsv`.

It uses `python-frontmatter` (with a regex fallback if not installed) and skips hidden folders like `.obsidian`, `.git`, and `.trash`.

### Prerequisites

For the most robust YAML parsing, install `python-frontmatter`:

Bash

```
pip install python-frontmatter
```

*(If you run it without installing the package, the built-in fallback parser will still handle standard YAML blocks).*

### Python Manifest Generator (`build_manifest.py`)

Save this file in the root of your Obsidian vault or pass the vault path via `--vault`.

Python

```
#!/usr/bin/env python3
"""
build_manifest.py

Scans an Obsidian vault and extracts note metadata into a compact, tab-delimited
vault_manifest.tsv file optimized for LLM context windows (Gemini CLI).
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

# Optional dependency: python-frontmatter
try:
    import frontmatter
    HAS_FRONTMATTER = True
except ImportError:
    HAS_FRONTMATTER = False

EXCLUDE_DIRS = {".obsidian", ".git", ".trash", ".templates", "templates"}
EXCLUDE_EXTS = {".canvas", ".png", ".jpg", ".jpeg", ".pdf", ".svg", ".zip"}


def clean_text_field(text: str) -> str:
    """Normalize whitespace and strip tabs/newlines to prevent TSV field corruption."""
    if not text:
        return ""
    # Replace internal tabs and newlines with spaces, strip extra whitespace
    cleaned = re.sub(r"[\r\n\t]+", " ", str(text)).strip()
    return re.sub(r"\s{2,}", " ", cleaned)


def fallback_parse(content: str):
    """Fallback YAML frontmatter and body extractor if python-frontmatter isn't installed."""
    metadata = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_yaml = parts[1]
            body = parts[2]
            
            # Simple line-by-line key-value parse for common fields
            title_match = re.search(r"^title:\s*[\"']?(.*?)[\"']?$", raw_yaml, re.MULTILINE)
            if title_match:
                metadata["title"] = title_match.group(1).strip()

            tags_match = re.search(r"^tags:\s*\[(.*?)\]", raw_yaml, re.MULTILINE)
            if tags_match:
                metadata["tags"] = [t.strip().strip("'\"") for t in tags_match.group(1).split(",") if t.strip()]
            else:
                # Check for list-style tags
                list_tags = re.findall(r"^\s*-\s+([a-zA-Z0-9_\-\/]+)", raw_yaml, re.MULTILINE)
                if list_tags:
                    metadata["tags"] = list_tags

            type_match = re.search(r"^type:\s*[\"']?(.*?)[\"']?$", raw_yaml, re.MULTILINE)
            if type_match:
                metadata["type"] = type_match.group(1).strip()

    return metadata, body


def extract_first_heading_and_summary(body: str, max_summary_chars: int = 220):
    """Extracts the first markdown heading (#+) and a short, plain-text summary."""
    lines = body.splitlines()
    first_heading = ""
    summary_chunks = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Detect the first heading if not found yet
        if not first_heading and re.match(r"^#{1,6}\s+", stripped):
            first_heading = re.sub(r"^#{1,6}\s+", "", stripped)
            continue

        # Skip callouts, code fences, dataview blocks, and horizontal rules
        if stripped.startswith("> [!") or stripped.startswith("```") or stripped == "---":
            continue

        # Accumulate plain content for the summary
        clean_line = re.sub(r"\[\[(.*?)\]\]", r"\1", stripped)       # [[Link|Alias]] -> Link|Alias
        clean_line = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", clean_line) # [text](url) -> text
        clean_line = re.sub(r"[*_`]", "", clean_line)                # Strip markdown bold/code markers

        summary_chunks.append(clean_line)
        if sum(len(c) for c in summary_chunks) >= max_summary_chars:
            break

    summary = " ".join(summary_chunks)
    if len(summary) > max_summary_chars:
        summary = summary[:max_summary_chars].rsplit(" ", 1)[0] + "..."

    return first_heading, summary


def process_note(file_path: Path, vault_root: Path):
    """Reads a single markdown note and returns a dictionary of extracted fields."""
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return None

    if HAS_FRONTMATTER:
        try:
            post = frontmatter.loads(content)
            metadata = post.metadata
            body = post.content
        except Exception:
            metadata, body = fallback_parse(content)
    else:
        metadata, body = fallback_parse(content)

    rel_path = file_path.relative_to(vault_root).as_posix()
    note_name = file_path.stem

    # Determine Title (frontmatter title > note filename)
    title = metadata.get("title") or note_name

    # Determine Tags
    raw_tags = metadata.get("tags", [])
    if isinstance(raw_tags, str):
        tags_list = [t.strip().lstrip("#") for t in raw_tags.split(",") if t.strip()]
    elif isinstance(raw_tags, list):
        tags_list = [str(t).strip().lstrip("#") for t in raw_tags if t]
    else:
        tags_list = []
    
    # Also capture inline #tags if frontmatter tags are empty
    if not tags_list:
        inline_tags = re.findall(r"(?:^|\s)#([a-zA-Z0-9_\-\/]+)", body)
        tags_list = list(dict.fromkeys(inline_tags))[:5] # Deduplicate and keep top 5

    tags_str = ",".join(tags_list)
    note_type = metadata.get("type", "")

    first_heading, summary = extract_first_heading_and_summary(body)

    return {
        "filepath": clean_text_field(rel_path),
        "title": clean_text_field(title),
        "type": clean_text_field(note_type),
        "tags": clean_text_field(tags_str),
        "first_heading": clean_text_field(first_heading),
        "summary": clean_text_field(summary),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate vault_manifest.tsv for Gemini CLI.")
    parser.add_argument("--vault", type=str, default=".", help="Path to your Obsidian vault root (default: current dir).")
    parser.add_argument("--output", type=str, default="vault_manifest.tsv", help="Output file path (default: vault_manifest.tsv).")
    args = parser.parse_args()

    vault_root = Path(args.vault).resolve()
    output_path = Path(args.output).resolve()

    if not vault_root.is_dir():
        print(f"Error: Vault path '{vault_root}' does not exist or is not a directory.", file=sys.stderr)
        sys.exit(1)

    columns = ["filepath", "title", "type", "tags", "first_heading", "summary"]
    records = []

    print(f"Scanning markdown files in: {vault_root}")

    for root, dirs, files in os.walk(vault_root):
        # Exclude internal/hidden directories in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]

        for file in files:
            if not file.endswith(".md"):
                continue
            
            full_path = Path(root) / file
            record = process_note(full_path, vault_root)
            if record:
                records.append(record)

    # Sort alphabetically by relative filepath for clean ordering
    records.sort(key=lambda x: x["filepath"])

    # Write out TSV
    with open(output_path, mode="w", encoding="utf-8", newline="") as tsv_file:
        writer = csv.DictWriter(tsv_file, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    total_notes = len(records)
    file_size_kb = output_path.stat().st_size / 1024
    print(f"Done. Processed {total_notes} notes.")
    print(f"Manifest written to: {output_path} ({file_size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
```

### How to Run It

1.  Make the script executable:
    
    Bash
    
    ```
    chmod +x build_manifest.py
    ```
    
2.  Run it against your vault:
    
    Bash
    
    ```
    ./build_manifest.py --vault . --output vault_manifest.tsv
    ```
    

### What the Resulting `vault_manifest.tsv` Looks Like

| filepath | title | type | tags | first_heading | summary |
| --- | --- | --- | --- | --- | --- |
| Concepts/GARCH Models.md | GARCH Volatility Modeling | concept | finance/risk,math/stats | Generalized Autoregressive Conditional Heteroskedasticity | GARCH models estimate time-varying conditional variance in financial asset returns using lagged residuals... |
| Daily/2026-09-15.md | 2026-09-15 | daily | log | Standup Notes | Built FastAPI volatility endpoint; debugged student-t distribution convergence in arch package... |

### Using the Manifest with Gemini CLI

With 1,700 notes, this file typically weighs around **180–300 KB** (approx. 50,000 to 75,000 tokens), fitting comfortably inside Gemini's context window.

#### 1\. Cluster Recall & MOC Brainstorming

Bash

```
gemini -p "Read @vault_manifest.tsv. Identify all notes relating to time series volatility, GARCH, and risk estimation. Return an outline for a new Map of Content (MOC) with [[wikilinks]]."
```

#### 2\. Finding Forgotten or Unlinked Notes

Bash

```
gemini -p "Using @vault_manifest.tsv, find notes that have empty tags or are marked 'seedling' under type 'concept'. Group them by primary domain so I can triage them."
```

#### 3\. Automatic Shell Refresh via Git Hook or Task Runner

You can add a simple alias or pre-commit hook to update the manifest whenever your vault changes:

Bash

```
# Add to ~/.zshrc or ~/.bashrc
alias update-manifest="python3 ~/path/to/build_manifest.py --vault ~/Documents/ObsidianVault"
```