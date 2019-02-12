"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


@pytest.mark.parametrize("sentence, expected_title_case",
                         [('tHIs iS a test.', 'This Is A Test.'),
                          ('ThIs iS a StRinG tO be COnvErted.', 'This Is A String To Be Converted.')])
def test_title_case(sentence, expected_title_case):
    assert md.title_case(sentence) == expected_title_case


def test_title_case_type_error():
    test_variable = 2
    with pytest.raises(TypeError):
        md.title_case(test_variable)


def test_title_case_index_error():
    test_variable = ''
    with pytest.raises(IndexError):
        md.title_case(test_variable)
