""" These are the test functions.

For the moment you shouldn't edit them. They are here to automatically test your work.
We will look at unit tests and test driven development later in the course.
"""

import main
import pytest


def test_data_type():
    values = main.data_type()
    assert  type(values[0]) == int
    assert  type(values[1]) == float
    assert  type(values[2]) == str
    assert  type(values[3]) == bool
    