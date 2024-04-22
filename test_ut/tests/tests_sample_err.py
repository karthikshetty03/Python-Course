import pytest


def func(var) -> str:
    if not isinstance(var, str):
        raise ValueError('var is not a string')
        # raise Exception
    else:
        return var


def test_int_raise_type_error():
    with pytest.raises(ValueError):
        func(1)
