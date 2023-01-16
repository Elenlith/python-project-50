import json
import yaml


def parse_json(filepath):
    return json.load(open(filepath))


def parse_yaml(filepath):
    with open(filepath, 'r') as file:
        value = yaml.safe_load(file)
    return value
