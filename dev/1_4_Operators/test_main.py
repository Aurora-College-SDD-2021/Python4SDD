""" These are the test functions.

For the moment you shouldn't edit them. They are here to automatically test your work.
We will look at unit tests and test driven development later in the course.
"""

import main
import pytest


def test_calc_sum():
    assert main.calc_sum(40, 2) == 42

def test_calc_difference():
    assert main.calc_difference(49, 7) == 42

def test_calc_product():
    assert main.calc_product(6, 7) == 42

def test_calc_quotient():
    assert main.calc_quotient(126, 3) == 42

def test_calc_remainder():
    assert main.calc_remainder(142, 50) == 42

def test_calc_exponentiation():
    assert main.calc_exponentiation(2, 10) == 1024

def test_largest():
    assert main.largest(42, 7) is 42

def test_smallest():
    assert main.smallest(42, 7) is 42

    
    