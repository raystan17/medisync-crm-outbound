"""
Generate personalized investor emails and LinkedIn DMs from templates.
Run from the outbound-engine directory: python scripts/generate_messages.py
"""

import csv
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Paths relative to project root (outbound-engine)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Default template variables
DEFAULTS = {
    "user_count": "2,000+",
    "premium_growth": "30+",
    "demo_link": "https://www.medisynclabs.ca/demo-login",
    "raise_amount": "100,000",
}


def load_investors(csv_path: Path) -> list[dict]:
    """Load investor data from CSV."""
    investors = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            firm = (row.get("firm") or "").strip()
            if not firm:
                continue
            investor_name = (row.get("investor_name") or "").strip() or "the team"
            focus_area = (row.get("focus_area") or "").strip() or "healthcare"
            investors.append({
                "firm": firm,
                "investor_name": investor_name,
                "first_name": (row.get("first_name") or "").strip(),
                "focus_area": focus_area,
                "linkedin": (row.get("linkedin") or "").strip(),
            })
    return investors


def build_context(investor: dict) -> dict:
    """Build template context from investor row and defaults."""
    return {
        "investor_name": investor["investor_name"],
        "firm_name": investor["firm"],
        "focus_area": investor["focus_area"],
        **DEFAULTS,
    }


def main() -> None:
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    email_template = env.get_template("investor_email_base.md")
    dm_template = env.get_template("investor_dm_base.md")

    investors = load_investors(DATA_DIR / "investors.csv")
    if not investors:
        print("No investors found in data/investors.csv")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    email_blocks = []
    dm_blocks = []

    for inv in investors:
        ctx = build_context(inv)
        header = f"{inv['firm']}"
        if inv["investor_name"] != "the team":
            header += f" — {inv['investor_name']}"

        # Render email (template includes subject + body)
        email_content = email_template.render(**ctx)
        email_blocks.append(f"## {header}\n\n{email_content}")

        # Render LinkedIn DM
        dm_content = dm_template.render(**ctx)
        dm_blocks.append(f"## {header}\n\n{dm_content}")

    # Write output files with clear separators for easy copy-paste
    separator = "\n\n---\n\n"
    emails_path = OUTPUT_DIR / "emails.md"
    dms_path = OUTPUT_DIR / "linkedin_dms.md"

    with open(emails_path, "w", encoding="utf-8") as f:
        f.write(separator.join(email_blocks))

    with open(dms_path, "w", encoding="utf-8") as f:
        f.write(separator.join(dm_blocks))

    print(f"Generated {len(investors)} emails -> {emails_path}")
    print(f"Generated {len(investors)} LinkedIn DMs -> {dms_path}")


if __name__ == "__main__":
    main()
