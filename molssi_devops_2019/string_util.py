"""
string_util.py
A sample python package

Misc. string processing functions
"""


def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first character of every word is capitalized. Otherwise,
    lowercase.

    Parameters
    ----------
    sentence: string
        String to be converted to title case

    Returns
    -------
    ret: string
        Input string in title case

    Examples
    --------
    >>> title_case('ThIs iS a StRinG tO be COnvErted.')
        'This Is A String To Be Converted.'
    """

    # Check that input is string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be type string' % (sentence))

    # Error if empty string
    if len(sentence) == 0:
        raise IndexError('Cannot apply title function to empty string.')

    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()

    return ret



    return True
