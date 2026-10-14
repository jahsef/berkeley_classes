"""Homework 2: Control."""


def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    "*** YOUR CODE HERE ***"
    count = 1
    while n>1:
        count+=1
        print(n)
        if n % 2 == 0:
            n = n //2
        else:
            n = n*3 + 1
    print(n)
    return count
    
    
    


def abundant(n):
    """Print all ways of forming positive integer n by multiplying two positive
    integers together, ordered by the first term. Then, return whether the sum
    of the proper divisors of n is greater than n.

    A proper divisor of n evenly divides n but is less than n.

    >>> abundant(12) # 1 + 2 + 3 + 4 + 6 is 16, which is larger than 12
    1 * 12
    2 * 6
    3 * 4
    True
    >>> abundant(14) # 1 + 2 + 7 is 10, which is not larger than 14
    1 * 14
    2 * 7
    False
    >>> abundant(16)
    1 * 16
    2 * 8
    4 * 4
    False
    >>> abundant(20)
    1 * 20
    2 * 10
    4 * 5
    True
    >>> abundant(22)
    1 * 22
    2 * 11
    False
    >>> r = abundant(24)
    1 * 24
    2 * 12
    3 * 8
    4 * 6
    >>> r
    True
    >>> abundant(25)
    1 * 25
    5 * 5
    False
    >>> abundant(156)
    1 * 156
    2 * 78
    3 * 52
    4 * 39
    6 * 26
    12 * 13
    True
    """
    "*** YOUR CODE HERE ***"
#     A proper divisor of positive integer n is a positive integer smaller than n that evenly divides n.
# A positive integer is abundant if it is smaller than the sum of of its proper divisors.
# Implement a function abundant that takes a positive integer n. 
# It prints all ways of multiplying two positive integers to make n, with the smaller factor first, ordered from the smallest first factor to the largest. 
# Each pair is printed only once (so 3 * 4 is printed but 4 * 3 is not). It returns whether n is an abundant.
    proper_divisor_sum = 0
    for i in range(1,int(n**0.5)+1):
        # check if can divide
        if n / i != n // i:
            continue
        proper_divisor_sum += i + n//i
        # correction terms for double counting
        if i == n//i:
            proper_divisor_sum -= i
        print(i, "*",n//i)
    proper_divisor_sum -= n # correction term since we add n//i or n//1 which we dont want
    # check that sum of proper divisors is > n
    return proper_divisor_sum > n
        


if __name__ =="__main__":
    hailstone(10)