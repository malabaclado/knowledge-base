---
title: "Knowledge Base Reorganization & Automation Plan"
date: "2026-10-04"
author: "Gemini CLI"
tags:
  - architecture
  - pkm
  - obsidian
  - automation
  - quartz
description: "Comprehensive blueprint for vault reorganization, fast recall optimization, strict human-AI note separation, graph connectivity, and maintenance automation."
---

# Knowledge Base Reorganization & Automation Plan

> [!ABSTRACT] Executive Summary
> This blueprint establishes a scalable architecture for your Obsidian vault and Quartz digital garden. It directly addresses the friction of slow recall, search pollution from historical archives, and the manual overhead of second-brain maintenance. The plan enforces three core principles:
> 1. **Sub-second recall and lookup** via frontmatter aliases and search scoping.
> 2. **A strict architectural divide** between human knowledge synthesis and machine-generated AI exports.
> 3. **High graph connectivity** through systematic linking conventions and automated orphan detection.

---

## 1. Vault State Assessment & Friction Points

An exhaustive analysis of your workspace (`content/_drafts`) reveals ~1,500+ files distributed across three tiers:
- **Active Working Core:** High-value notes in root (`FastAPI Crash Course`, `Gradient Descent`, `Customer Segmentation`), structured book analyses (`books/`), and recent daily logs (`periodic notes/daily/`).
- **Domain MOCs:** 14 newly structured, minimal Maps of Content (`000 Overview MOC` through `013 Undergraduate Thesis & ML Research MOC`) providing clean top-down entry points.
- **Unprocessed Staging & Inbox:** High-value deep dives (`Value-at-Risk.md`, `Pydantic.md`, `Notes on Time Series Analysis.md`) mixed with 0-byte scratchpads and `.base` database files in `inbox/`.
- **Nested Legacy Archives (`_archive/`):** 24 nested folders containing ~1,270 legacy notes, university coursework (`Courses/`, `Differential Equations/`), thesis drafts (`Thesis/`, `Research Notes/`), SQL tracks (`Udacity-SQL-Notes/`), web clippings (`ReadItLater Inbox/`, `Omnivore/`, `Hypothesis Highlights/`), and historical journals (`Journal/`).
- **AI Transcripts:** Chronologically partitioned chat dumps in `ai-generated-notes/gemini/YYYY-MM-DD/`.

### Key Friction Points
1. **Search Dilution:** Global searches (`Ctrl+Shift+F`) query across hundreds of uncurated web clippings and old university assignments, obscuring active professional notes.
2. **Recall Blind Spots:** Core notes lack `aliases`, preventing Obsidian's Quick Switcher (`Ctrl+O`) from matching acronyms, alternate spellings, or abbreviations.
3. **AI Siloing vs. AI Contamination:** AI exports are either disconnected in date folders where they cannot be found, or risk polluting human notes if pasted directly without attribution.
4. **Manual Maintenance Fatigue:** Manually updating MOCs, cleaning empty daily notes, and checking for broken links requires too much cognitive overhead.

---

## 2. Foundational Architecture: The 3 Core Mandates

```
                          ┌────────────────────────────────┐
                          │   Vault Structural Hierarchy   │
                          └───────────────┬────────────────┘
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                ▼                                ▼
┌──────────────────┐             ┌──────────────────┐             ┌──────────────────┐
│   000-013 MOCs   │             │   Human Domain   │             │   AI Generated   │
│   (Top Indexes)  │             │    Knowledge     │             │    Transcripts   │
│  Minimal Lists   │             │ (Curated Notes)  │             │ (Isolated Dumps) │
└────────┬─────────┘             └────────┬─────────┘             └────────┬─────────┘
         │                                │                                │
         │                                ▼                                │
         │                     [[Human Concept Note]]                      │
         │                                │                                │
         └───────────────────────────────►├◄───────────────────────────────┘
                                  (Transclusion & Citations)
```

### Pillar 1: Sub-Second Recall & Fast Lookup
To locate any concept within 3 seconds, retrieval must not depend on remembering the exact folder path or original file name.

