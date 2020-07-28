# Convert content files from
# {base url}/{type}/{title} to {base url}/{type}/{year}/{month}/{title}
# while retaining alias urls
import shutil
from datetime import datetime
from pathlib import Path

# globals
ROOT_DIR = Path(__file__).parents[1]
CONTENT_DIR = ROOT_DIR / "content"
CONTENT_TYPES = ["post", "publication", "talk"]

paths = list(CONTENT_DIR.rglob("index.md"))
content_dirs = [p.parent for p in paths]


for p in paths:
    post_dir = p.parent
    content_type = post_dir.parent.name
    if content_type not in CONTENT_TYPES:
        continue
    print(f"Processing: {post_dir}")

    with open(p) as f:
        lines = f.read().splitlines()

    date = None
    for l in lines:
        if l.startswith("date"):
            date = l.split()[-1].strip('"')
            date = datetime.fromisoformat(date)
            break

    front_matter_delimiter = None
    front_matter_type = None
    try:
        front_matter_delimiter = lines.index("---", 1)
        front_matter_type = "yaml"
    except ValueError:
        front_matter_delimiter = lines.index("+++", 1)
        front_matter_type = "toml"

    alias = f"/{content_type}/{post_dir.name}"
    if front_matter_type == "yaml":
        alias = f"aliases:\n- {alias}"
    else:
        alias = f'aliases = ["{alias}"]'
    lines.insert(front_matter_delimiter, alias)

    if not date:
        raise (ValueError(f"{p} does not have a valid date"))

    new_dir = (
        CONTENT_DIR / content_type / str(date.year) / str(date.month) / post_dir.name
    )
    print(f"Moving to: {new_dir}")
    shutil.move(str(post_dir.resolve()), str(new_dir.resolve()))

    # write updated index.md with alias in front matter
    lines.append("")
    lines = "\n".join(lines)
    with open(new_dir / "index.md", "w") as f:
        f.write(lines)
