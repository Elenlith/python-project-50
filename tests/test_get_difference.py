import pytest
from pathlib import Path
from gendiff.get_difference import generate_diff


@pytest.mark.parametrize("out_format,expected", [
    ("stylish", '../python-project-50/tests/fixtures/res_styl.txt'),
    ("plain", '../python-project-50/tests/fixtures/res_plain.txt'),
    ("json", '../python-project-50/tests/fixtures/res_json.txt')
])
def test_generate_diff_json(out_format, expected):
    path_1 = '../python-project-50/tests/fixtures/file1.json'
    path_2 = '../python-project-50/tests/fixtures/file2.json'
    text = Path(expected).read_text()
    correct_answer = text[:-1]
    assert generate_diff(path_1, path_2, out_format) == correct_answer


@pytest.mark.parametrize("out_format,expected", [
    ("stylish", '../python-project-50/tests/fixtures/res_styl.txt'),
    ("plain", '../python-project-50/tests/fixtures/res_plain.txt'),
    ("json", '../python-project-50/tests/fixtures/res_json.txt')
])
def test_generate_diff_yaml(out_format, expected):
    path_1 = '../python-project-50/tests/fixtures/file1.yml'
    path_2 = '../python-project-50/tests/fixtures/file2.yml'
    text = Path(expected).read_text()
    correct_answer = text[:-1]
    assert generate_diff(path_1, path_2, out_format) == correct_answer
