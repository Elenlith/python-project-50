import json
from pathlib import Path
from gendiff.modules.get_difference import generate_diff


def test_generate_diff():
    file_1 = json.load(open('../python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('../python-project-50/tests/fixtures/file2.json'))
    text = Path('../python-project-50/tests/fixtures/result.txt').read_text()
    correct_answer = text[:-1]
    assert generate_diff(file_1, file_2) == correct_answer
