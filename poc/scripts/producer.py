import json
from pathlib import Path

# Benign control input: pure JSON (no _OpaqueObject, no pickle path).
benign = {
    "kind": "control",
    "message": "hello from producer",
    "numbers": [1, 2, 3],
}

Path("artifacts").mkdir(parents=True, exist_ok=True)
Path("artifacts/benign.json").write_text(json.dumps(benign, indent=2) + "\n", encoding="utf-8")
print("Wrote artifacts/benign.json")