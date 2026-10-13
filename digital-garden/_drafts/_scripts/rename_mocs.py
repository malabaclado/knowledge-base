"""
Rename Maps of Content (MOCs) Script
====================================
Purpose:
    Applies a standardized 3-digit numerical prefix (`000` to `013`) to all
    MOC files in the `mocs/` directory.

Key Behaviors:
    1. Pins the master index to the top as `000 Overview MOC.md`.
    2. Sorts domain MOCs alphabetically with prefixes `001` through `013`.
    3. Injects backwards-compatible YAML frontmatter:
           aliases:
             - "<Original MOC Title>"
       This ensures Obsidian's Quick Switcher (`Ctrl+O`) and existing `[[Wikilinks]]`
       continue to resolve smoothly without broken links.
    4. Automatically updates internal wikilinks between MOC files (e.g., inside
       `000 Overview MOC.md`).

Usage:
    Run from the vault root (or content/_drafts directory):
        python _scripts/rename_mocs.py
"""

import os
import re

MOCS_DIR = "mocs"

RENAME_MAP = {
    "Overview MOC.md": "000 Overview MOC.md",
    "Archive Uncategorized MOC.md": "001 Archive Uncategorized MOC.md",
    "Data Science & ML MOC.md": "002 Data Science & ML MOC.md",
    "Insurance Advisory & Business MOC.md": "003 Insurance Advisory & Business MOC.md",
    "Mathematics & Numerical Methods MOC.md": "004 Mathematics & Numerical Methods MOC.md",
    "Personal Life & Hobbies MOC.md": "005 Personal Life & Hobbies MOC.md",
    "Productivity & PKM MOC.md": "006 Productivity & PKM MOC.md",
    "Psychology & Attachment Theory MOC.md": "007 Psychology & Attachment Theory MOC.md",
    "Python & Backend Engineering MOC.md": "008 Python & Backend Engineering MOC.md",
    "Quantitative Finance & Risk MOC.md": "009 Quantitative Finance & Risk MOC.md",
    "R Programming MOC.md": "010 R Programming MOC.md",
    "SQL & Database Querying MOC.md": "011 SQL & Database Querying MOC.md",
    "Technical Analysis & Trading MOC.md": "012 Technical Analysis & Trading MOC.md",
    "Undergraduate Thesis & ML Research MOC.md": "013 Undergraduate Thesis & ML Research MOC.md",
}


def main():
    if not os.path.exists(MOCS_DIR):
        print(f"Directory '{MOCS_DIR}' does not exist.")
        return

    link_replacements = {old_f[:-3]: new_f[:-3] for old_f, new_f in RENAME_MAP.items()}

    for old_file, new_file in RENAME_MAP.items():
        old_path = os.path.join(MOCS_DIR, old_file)
        new_path = os.path.join(MOCS_DIR, new_file)

        # Source may already be renamed or at old path
        source_path = old_path if os.path.exists(old_path) else new_path
        if not os.path.exists(source_path):
            continue

        with open(source_path, "r", encoding="utf-8") as f:
            content = f.read()

        old_name = old_file[:-3]
        new_name = new_file[:-3]

        # Update Frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                body = parts[2]

                # Update title to prefixed name
                if "title:" in fm:
                    fm = re.sub(r'title:\s*".*?"', f'title: "{new_name}"', fm)
                    fm = re.sub(r"title:\s*'.*?'", f'title: "{new_name}"', fm)
                else:
                    fm = f'\ntitle: "{new_name}"' + fm

                # Ensure aliases list has the original name
                if "aliases:" not in fm:
                    fm = fm.strip() + f'\naliases:\n  - "{old_name}"\n'
                elif f'"{old_name}"' not in fm:
                    fm = fm.replace("aliases:", f'aliases:\n  - "{old_name}"')

                content = f"---{fm}\n---{body}"
        else:
            content = f'---\ntitle: "{new_name}"\naliases:\n  - "{old_name}"\ntags:\n  - moc\n---\n\n' + content

        # Replace internal links
        for o_name, n_name in link_replacements.items():
            content = re.sub(rf"\[\[{re.escape(o_name)}\]\]", f"[[{n_name}]]", content)
            content = re.sub(rf"\[\[{re.escape(o_name)}\|", f"[[{n_name}|", content)

        # Write to target path
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Remove old file if paths differ
        if old_path != new_path and os.path.exists(old_path):
            os.remove(old_path)

    print("Successfully verified and applied MOC numbering and links.")


if __name__ == "__main__":
    main()
