import json

class FileHandler:
    @staticmethod
    def read_from_file(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def write_to_file(data, file_name):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)