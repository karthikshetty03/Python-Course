import pytest

from test_ut import sample_module

"""
first argument to parametrize is the name of the parameter
Example: @pytest.mark.parametrize('text, expected_result', ['abc', 'cba'])
second argument is a list of tuples containing the values for the parameters
same arguments should be passed to the test function
"""


@pytest.mark.parametrize('text, expected_result', [
    ('abc', 'cba'),
    ('hello', 'olleh'),
    # ('adidas', 'cascades'),
    ('123', '321'),
    ("", "")
])
def test_reverse_text(text, expected_result):
    actual = sample_module.reverse_text(text)
    expected = expected_result
    assert actual == expected


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


"""
marks are used to categorize tests
xfail: expected to fail
skip: skip the test
skipif: skip the test if the condition is met
"""


class TestGroup:
    @pytest.mark.xfail
    def test_will_always_fail(self):
        assert False

    def test_always_succeeds(self):
        assert True

    @pytest.mark.skip
    def test_sort_numbers(self, sample_numbers_unsorted):
        actual = sample_module.sort_numbers(sample_numbers_unsorted)
        expected = []
        assert actual == expected

    @pytest.mark.skipif(True, reason='This test is skipped because of the condition')
    def test_reverse_numbers(self, sample_numbers_unsorted):
        actual = sample_module.reverse_numbers(sample_numbers_unsorted)
        expected = []
        assert actual == expected
