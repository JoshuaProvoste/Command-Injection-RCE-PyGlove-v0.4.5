import json
import os
import pyglove as pg
from pyglove.json_conversion import _OpaqueObject  # Fuerza import y registro

def load_pyglove_from_json(filename='poc.json'):
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
        # _OpaqueObject se registró al importar el módulo; ahora el nombre calificado funcionará
        obj = pg.from_json(data)
        return obj
    except Exception as e:
        print(f"Error while reconstructing object with PyGlove: {e}")
        return None

if __name__ == '__main__':
    result = load_pyglove_from_json()
    if result is not None:
        print("Reconstructed object:", result)
