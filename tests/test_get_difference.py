import json
import yaml
from pathlib import Path
from gendiff.get_difference import generate_diff


def test_generate_diff_yaml_stylish():
    with open('../python-project-50/tests/fixtures/file1.yml', 'r') as file:
        file_1 = yaml.safe_load(file)
    with open('../python-project-50/tests/fixtures/file2.yml', 'r') as file:
        file_2 = yaml.safe_load(file)
    t = Path('../python-project-50/tests/fixtures/res_styl.txt').read_text()
    correct_answer = t[:-1]
    assert generate_diff(file_1, file_2) == correct_answer


def test_generate_diff_json_stylish():
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path('../python-project-50/tests/fixtures/res_styl.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2) == correct_answer


def test_generate_diff_json_plain():
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path('../python-project-50/tests/fixtures/res_plain.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, 'plain') == correct_answer


def test_generate_diff_yaml_plain():
    with open('../python-project-50/tests/fixtures/file1.yml', 'r') as file:
        file_1 = yaml.safe_load(file)
    with open('../python-project-50/tests/fixtures/file2.yml', 'r') as file:
        file_2 = yaml.safe_load(file)
    text = Path('../python-project-50/tests/fixtures/res_plain.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, 'plain') == correct_answer


def test_generate_diff_json_json():
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path('../python-project-50/tests/fixtures/res_json.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, 'json') == correct_answer


def test_generate_diff_yaml_json():
    with open('../python-project-50/tests/fixtures/file1.yml', 'r') as file:
        file_1 = yaml.safe_load(file)
    with open('../python-project-50/tests/fixtures/file2.yml', 'r') as file:
        file_2 = yaml.safe_load(file)
    text = Path('../python-project-50/tests/fixtures/res_json.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, 'json') == correct_answer
