"""
Arrange-Act-Assert model:
- Arrange, or set up the conditions for the test
- Act, by calling some function or method
- Assert that some end condition is true
"""

"""
You must create a test function with a name that starts with test_.
"""


# def test_passing():
#     assert (1, 2, 3) == (1, 2, 3)
#
#
# def test_failing():
#     assert (1, 2, 3) == (3, 2, 1)


def add(a, b):
    for num in [a, b]:
        if not isinstance(num, int | float):
            return 0
    return a + b


class TestGroup:
    def test_one_plus_one_is_two(self):
        a, b = 1, 1  # Arrange
        actual = add(a, b)  # Act
        expected = 2
        assert actual == expected  # Assert

    def test_one_plus_letter_returns_zero(self):
        a, b = 1, 'a'  # Arrange
        actual = add(a, b)  # Act
        expected = 0
        assert actual == expected  # Assert
