import json
from pathlib import Path
import pyglove as pg

p = Path("artifacts/benign.json")
data = json.loads(p.read_text(encoding="utf-8"))

# Procesamiento benigno: round-trip seguro
obj = pg.from_json(data)
_ = pg.to_json(obj)

print("Benign JSON processed OK")