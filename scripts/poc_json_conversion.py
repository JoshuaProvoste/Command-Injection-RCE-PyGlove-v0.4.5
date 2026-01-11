import json
import os
import pyglove as pg
import importlib.util

# Minimal valid use of pyglove that doesn’t explotar nada
_ = pg.to_json(True)

def load_json_conversion_module():
    module_path = os.path.join('pyglove', 'core', 'utils', 'json_conversion.py')
    if not os.path.isfile(module_path):
        print(f"Error: json_conversion.py not found at {module_path}")
        return None

    spec = importlib.util.spec_from_file_location('json_conversion', module_path)
    json_conversion = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(json_conversion)
    return json_conversion

def load_object_from_json(filename='poc.json'):
    jc = load_json_conversion_module()
    if jc is None:
        return None

    if not os.path.isfile(filename):
        print(f"Error: file not found: {filename}")
        return None

    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in {filename}: {e}")
        return None

    try:
        obj = jc.from_json(data)
        return obj
    except Exception as e:
        print(f"Error while reconstructing object with json_conversion: {e}")
        return None

if __name__ == '__main__':
    result = load_object_from_json()
    if result is not None:
        print("Reconstructed object:", result)
