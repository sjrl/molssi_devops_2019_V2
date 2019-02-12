"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = md.mean(num_list)
    expected = 3
    assert observed == expected


def test_mean_type_error():
    test_variable = 'Hello world'
    with pytest.raises(TypeError):
        md.mean(test_variable)


#@pytest.mark.skip
def test_mean_value_error():
    empty_list = []
    with pytest.raises(ValueError):
        md.mean(empty_list)
