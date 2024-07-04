import json

def save_dict_as_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
def load_json_as_dict(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data
