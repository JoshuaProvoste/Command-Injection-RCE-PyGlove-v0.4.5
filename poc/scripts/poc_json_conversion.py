import os
import json
from pyglove.core.utils import json_conversion as jc

def load_objects_from_json(filenames=None):
    if filenames is None:
        filenames = ['artifacts/benign.json', 'artifacts/poc.json']  # orden explícito

    results = []
    for filename in filenames:
        if not os.path.isfile(filename):
            print(f"Skip: file not found: {filename}")
            continue

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: invalid JSON in {filename}: {e}")
            results.append((filename, None))
            continue

        try:
            obj = jc.from_json(data)
            results.append((filename, obj))
        except Exception as e:
            print(f"Error while reconstructing object with json_conversion from {filename}: {e}")
            results.append((filename, None))

    return results

if __name__ == '__main__':
    for fname, obj in load_objects_from_json():
        if obj is not None:
            print(f"Reconstructed from {fname}: {obj}")