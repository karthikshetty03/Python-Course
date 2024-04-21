"""
naming should be conftest.py
pytest will automatically find this file and execute it before running any test
"""

import pytest
import test_ut.sample_module as sm


@pytest.fixture()
def sample_numbers_unsorted() -> list[int]:
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


@pytest.fixture(autouse=True)
def disable_api_data():
    sm.get_api_data = lambda: 'MODIFIED DATA'
