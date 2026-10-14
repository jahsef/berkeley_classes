"""Lab 1: Functions."""


def pick_digit(n, k):
    """Return the k-th digit from the right of n.

    >>> pick_digit(3579, 2)
    5
    >>> pick_digit(3579, 0)
    9
    >>> pick_digit(3579, 10)
    0
    """
    
    modulo = 10
    truncated_n = n
    for i in range(k):
        mult = truncated_n // modulo
        truncated_n = mult 
        # print(truncated_n)
        
    

    truncated_n = truncated_n - (truncated_n//modulo * modulo)
    
    
    return truncated_n


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    list = [a,b,c]
    list.sort()
    return list[1]


if __name__ == "__main__":
    pass