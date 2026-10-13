# Project Context: Knowledge Base Vault & Quartz Drafts

This workspace (`content/_drafts`) is MY personal knowledge management (PKM) vault and staging ground for notes, technical documentation, study materials, and AI-assisted research. It is authored primarily via **Obsidian** and managed within a **Quartz 4** digital garden repository.

---

## Workspace & Directory Structure

- **Root (`_drafts/`)**: Active drafts, tutorials, and technical reference notes across Data Science, Data Engineering, Python, Machine Learning, and API architecture.
- **`ai-generated-notes/`**: AI conversation transcripts and structured summaries exported into date-partitioned folders (e.g., `gemini/YYYY-MM-DD/`).
- **`books/`**: Structured reading notes, book summaries, and concept breakdowns (e.g., *Learning Python*, *Practical Statistics for Data Scientists*, *Analysis of Financial Time Series*), frequently linked with NotebookLM research notebooks.
- **`inbox/`**: Fleeting notes, quick captures, idea prompts, and `.base` files (Obsidian Bases / tabular view definitions).
- **`mocs/`**: Maps of Content (MOCs) serving as high-level topic indexes and entry points for interconnected notes.
- **`periodic notes/daily/`**: Daily journal entries organized chronologically using the naming pattern `MMM DD, YYYY.md` (e.g., `Oct 01, 2026.md`).
- **`_archive/`**: Archived notes, academic coursework (mathematics, statistics, university thesis drafts), and inactive projects.
- **`_attachments/`**: Images, diagrams, and media embedded across notes.
- **`_templates/`**: Obsidian note templates and reusable callout snippets (e.g., `info-callout.md`).
- **`quartz_docs/`**: Quartz 4 reference documentation covering build commands, configuration, layout components, and deployment.

---

## Authoring & Formatting Standards

### 1. Markdown Flavor & Syntax
- **Obsidian Flavored Markdown**:
  - **Internal Links (Wikilinks)**: Use `[[Target Note Name]]` or `[[Target Note Name|Display Text]]`.
  - **Callouts**: Use standard Obsidian callout syntax:
    ```markdown
    > [!NOTE]
    > [!QUESTION]
    > [!TIP]
    > [!INFO]
    ```
  - **Math & LaTeX**: Inline formulas use `$ ... $` and block equations use `$$ ... $$`.
  - **Images & Embeds**: Format embedded media as `![caption](url)` or `![[attachment-name.png]]`.

### 2. Frontmatter Standards (YAML)
Notes intended for publication or structured indexing must include YAML frontmatter at the top:

```yaml
---
title: "Descriptive Note Title"
date: "YYYY-MM-DD"
tags:
  - topic-name
  - note-type
draft: true
description: "Brief summary for Quartz previews and search indexing."
---
```

**Common Tag Taxonomies**:
- `ai-conversation`, `ai-note`, `gemini`: For machine-assisted sessions or exported chats.
- `video-note`, `youtube`: For notes derived from lectures, talks, and video courses.
- `data-science`, `machine-learning`, `python`, `api`: Topic-specific domain tags.

### 3. AI Note Exports Schema (`ai-generated-notes/gemini/`)
Exports generated via Obsidian AI Exporter follow this frontmatter structure:
```yaml
---
id: gemini_<id>
title: Note Title
source: gemini
url: "https://gemini.google.com/app/<id>"
created: "YYYY-MM-DDTHH:mm:ss+08:00"
modified: "YYYY-MM-DDTHH:mm:ss+08:00"
tags:
  - ai-conversation
  - gemini
message_count: 2
---
```

---

## Tech Stack & Tooling Context

- **Editor**: Obsidian (integrated with `periodic-notes`, `outliner`, `obsidian-local-rest-api`).
- **Publishing Platform**: Quartz 4 (Static site generator for digital gardens).
  - Sync command (from repository root): `npx quartz sync`
  - Local preview: `npx quartz build --serve`
- **Domain Tools**: Python virtual environments (`.venv`), FastAPI, Pydantic, Scikit-learn, NotebookLM, Docker/Ollama/OpenVINO for local LLMs.

---

## Operational Guidelines for AI Assistants

1. **Surgical Note Edits**: Preserve existing wikilinks, tags, callouts, and frontmatter metadata when updating or refactoring notes.
2. **Knowledge Graph Integrity**: When creating new notes, link them back to relevant topic MOCs (`mocs/`) or related notes using `[[Wikilinks]]`.
3. **Daily Notes**: Follow the `MMM DD, YYYY.md` date format in `periodic notes/daily/` when capturing daily logs.
4. **Git Mandates**: The vault is version-controlled under git (`v4` branch). Do not stage or commit files unless explicitly directed by the user.
