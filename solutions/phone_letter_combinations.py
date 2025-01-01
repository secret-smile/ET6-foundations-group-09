#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for all the possible letter combinations for a given number

Module contents:
      phone_letter_combinations: Creates a new list with possible
      letter combinations in phone keyboard for the numbers given
      for simplification I made it maximum of 2 digits

Created on 2024-12-30
Author: Hiba Daffallah
"""


def phone_letter_combinations(digits: str) -> list[str]:
    """
    phone_letter_combinations function creates a new list with possible
    letter combinations in phone keyboard for the numbers given
    for simplification I made it maximum of 2 digits

    Parameters:
    digits: string of numbers it should be from 2 to 9

    Returns:
    possible_combinations: list of characters

    Raises:
    AssertionError if the input was not a number

    Example:
    >>> phone_letter_combinations("23")
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    >>> phone_letter_combinations("")
    []
    >>> phone_letter_combinations("2")
    ['a', 'b', 'c']
    >>> phone_letter_combinations("1")
    Input must only contain digits from 2 to 9.
    """
    if not all(char in "23456789" for char in digits):
        raise AssertionError("Input must only contain digits from 2 to 9.")
    if not digits:
        return []
    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def possibility(i, temp):
        if i == len(digits):
            combination.append(temp[:])
            return
        for letter in digit_to_letters[digits[i]]:
            possibility(i + 1, temp + letter)

    combination = []
    possibility(0, "")

    return combination
