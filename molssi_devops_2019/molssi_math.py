"""
molssi_math.py
A sample python package

Handles the primary functions
"""

import numpy as np

def mean(num_list):
    """
    Computes the mean of a list of numbers.

    Parameters
    ----------
    num_list : list
        List of numbers.

    Returns
    -------
    mean : float
        Mean of the numbers in num_list.
    """

    # Check that input it type list
    if not isinstance(num_list, list):
        raise TypeError('Invalid input %s - must be type list.' % (num_list))

    # Check that list has length greater than 0
    if len(num_list) == 0:
        raise ValueError('Cannot calculate mean of empty list.')

    # Perform the mean
    total_sum = 0.0
    for item in num_list:
        total_sum += item
    mean = total_sum / len(num_list)
    return mean


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
