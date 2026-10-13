"""
Reorganize Archive Script
=========================
Purpose:
    Categorizes loose files (Markdown and Obsidian Canvas) residing in the `_archive/`
    directory and moves them into dedicated topic directories in the workspace root.

Categories & Target Folders:
    - Mathematics & Numerical Methods -> `mathematics/`
    - Undergraduate Thesis & ML Research -> `thesis-research/`
    - Technical Analysis & Trading -> `trading-finance/`
    - SQL & Database Querying -> `sql-databases/`
    - R Programming -> `r-programming/`
    - Psychology & Attachment Theory -> `psychology/`
    - Productivity & PKM -> `productivity/`
    - Insurance Advisory & Business -> `business-advisory/`
    - Personal Life & Hobbies -> `personal/`
    - Uncategorized fallback -> `archive-misc/`

Usage:
    Run from the vault root (or content/_drafts directory):
        python _scripts/reorganize_archive.py
"""

import os
import shutil

ARCHIVE_DIR = "_archive"
BASE_DIR = "."

CATEGORIES = {
    "Mathematics & Numerical Methods": {
        "folder": "mathematics",
        "keywords": [
            "math", "algebra", "theorem", "calculus", "convergence", "matrix",
            "eigenvalue", "integration", "interpolation", "polynomial", "field",
            "cofactor", "determinant", "dirac", "homomorphism", "irreducibility",
            "kronecker", "linear transformation", "multi-set", "numerical",
            "projective geometry", "symmetric", "tensor", "vector", "stat ",
            "hypothesis", "probability", "distribution", "variance", "stochastic",
            "lagrange", "equation", "fraction", "formula", "arithmetic",
            "inner product", "kernel", "fixed point"
        ]
    },
    "Undergraduate Thesis & ML Research": {
        "folder": "thesis-research",
        "keywords": [
            "thesis", "literature", "methodology", "dataset", "algorithm",
            "svm", "gaussian", "mixture model", "optimization", "clustering",
            "regression", "abstract", "review of", "support vector",
            "machine learning", "neural network", "classification", "f1 score",
            "precision", "overfitting", "cross validation", "empirical risk",
            "pgm", "model", "prediction", "accuracy", "error analysis", "gradient"
        ]
    },
    "Technical Analysis & Trading": {
        "folder": "trading-finance",
        "keywords": [
            "rsi", "indicator", "market", "stock", "volatility", "trading",
            "moving average", "true range", "blue-chip", "finance concepts",
            "technical analysis", "ulcer index", "red tide"
        ]
    },
    "SQL & Database Querying": {
        "folder": "sql-databases",
        "keywords": [
            "sql", "database", "dml", "subqueries", "query", "data frame", "data type"
        ]
    },
    "R Programming": {
        "folder": "r-programming",
        "keywords": [
            " r ", " r.", "rstudio", "r programming", "syntax in r", "types in r",
            "bar plot", "displaying factor"
        ]
    },
    "Psychology & Attachment Theory": {
        "folder": "psychology",
        "keywords": [
            "attachment", "psychology", "behavior", "ainsworth", "relationship"
        ]
    },
    "Productivity & PKM": {
        "folder": "productivity",
        "keywords": [
            "obsidian", "second brain", "latex", "tikz", "workflow", "habits",
            "goal", "task", "ticktick", "para", "reading", "journal", "notes",
            "template", "learning", "study", "capacities", "shortcuts", "anki"
        ]
    },
    "Insurance Advisory & Business": {
        "folder": "business-advisory",
        "keywords": [
            "pru", "insurance", "sales", "client", "finance", "credit card",
            "recruitment", "business", "accounting", "engagement", "swot",
            "pera", "philhealth", "career", "linkedin", "ubp", "communication",
            "social media", "content", "lead generation", "raci", "marketing",
            "customer"
        ]
    },
    "Personal Life & Hobbies": {
        "folder": "personal",
        "keywords": [
            "nihongo", "japanese", "hapon", "genki", "kanji", "arnis", "fitness",
            "skincare", "mobile legends", "rpg", "spiritual", "god", "double stick",
            "pe 2", "calamba", "waray", "speech"
        ]
    },
    "Archive Uncategorized": {
        "folder": "archive-misc",
        "keywords": []
    }
}


def main():
    if not os.path.exists(ARCHIVE_DIR):
        print(f"Directory '{ARCHIVE_DIR}' does not exist.")
        return

    # Ensure all target directories exist
    for info in CATEGORIES.values():
        os.makedirs(os.path.join(BASE_DIR, info["folder"]), exist_ok=True)

    moved_count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        file_path = os.path.join(ARCHIVE_DIR, filename)

        # Skip subdirectories and hidden dot-files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue

        filename_lower = filename.lower()
        assigned_cat = "Archive Uncategorized"

        for cat, info in CATEGORIES.items():
            if cat == "Archive Uncategorized":
                continue
            if any(kw in filename_lower for kw in info["keywords"]):
                assigned_cat = cat
                break

        # Edge case: isolate R programming matches to avoid generic "r" letters
        if " r " in f" {filename_lower} " or filename_lower.startswith("r ") or " r." in filename_lower:
            assigned_cat = "R Programming"

        target_folder = CATEGORIES[assigned_cat]["folder"]
        target_path = os.path.join(BASE_DIR, target_folder, filename)
        shutil.move(file_path, target_path)
        moved_count += 1

    print(f"Successfully organized and moved {moved_count} file(s) from '{ARCHIVE_DIR}'.")


if __name__ == "__main__":
    main()