1. **Frontmatter Aliasing Standard:**
   Every core concept note must include an `aliases` array in its YAML frontmatter covering acronyms, full names, and colloquial terms:
   ```yaml
   ---
   title: "Value-at-Risk"
   aliases:
     - "VaR"
     - "Value at Risk"
     - "Parametric VaR"
   tags:
     - finance/risk
     - quantitative-finance
   ---
   ```
2. **Search Scoping (Excluding Cold Storage):**
   Configure Obsidian to exclude raw archive and media directories from global search:
   - Navigate to **Settings → Files and links → Excluded files**.
   - Add: `_archive/`, `_attachments/`, `ReadItLater Inbox/`, `Omnivore/`.
   - *Result:* `Ctrl+O` and `Ctrl+Shift+F` instantly return only active, curated knowledge.
3. **Standardized Tag Hierarchy:**
   Use nested tags to enable faceted filtering in Obsidian's tag pane and Dataview:
   - `domain/topic`: `#finance/risk`, `#finance/time-series`, `#ml/nlp`, `#ml/optimization`, `#backend/fastapi`.
   - `status`: `#status/seed`, `#status/growing`, `#status/evergreen`.

---

### Pillar 2: Strict Human-AI Separation

To maintain the epistemic integrity of your second brain, **raw AI output must never be masqueraded as verified personal knowledge**, yet valuable machine insights must remain readily retrievable.

1. **Physical Namespace Boundary:**
   - **Human Knowledge Space:** `mocs/`, `books/`, `mathematics/`, `trading-finance/`, `sql-databases/`, `periodic notes/`.
   - **Machine Knowledge Space:** strictly confined to `ai-generated-notes/` (sub-partitioned by provider/agent: `gemini/`, `gemini_cli/`, `claude/`, `notebooklm/`).
2. **Frontmatter AI Metadata Schema:**
   All files inside `ai-generated-notes/` must contain provenance metadata:
   ```yaml
   ---
   title: "Conversation Title"
   source: "gemini" # or gemini_cli, notebooklm, chatgpt
   created: "YYYY-MM-DDTHH:mm:ss"
   type: "ai-transcript"
   tags:
     - ai-generated
     - domain/topic
   verified: false
   ---
   ```
3. **Visual Callout Banners:**
   AI-generated summaries must feature an explicit warning banner at the top of the body:
   ```markdown
   > [!AI-TRANSCRIPT] Automated Machine Output
   > Source: Gemini CLI | Date: 2026-10-04
   > Status: Raw / Unverified human synthesis.
   ```
4. **The "Distillation & Reference" Linking Pattern:**
   - **Never** paste AI explanations directly into human concept notes without review.
   - **Instead**, human concept notes cite or transclude specific sections of AI transcripts:
     ```markdown
     ## Model Diagnostics
     For the calibration benchmarks of GARCH(1,1), see:
     - Analysis: [[i-have-a-garch-1-1-model-using-python-s-arch-libra-97aefc13#Summary Diagnostics]]
     - Transcluded Architecture:
       ![[snowpro-core-certification-competencies-explained-17160812#Core Architecture]]
     ```
   - This keeps your primary notes concise and 100% human-verified while maintaining instant 1-click access to deep AI research sessions.

---

### Pillar 3: High Graph Connectivity (No Orphaned Notes)

A note without links is dead knowledge. Every note in the vault must be reachable from `000 Overview MOC` within **3 clicks maximum**.

1. **The "Rule of Two Links":**
   Every note created or graduated into the vault must contain at minimum:
   - **One Upward Link (Parent):** Pointing to its domain MOC or topic index.
   - **One Lateral Link (Sibling/Related):** Pointing to a related concept, project, or book note.
2. **Standardized Navigation Header/Footer:**
   Add a uniform navigation footer to notes:
   ```markdown
   ---
   ## References & Navigation
   - **Up:** [[008 Python & Backend Engineering MOC]]
   - **Related:** [[FastAPI Crash Course]], [[Pydantic]]
   ```
