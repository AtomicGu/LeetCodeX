"""题解：
https://www.cnblogs.com/gangduo%2Dshangjinlieren/p/4372897.html

妈的，绝了！
"""

from math import comb
from functools import lru_cache


def lucas(n, k, p):
    """C^k_n mod p"""
    if k == 0:
        return 1
    a, b = divmod(n, p)
    c, d = divmod(k, p)
    return lucas(a, c, p) * comb(b, d)


n = int(input())
m = int(input())
k = int(input())


@lru_cache()
def dp(k, j):
    if j == 0:
        return 0


print(lucas(n, m, 999101) * sum([comb(n, i) * i ** k for i in range(n + 1)]) % 999101)
