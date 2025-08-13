# JSON Handling in Python (basics)
# JSON = JavaScript Object Notation
# Format for sending/receiving data between client and server.

# Example : 
{
  "id": 1,
  "name": "Mann",
  "skills": ["Python", "Backend"]
}

# using json module 

import json

# Python object → JSON string
person = {"name": "Mann", "age": 22}
json_str = json.dumps(person)  # dumps = dump string
print(json_str)  # {"name": "Mann", "age": 22}

# JSON string → Python object
json_data = '{"name": "Mann", "age": 22}'
python_obj = json.loads(json_data)  # loads = load string
print(python_obj["name"])  # Mann
