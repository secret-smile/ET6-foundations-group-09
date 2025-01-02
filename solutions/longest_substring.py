#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the longest substring

Module contents:
    longest_substring: generates the longest substring without
    repetition for a given string.

Created on 2025-01-01
@author: Hiba Daffallah
"""


def longest_substring(input_string: str) -> str:
    """
     Generates a string containing the longest substring without repitition
     from the input_string.

    Parameters:
        input_string: str

    Returns :
      substring: the longest substring

    Raises:
        AssertionError: if the argument is not a string

    >>> longest_substring('')
    ''
    >>> longest_substring('bbbbbb')
    'b'
    >>> longest_substring('abcdef')
    'abcdef'
    >>> longest_substring('pwwkew')
    'wke'
    >>> longest_substring('celelocceli')
    'eloc'
    """
    assert isinstance(input_string, str)

    n = len(input_string)
    if n == 0:
        return ""

    sub = set()
    longest_sub = ""
    left = 0
    for right in range(n):
        while input_string[right] in sub:
            sub.remove(input_string[left])
            left += 1
        sub.add(input_string[right])
        current_len = right - left + 1
        if current_len > len(longest_sub):
            longest_sub = input_string[left : right + 1]

    return longest_sub
