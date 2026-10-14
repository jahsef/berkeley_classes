"""Lab 7: Linked Lists."""


from __future__ import annotations
from link import Link


def change(s, old, new):
    """Returns a linked list matching s but with all instances of old (if any)
    replaced by new.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = change(s, 3, 1)
    >>> print(t)
    (1 2 1)
    >>> u = change(t, 1, 2)
    >>> print(u)
    (2 2 2)
    >>> v = change(u, 5, 1)
    >>> print(v)
    (2 2 2)
    >>> print(s)   # The original linked list s is unchanged.
    (1 2 3)
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    if s == ():
        return ()
    if s.first ==  old:
        return Link(new, change(s.rest, old, new))
    else:
        return Link(s.first, change(s.rest,old,new))
    
    
    


def without(s, i: int):
    """Return a linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> print(without(s, 0))
    (5 7 9)
    >>> print(without(s, 2))
    (3 5 9)
    >>> print(without(s, 4))  # There is no index 4, so all of s is retained.
    (3 5 7 9)
    >>> print(s)              # The original linked list s is unchanged.
    (3 5 7 9)
    >>> without((), 0)
    ()
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    if not s:
        return ()
    if i == 0:
        return s.rest
    else:
        return Link(s.first, without(s.rest, i-1))
    


def store_digits(n: int):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(first=1, rest=())
    >>> print(store_digits(2345))
    (2 3 4 5)
    >>> print(store_digits(876))
    (8 7 6)
    >>> print(store_digits(2450))
    (2 4 5 0)
    >>> print(store_digits(20105))
    (2 0 1 0 5)
    >>> # a check that you do not use str or reversed
    >>> import inspect, ast
    >>> [n.id for n in ast.walk(ast.parse(inspect.getsource(store_digits)))
    ...  if isinstance(n, ast.Name) and n.id in ('str', 'reversed')]
    []
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    
    if n < 10:
        return Link(n)
    curr = store_digits(n//10)
    
    # with curr LL we have an end ptr
    # walk until end of LL and add 
    end = curr
    while end.rest != ():
        end = end.rest
    end.rest = store_digits(n%10)
    
    return curr
    
    
    
    
