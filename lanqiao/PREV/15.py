"""这题就是找递推公式

硬要说的话，也算动态规划吧，不过和一般的动态规划题考查点不太一样
"""

from functools import lru_cache


def A(n):
    return 2**(n - 1)


@lru_cache()
def B(n):
    if n == 1:
        return 1
    if n == 2:
        return 6
    return 4 * B(n - 2) + 2 * B(n - 1) + 2 * A(n - 1)


def C(n):
    if n == 1:
        return 2
    if n == 2:
        return 24
    return 4 * B(n) + 16 * sum([A(i) * B(n - 1 - i) for i in range(1, n - 1)])


n = int(input())
print(C(n) % 1000000007)
