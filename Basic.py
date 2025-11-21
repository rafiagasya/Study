def add_to_zero(nums):
    """
    Check if any two numbers in the list add up to zero.
    
    >>> add_to_zero([1, 2, 3, -2])
    True
    >>> add_to_zero([1, 2, 3, 4])
    False
    >>> add_to_zero([])
    False
    >>> add_to_zero([5])
    False
    >>> add_to_zero([1, -1])
    True
    >>> add_to_zero([0, 0])
    True
    >>> add_to_zero([3, -3, 5, -5])
    True
    """
    
    if len(nums) < 2:
        return False
    
    num_set = set(nums)
    
    for num in nums:
        if -num in num_set:
            return True
    
    return False


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    
    if results.failed == 0:
        print(f" All tests passed!")
        print(f" Tests attempted: {results.attempted}")
        print(f" Tests failed: {results.failed}")
    else:
        print(f"{results.failed}/{results.attempted} tests failed")