3. **Daily Note Integration:**
   Daily logs in `periodic notes/daily/` act as chronological discovery hubs. Whenever you work on or study a concept, wikilink it directly in that day's log:
   ```markdown
   - Investigated [[Value-at-Risk]] calculation methods.
   - Configured [[FastAPI Crash Course]] dependency injection.
   ```

---

## 3. Reorganization Plan for Nested Folders & Inbox

### Phase 1: Resolving the 24 Nested Folders in `/_archive/`

| Folder in `/_archive/` | Nature of Content | Strategic Destination | Action Plan |
|---|---|---|---|
| `Courses/` & `Differential Equations/` | University Math/Stats/CS notes | Merge into `mathematics/` & `personal/` | Move academic notes into `mathematics/` (pure math) or `personal/` (GE subjects like PI 100). |
| `Thesis/` & `Research Notes/` | ML research papers, PRML, Bishop notes | Merge into `thesis-research/` | Keep high-value literature reviews and algorithms in `thesis-research/`. |
| `Udacity-SQL-Notes/` | Structured SQL lessons 1–7 | `sql-databases/udacity/` | Move intact as a dedicated subfolder within `sql-databases/`. |
| `Datacamp/` & `Kaggle/` | Python, Pandas, visualization exercises | Merge into `data-science/` & `sql-databases/` | Consolidate course notes into active learning tracks. |
| `Project SPARTA/` | Analytics & data governance modules | `data-science/sparta/` | Move intact to preserve certification coursework. |
| `Seedbox/` (~300 notes) | Legacy vault dump from earlier system | Triage & Merge | Run keyword classification script to route notes to active topic folders; discard empty shells. |
| `ReadItLater Inbox/`, `Omnivore/`, `Hypothesis Highlights/` | Clipped web articles & image assets | `_archive/web-clippings/` | Move all web-capture subfolders into a single `web-clippings/` folder and exclude from search. |
| `Journal/` (2023 logs) | Historical daily/weekly logs | `periodic notes/archive/2023/` | Relocate to chronological periodic note archives. |
| `Templates/` | Outdated Obsidian templates | Merge into `_templates/` | Keep useful templates, remove duplicates. |

### Phase 2: Inbox Triage & Graduation
1. **Graduate Permanent Knowledge:**
   - Move `Value-at-Risk.md`, `Expected Shortfall.md`, `Notes on Time Series Analysis.md`, and `volatility and value at risk forecasting API with Python.md` to `trading-finance/`.
   - Move `Pydantic.md` and `venv.md` to `backend/` or workspace root.
   - Move `scikit-learn.md` and `Intro to Data Visualization with Matplotlib.md` to `data-science/`.
2. **Purge Ephemeral Clutter:**
   - Delete 0-byte dated scratchpads (`2026-07-10.md`, `2026-08-04.md`, `Untitled.base`).

---

## 4. Automation Blueprint: Minimizing Manual Maintenance

To keep the second brain effortless to maintain, routine operational tasks must be automated via scripts and Obsidian plugins.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AUTOMATION ECOSYSTEM                            │
└────────────────────────────────────────────────────────────────────────┘

  [ Web / AI Capture ]           [ Obsidian Vault ]            [ Maintenance ]
  ───────────────────           ──────────────────            ───────────────
  Chrome AI Exporter ──► HTTPS ──► Local REST API              _scripts/
                                       │                       ├── generate_mocs.py
  Readwise / Omnivore ──► Sync ────────┤                       ├── vault_linter.py
                                       ▼                       └── backup_vault.ps1
                                  Inbox Staging
                                       │
                                (Daily Triage)
                                       │
                                       ▼
                              Permanent Domains & MOCs
