import json
import yaml
import os


def read_file(filepath):
    return open(filepath, 'r')


def parse_data(filepath, file_str):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.json':
        file = json.load(file_str)
    elif ext == '.yml' or '.yaml':
        file = yaml.safe_load(file_str)
    return file
