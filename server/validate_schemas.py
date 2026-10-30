import json
import shutil
from pathlib import Path

from jsonschema.validators import validator_for

SOURCE_DIR = Path("/input")
OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for schema_file in SOURCE_DIR.rglob("*.json"):

    if schema_file.name == "current.json":
        # Discard current.json, we only want the versioned files
        continue

    if any(part.startswith("_") for part in schema_file.parts):
        continue

    with open(schema_file) as f:
        schema = json.load(f)

    # Validate that this is itself a valid JSON Schema
    validator_cls = validator_for(schema)
    validator_cls.check_schema(schema)

    rel_path = schema_file.relative_to(SOURCE_DIR)

    target = OUTPUT_DIR / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(schema_file, target)

    print(f"VALID   {rel_path}")
