"""
Add your solution in here
"""


def fib(n) -> int:
    """
    Calculate the nth Fibonacci number

    when n is 0 return 0
    when n is 1 return 1
    when n is 2 return 1
    when n is 3 return 2
    ...


    The fibonacci sequence is defined as follows:
    0,1,1,2,3,5,8,13,21,34 ...
    """
    fib_seq = [0, 1]
    for x in range(1, n):
        next_num = fib_seq[0] + fib_seq[1]
        fib_seq[0] = fib_seq[1]
        fib_seq[1] = next_num
    return 0 if n == 0 else fib_seq[1]

    # This could be made clearer and more memory efficient using vars instead of a list
