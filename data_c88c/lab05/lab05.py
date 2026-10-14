"""Lab 5: Sequences."""
# remember list * int => duplicates list that many times
# range() literally returns range object with same args i guess


def print_if(s, f):
    """Print each element of s for which f returns a true value.

    >>> print_if([3, 4, 5, 6], lambda n: n > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda n: n % 2 == 0)
    4
    6
    >>> print(result)  # print_if should return None
    None
    """
    for x in s:
        "*** YOUR CODE HERE ***"
        if f(x):
            print(x)

def close(s, k):
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        "*** YOUR CODE HERE ***"
        if abs(s[i] - i) <=k:
            count+=1
    return count



from math import sqrt

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    
    return [int(n**0.5) for n in s if n**0.5 == int(n**0.5)]


def double_eights(n):
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> double_eights(1077)
    False
    """
    "*** YOUR CODE HERE ***"
    # base case we hit an 8, check 88
    # or if n < 10 return false
    if n < 10:
        return False
    
    # we can prune 2 numbers if this doesnt return
    if n % 10 == 8:
        if (n // 10) % 10 == 8:
            return True
    
    return double_eights(n//10)
        


def flatten(s):
    """Returns a flattened version of list s, which contains lists and integers.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [[[[5], 6]], 7]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(deep[1])
    [2, 3]
    >>> deep                                # input list should be unchanged
    [1, [[2], 3], 4, [[[[5], 6]], 7]]
    """
    "*** YOUR CODE HERE ***"


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6
    6
    """
    "*** YOUR CODE HERE ***"


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    """
    "*** YOUR CODE HERE ***"
