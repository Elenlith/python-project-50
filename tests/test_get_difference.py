import json
import yaml
from pathlib import Path
from gendiff.modules.get_difference import generate_diff


def test_generate_diff_simple_yaml():
    with open('../python-project-50/tests/fixtures/file1.yml', 'r') as file:
        file_1 = yaml.safe_load(file)
    with open('../python-project-50/tests/fixtures/file2.yml', 'r') as file:
        file_2 = yaml.safe_load(file)
    t = Path('../python-project-50/tests/fixtures/result_yml.txt').read_text()
    correct_answer = t[:-1]
    assert generate_diff(file_1, file_2) == correct_answer


def test_generate_diff_adv_json():
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path('../python-project-50/tests/fixtures/result_j.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2) == correct_answer
