import pytest

from test_ut import sample_module


@pytest.fixture()
def sample_numbers_unsorted() -> list[int]:
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


def test_sort_numbers(sample_numbers_unsorted):
    actual = sample_module.sort_numbers(sample_numbers_unsorted)
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert actual == expected


def test_reverse_numbers(sample_numbers_unsorted):
    actual = sample_module.reverse_numbers(sample_numbers_unsorted)
    expected = [5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3]
    assert actual == expected


def test_api_returns_data():
    actual = sample_module.get_api_data()
    expected = 'MODIFIED DATA'
    assert actual == expected
