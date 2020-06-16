# Convert content files from
# {base url}/{type}/{title} to {base url}/{type}/{year}/{month}/{title}
# while retaining alias urls
from pathlib import Path
import shutil
from datetime import datetime

# globals
ROOT_DIR = Path(__file__).parents[1]
CONTENT_DIR = ROOT_DIR / "content"
CONTENT_TYPES = ["post", "publication", "talk"]

paths = list(CONTENT_DIR.rglob("index.md"))
content_dirs = [p.parent for p in paths]


for p in paths:
    content_dir = p.parent
    content_type = content_dir.parent.name
    if content_type not in CONTENT_TYPES:
        continue
    print(f'Processing: {content_dir}')

    with open(p) as f:
        lines = f.read().splitlines()

    date = None
    for l in lines:
        if l.startswith("date"):
            date = l.split()[-1].strip('"')
            date = datetime.fromisoformat(date)
            break
    if not date:
        raise (ValueError(f"{p} does not have a valid date"))

    new_dir = CONTENT_DIR / content_type / str(date.year) / str(date.month)
    print(f'Moving to: {new_dir}')

    shutil.move(str(content_dir.resolve()), str(new_dir.resolve()))
