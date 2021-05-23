import io
import sys

sys.stdin = io.StringIO(
    """4 10 2 3
"""
)

from functools import lru_cache

n, s, a, b = map(int, input().split())


@lru_cache()
def method_number(i=1, mod=s % n):
    """p_i ~ p_{n-1} 累加模 n 为 mod 的方案数量"""
    if i == n - 1:
        return (a % n == mod) + (b % n == mod)

    is_a = (n - i) * a
    x_mod_n = mod - is_a % n
    if x_mod_n < 0:
        x_mod_n += n

    is_b = (n - i) * -b
    y_mod_n = mod - is_b % n
    if y_mod_n < 0:
        y_mod_n += n

    return method_number(i + 1, x_mod_n) + method_number(i + 1, y_mod_n)


print(method_number() % 100000007)
