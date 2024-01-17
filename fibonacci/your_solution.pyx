# cython: language_level=3
from libc.stdint cimport int64_t
import gmpy2
from gmpy2 import mpz
from cpython cimport array
import array

def fib(int n):
    a = mpz(0)
    b = mpz(1)
    # cdef array.array fib_seq = array.array('Q', [0, 1]) # 'Q' for unsigned long long (int64_t)
    cdef int i

    for i in range(1, n):
        a, b = b, a + b

    return 0 if n == 0 else b