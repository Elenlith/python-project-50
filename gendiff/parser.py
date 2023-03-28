import json
import yaml
import os


def read_file(filepath):
    return open(filepath, 'r')


def parse_data(filepath, file_str):
    file_extension = os.path.splitext(filepath)[-1].lower()
    if file_extension == '.json':
        contents = json.load(file_str)
    elif file_extension == '.yml' or '.yaml':
        contents = yaml.safe_load(file_str)
    return contents
