import json
import yaml
import os


def read_file(filepath):
    return open(filepath, 'r')


def parse_json(file_str):
    return json.load(file_str)


def parse_yaml(file_str):
    return yaml.safe_load(file_str)


def parse_data(filepath, file_str):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.json':
        file = parse_json(file_str)
    elif ext == '.yml' or '.yaml':
        file = parse_yaml(file_str)
    return file
