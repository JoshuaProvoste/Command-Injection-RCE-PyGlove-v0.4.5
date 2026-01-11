import base64
import pickle
import json

def generate_opaque_json_file(output_filename='poc.json'):
    # Example value to serialize (can be any Python object)
    data = {'hello', 'world'}

    # Serialize with pickle and encode with base64
    encoded = base64.encodebytes(pickle.dumps(data)).decode('utf-8')

    # Build JSON structure expected by _OpaqueObject.from_json
    obj = {
        "_type": "json_conversion._OpaqueObject",
        "value": encoded
    }

    # Write to JSON file
    with open(output_filename, 'w') as f:
        json.dump(obj, f, indent=2)

if __name__ == '__main__':
    generate_opaque_json_file()
