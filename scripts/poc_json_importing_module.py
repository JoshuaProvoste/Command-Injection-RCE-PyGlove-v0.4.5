import json
import os
import json_conversion as jc  # Asegúrate de que esté en el mismo directorio o en PYTHONPATH

def load_from_json_conversion(filename='poc.json'):
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
    result = load_from_json_conversion()
    if result is not None:
        print("Reconstructed object:", result)
