import json
from gendiff.modules.get_difference import generate_diff


def test_generate_diff():
    file_1 = json.load(open('/home/daekir/python-project-50/tests/fixtures/file1.json'))
    file_2 = json.load(open('/home/daekir/python-project-50/tests/fixtures/file2.json'))
    assert generate_diff(file_1, file_2) == "{\n- age: 35\n+ birth_year: 1985\n- married: true\n+ married: false\n  name: Artyom\n- surname: Ivanov\n+ surname: Petrov\n}"
