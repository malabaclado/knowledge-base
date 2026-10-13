"""
Generate Maps of Content (MOCs) Script
======================================
Purpose:
    Rebuilds or regenerates clean, minimalist, list-based Maps of Content (MOCs)
    inside the `mocs/` directory.

Design Principles:
    - Zero verbose filler or text clutter: outputs clean bulleted lists of `[[Wikilinks]]`.
    - Automatically traverses topic directories (`mathematics/`, `business-advisory/`,
      `trading-finance/`, etc.) to index newly created or moved notes.
    - Preserves core curated launchpads (`000 Overview MOC`, `002 Data Science & ML MOC`,
      `008 Python & Backend Engineering MOC`, `009 Quantitative Finance & Risk MOC`).
    - Standardizes YAML frontmatter across all MOC notes with titles, aliases, and tags.

Usage:
    Run from the vault root (or content/_drafts directory):
        python _scripts/generate_mocs.py
"""

import os

MOCS_DIR = "mocs"

# Curated core domain MOCs
CORE_MOCS = {
    "000 Overview MOC.md": """---
title: "000 Overview MOC"
aliases:
  - "Overview MOC"
tags:
  - moc
  - index
---

# Knowledge Base Overview MOC

## Domains
- [[002 Data Science & ML MOC]]
- [[008 Python & Backend Engineering MOC]]
- [[009 Quantitative Finance & Risk MOC]]

## Vault & Tools
- [[Setting up Logseq-like Journal in Obsidian]]
- [[how i set up my knowledge base in obsidian]]
- [[quartz_docs/index|Quartz Documentation]]

## Restored Archive Domains
- [[004 Mathematics & Numerical Methods MOC]]
- [[013 Undergraduate Thesis & ML Research MOC]]
- [[012 Technical Analysis & Trading MOC]]
- [[011 SQL & Database Querying MOC]]
- [[010 R Programming MOC]]
- [[007 Psychology & Attachment Theory MOC]]
- [[006 Productivity & PKM MOC]]
- [[003 Insurance Advisory & Business MOC]]
- [[005 Personal Life & Hobbies MOC]]
- [[001 Archive Uncategorized MOC]]
""",

    "002 Data Science & ML MOC.md": """---
title: "002 Data Science & ML MOC"
aliases:
  - "Data Science & ML MOC"
tags:
  - moc
---

# Data Science & ML MOC

## Algorithms & Concepts
- [[Linear Regression]]
- [[Gradient Descent]]
- [[Customer Segmentation]]

## Tools & Libraries
- [[scikit-learn]]
- [[Intro to Data Visualization with Matplotlib]]
- [[Python libraries for data science]]

## Books & References
- [[Hands-on Data Analysis with Pandas]]
- [[Practical Statistics for Data Scientists]]

## Courses & Projects
- [[data science tutorial course on freeCodeCamp]]
- [[datacamp projects]]
- [[understanding subscription behaviors]]

## Related MOCs
- [[008 Python & Backend Engineering MOC]]
- [[009 Quantitative Finance & Risk MOC]]
- [[000 Overview MOC]]
""",

    "008 Python & Backend Engineering MOC.md": """---
title: "008 Python & Backend Engineering MOC"
aliases:
  - "Python & Backend Engineering MOC"
tags:
  - moc
---

# Python & Backend Engineering MOC

## Python Fundamentals
- [[Python Code Conventions]]
- [[String Functions]]
- [[books/Learning Python, 6th Ed.|Learning Python, 6th Ed.]]
- [[venv]]

## APIs & Frameworks
- [[FastAPI Crash Course]]
- [[Pydantic]]
- [[how-to-add-drop-down-parameters-in-swagger-in-fast-74a32d07|FastAPI Swagger Dropdown Parameters]]

## Projects & Systems
- [[Project - Real-Time Inventory Reservation Service]]
- [[volatility and value at risk forecasting API with Python]]
- [[How I'd Learn to be a Data Engineer]]

## Infrastructure & AI Tools
- [[Setting up my local AI Workspace]]
- [[i-ve-completed-datacamp-s-containerization-and-vir-fb9780c4|Containerization & Virtualization]]
- [[snowpro-core-certification-competencies-explained-17160812|Snowflake SnowPro Core Architecture]]
- [[github resources]]

## Related MOCs
- [[002 Data Science & ML MOC]]
- [[009 Quantitative Finance & Risk MOC]]
- [[000 Overview MOC]]
""",

    "009 Quantitative Finance & Risk MOC.md": """---
title: "009 Quantitative Finance & Risk MOC"
aliases:
  - "Quantitative Finance & Risk MOC"
tags:
  - moc
---

# Quantitative Finance & Risk MOC

## Risk Metrics
- [[Value-at-Risk]]
- [[Expected Shortfall]]
- [[Does it make sense to calculate both parametric and historical var|Parametric vs. Historical VaR]]

## Time Series & Econometrics
- [[Notes on Time Series Analysis]]
- [[Applied Time Series Analysis - PSU Stat510]]
- [[arch]]
- [[books/Analysis of Financial Time Series|Analysis of Financial Time Series (Ruey S. Tsay)]]

## Forecasting APIs & Implementation
- [[volatility and value at risk forecasting API with Python]]
- [[Is there an end-user workflow that uses both volatility and VaR. My API only calculates one stock at a time.|End-User Workflow: Volatility & VaR]]
- [[Would a 1-year or 252-day EOD data enough training sample for this usecase|Sample Size Calibration (252-Day EOD)]]
- [[i-have-a-garch-1-1-model-using-python-s-arch-libra-97aefc13|GARCH(1,1) Python Arch Calibration]]

## Financial Planning
- [[How can I achieve FIRE (Financial Independent, Retire Early) by 40|FIRE Strategy by 40]]

## Related MOCs
- [[008 Python & Backend Engineering MOC]]
- [[002 Data Science & ML MOC]]
- [[000 Overview MOC]]
"""
}

