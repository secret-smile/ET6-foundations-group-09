#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for providing the indices of two numbers in a list that add up to a target sum.

Module contents: Takes a list of numbers (integers or floats) and a target sum as input and returns the indices of the two numbers that add up to the target sum.

Created on 2025-01-04

@author: Jeffery Offei Darko
"""


def find_two_sum_indices(nums: list[float], target: float) -> list[int]:
    """
    Find two indices in the list such that their values add up to the target.

    Parameters:
    nums (list[float]): The list of numbers (integers or floats).
    target (float): The target sum.

    Returns:
    list[int]: The indices of the two numbers that add up to the target.

    Raises:
    AssertionError: If the input is not valid or no solution is found.

    Examples:
    >>> find_two_sum_indices([2, 7, 11, 15], 9)
    [0, 1]

    >>> find_two_sum_indices([3, 2.5, 4], 6.5)
    [1, 2]

    >>> find_two_sum_indices([3.0, 3], 6.0)
    [0, 1]
    """
    # Debugging input validation
    assert isinstance(nums, list), "Input must be a list."
    assert all(
        isinstance(num, (int, float)) for num in nums
    ), "List must contain numbers (integers or floats)."
    assert isinstance(
        target, (int, float)
    ), "Target must be a number (integer or float)."
    assert len(nums) > 1, "List must contain at least two numbers."

    # Debugging main logic
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    # Debugging output if no solution
    assert False, "No two numbers add up to the target sum."
