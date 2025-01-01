#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the longest palindromic substring in a string.

Module contents:
    - find_longest_palindrome: finds the longest palindrome within a string.
    - is_palindrome: helper function to check if a string is a palindrome.

Created on 28 12 2024
@author: Mahdia Ahmadi
"""


def find_longest_palindrome(text: str) -> str:
    """
    Finds the longest palindromic substring within the input string.

    A palindrome reads the same forwards and backwards. This function returns
    the first occurrence of the longest palindrome if multiple exist.

    Parameters:
        text: str, the input string to search for palindromes

    Returns:
        str: the longest palindromic substring found

    Raises:
        AssertionError: if the input is not a string

    Examples:
        >>> find_longest_palindrome("babad")
        'bab'
        >>> find_longest_palindrome("racecar")
        'racecar'
        >>> find_longest_palindrome("hello")
        'll'
        >>> find_longest_palindrome("python")
        'p'
        >>> find_longest_palindrome("")
        ''
    """
    # Input validation
    assert isinstance(text, str), "Input must be a string"

    # Handle empty string and single characters
    if len(text) <= 1:
        return text

    # Initialize variables to track the longest palindrome
    longest_start = 0
    longest_length = 1

    # Check all possible substrings
    for start in range(len(text)):
        for end in range(start + longest_length, len(text) + 1):
            substring = text[start:end]
            # Only check if this could be a longer palindrome
            if is_palindrome(substring) and len(substring) > longest_length:
                longest_start = start
                longest_length = len(substring)

    # Return the longest palindrome found
    return text[longest_start : longest_start + longest_length]


def is_palindrome(text: str) -> bool:
    """
    Checks if the input string is a palindrome.

    Parameters:
        text: str, string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("a")
        True
        >>> is_palindrome("")
        True
    """
    # Compare string with its reverse
    return text == text[::-1]