# Dynamic directory-backed MOCs
FOLDER_MOCS = {
    "001 Archive Uncategorized MOC.md": ("Archive Uncategorized MOC", "archive-misc"),
    "003 Insurance Advisory & Business MOC.md": ("Insurance Advisory & Business MOC", "business-advisory"),
    "004 Mathematics & Numerical Methods MOC.md": ("Mathematics & Numerical Methods MOC", "mathematics"),
    "005 Personal Life & Hobbies MOC.md": ("Personal Life & Hobbies MOC", "personal"),
    "006 Productivity & PKM MOC.md": ("Productivity & PKM MOC", "productivity"),
    "007 Psychology & Attachment Theory MOC.md": ("Psychology & Attachment Theory MOC", "psychology"),
    "010 R Programming MOC.md": ("R Programming MOC", "r-programming"),
    "011 SQL & Database Querying MOC.md": ("SQL & Database Querying MOC", "sql-databases"),
    "012 Technical Analysis & Trading MOC.md": ("Technical Analysis & Trading MOC", "trading-finance"),
    "013 Undergraduate Thesis & ML Research MOC.md": ("Undergraduate Thesis & ML Research MOC", "thesis-research"),
}


def main():
    os.makedirs(MOCS_DIR, exist_ok=True)
    all_mocs = dict(CORE_MOCS)

    # Build dynamic topic MOCs by scanning directories
    for filename, (title, folder) in FOLDER_MOCS.items():
        clean_name = filename[:-3]
        files = sorted(os.listdir(folder)) if os.path.exists(folder) else []
        links = []
        for f in files:
            if f.startswith('.'):
                continue
            name_no_ext, ext = os.path.splitext(f)
            if ext == ".md":
                links.append(f"- [[{name_no_ext}]]")
            else:
                links.append(f"- [[{f}]]")

        notes_list = "\n".join(links)
        content = f"""---
title: "{clean_name}"
aliases:
  - "{title}"
tags:
  - moc
---

# {title}

## Notes
{notes_list}
"""
        all_mocs[filename] = content

    # Write out each MOC file
    for filename, content in all_mocs.items():
        out_path = os.path.join(MOCS_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Successfully generated {len(all_mocs)} MOCs in '{MOCS_DIR}/'.")


if __name__ == "__main__":
    main()
