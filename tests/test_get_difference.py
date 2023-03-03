import pytest
import json
import yaml
from pathlib import Path
from gendiff.get_difference import generate_diff


@pytest.mark.parametrize("out_format,expected", [
    ("stylish", '../python-project-50/tests/fixtures/res_styl.txt'),
    ("plain", '../python-project-50/tests/fixtures/res_plain.txt'),
    ("json", '../python-project-50/tests/fixtures/res_json.txt')
])
def test_generate_diff_json(out_format, expected):
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path(expected).read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, out_format) == correct_answer


@pytest.mark.parametrize("out_format,expected", [
    ("stylish", '../python-project-50/tests/fixtures/res_styl.txt'),
    ("plain", '../python-project-50/tests/fixtures/res_plain.txt'),
    ("json", '../python-project-50/tests/fixtures/res_json.txt')
])
def test_generate_diff_yaml(out_format, expected):
    with open('../python-project-50/tests/fixtures/file1.yml', 'r') as file:
        file_1 = yaml.safe_load(file)
    with open('../python-project-50/tests/fixtures/file2.yml', 'r') as file:
        file_2 = yaml.safe_load(file)
    text = Path(expected).read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2, out_format) == correct_answer
