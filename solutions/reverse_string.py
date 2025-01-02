def reverse_string(string: str):
    """This function takes a string and returns the reverse form of the string

    Parameters:
    string (str): The input to be reversed

    Returns:
    str: The reversed version of the input string

    Raises:
    AssertionError: If the input is not a string

    Examples:
    >>> reverse_string('hello')
    'olleh'

    >>> reverse_string('Python programming')
    'gnimmargorp nohtyP'

    >>> reverse_string('12345')
    '54321'

    >>> reverse_string('Madam')
    'madaM'

    >>> reverse_string('racecar')
    'racecar'
    """
    # Check if input is a string
    assert isinstance(string, str), "Input must be a string"

    return string[::-1]


print(reverse_string("Evan Cole"))
