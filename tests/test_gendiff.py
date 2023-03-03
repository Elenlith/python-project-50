import gendiff
from gendiff import get_difference


def test_names():
    assert hasattr(gendiff, 'generate_diff')


def test_references():
    assert gendiff.generate_diff is get_difference.generate_diff


def test_all_metavar():
    assert 'generate_diff' in gendiff.__all__
