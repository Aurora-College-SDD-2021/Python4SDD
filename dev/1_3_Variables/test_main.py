""" These are the test functions.

For the moment you shouldn't edit them. They are here to automatically test your work.
We will look at unit tests and test driven development later in the course.
"""

import main
import pytest


def test_the_answer():
    answer = main.the_answer()
    assert answer[0] != 42
    assert answer[1] != "harmless"
    