```

### Automation Workflow 1: Headless AI Chat Sync & Frontmatter Stamping
- **Tooling:** Obsidian Local REST API + Obsidian AI Exporter Chrome Extension.
- **Workflow:** When conversing with Gemini/ChatGPT/NotebookLM, clicking the exporter sends the chat directly via HTTPS REST API into `ai-generated-notes/gemini/YYYY-MM-DD/`.
- **Enhancement:** Configure the extension to automatically inject:
  - `type: ai-transcript`
  - `tags: [ai-note, gemini]`
  - Standardized callout banner `> [!AI-TRANSCRIPT]`.

---

### Automation Workflow 2: Automatic MOC Maintenance
Never manually type note links into MOCs. Maintain dynamic and static generation:

1. **Option A: Dynamic Obsidian Views (Dataview)**
   Inside any MOC or dashboard, embed dynamic queries that auto-populate as you create notes:
   ````markdown
   ```dataview
   TABLE date as "Created", tags as "Tags"
   FROM "trading-finance"
   WHERE !contains(file.tags, "moc")
   SORT file.name ASC
   ```
   ````
2. **Option B: Static Markdown Generation (Quartz Compatible)**
   Quartz does not execute runtime Dataview queries. Use our automated Python script `_scripts/generate_mocs.py` before building or syncing:
   - Scans every domain folder (`mathematics/`, `trading-finance/`, etc.).
   - Builds alphabetical `[[Wikilinks]]` lists.
   - Updates `000 Overview MOC.md` automatically.

---

### Automation Workflow 3: Automated Vault Health Linter (`_scripts/vault_linter.py`)
A single Python script that can be run on-demand or as a pre-commit hook to maintain vault hygiene:
- **Orphan Detection:** Lists all notes that have zero incoming and zero outgoing links.
- **Zero-Byte Pruning:** Automatically detects and removes empty 0-byte `.md` files in `inbox/` and `periodic notes/daily/`.
- **Broken Link Detection:** Identifies `[[Wikilinks]]` that point to non-existent notes.
- **Frontmatter Verification:** Flags notes missing `title`, `date`, or `aliases`.

---

### Automation Workflow 4: Automated Vault Backup
A lightweight PowerShell script scheduled via Windows Task Scheduler (or run manually) to commit and backup the vault safely:
```powershell
# _scripts/backup_vault.ps1
$date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git add .
git commit -m "Vault backup: $date"
Write-Host "Vault backed up successfully at $date"
```

---

## 5. Step-by-Step Implementation Roadmap

```
Phase 1: Quick Wins (Immediate)
├── Add search exclusions for _archive/ in Obsidian settings.
├── Add aliases to top 15 most-used active notes.
└── Clean 0-byte placeholder files from inbox/.

Phase 2: Archive & Inbox Reorganization
├── Run recursive sweep on nested _archive/ subfolders (grouping into topic folders).
├── Move web-clipping folders (Omnivore, ReadItLater) into a cold storage folder.
└── Graduate valuable inbox notes (VaR, Pydantic, Time Series) into topic folders.

Phase 3: Automation Setup
├── Deploy _scripts/vault_linter.py for automated orphan and hygiene checks.
├── Add Dataview auto-listing blocks to daily note templates.
└── Configure Templater hotkeys for instant new note generation with frontmatter.

Phase 4: Ongoing Cadence (5 Mins / Week)
├── Daily: Capture quick thoughts in periodic daily notes; export AI chats via extension.
└── Weekly: Run generate_mocs.py and vault_linter.py to reconcile new notes into MOCs.
```

---

## 6. Recommended Standard Note Templates

### Concept / Permanent Note Template
```markdown
---
title: "{{title}}"
aliases:
  - "{{alias1}}"
  - "{{alias2}}"
date: "{{date}}"
tags:
  - domain/topic
  - status/growing
---

# {{title}}

> [!SUMMARY] Core Definition
> One or two concise sentences defining the concept.

## Key Principles & Mechanics
- 

## Code / Practical Implementation
```python

```

## References & Navigation
- **Up:** [[000 Overview MOC]]
- **Related:** [[Related Note]]
- **AI Deep Dive:** [[AI Transcript Reference]]
```

### AI Transcript Template
```markdown
---
title: "{{title}}"
source: gemini # or gemini_cli, notebooklm
date: "{{date}}"
type: ai-transcript
tags:
  - ai-generated
  - domain/topic
verified: false
---

> [!AI-TRANSCRIPT] Automated Machine Output
> Generated via Gemini CLI on {{date}}. Unverified personal synthesis.

# {{title}}

## Transcript Body
...
```
