def find_two_sum_indices(nums: list[int], target: int) -> list[int]:
    """
    Find two indices in the list such that their values add up to the target.

    Parameters:
    nums (list[int]): The list of integers.
    target (int): The target sum.

    Returns:
    list[int]: The indices of the two numbers that add up to the target.

    Raises:
    AssertionError: If no solution is found.
    AssertionError: If the input is not a list of integers.
    AssertionError: If the target is not an integer.

    Examples:
    >>> find_two_sum_indices([2, 7, 11, 15], 9)
    [0, 1]
    
    >>> find_two_sum_indices([3, 2, 4], 6)
    [1, 2]
    
    >>> find_two_sum_indices([3, 3], 6)
    [0, 1]
    
    """
    if not isinstance(nums, list) or not all(isinstance(i, int) for i in nums):
        raise TypeError("Input must be a list of integers.")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer.")

    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    raise ValueError("No two sum solution.")
