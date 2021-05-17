"""lucas 定理，求组合数对素数的模
"""

from math import comb


def lucas(n, k, p):
    """C^k_n mod p"""
    if k == 0:
        return 1
    a, b = divmod(n, p)
    c, d = divmod(k, p)
    return lucas(a, c, p) * comb(b, d)


n, k, p = map(int, input().split())
print(lucas(n, k, p))
print(comb(n, k) % p)
