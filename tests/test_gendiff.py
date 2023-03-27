import gendiff
from gendiff import gendiff_with_formatter


def test_names():
    assert hasattr(gendiff, 'generate_diff')


def test_references():
    assert gendiff.generate_diff is gendiff_with_formatter.generate_diff


def test_all_metavar():
    assert 'generate_diff' in gendiff.__all__
