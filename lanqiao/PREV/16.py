# import sys
# import io
#
# sys.stdin = io.StringIO("""2 3 6
# 3 6
# """)

from collections import Counter
from functools import lru_cache

a = tuple(Counter(map(int, input().split())).items())
b = frozenset(map(int, input().split()))

next_choices = {}
for i, _ in a:
    t = set()
    for j, _ in a:
        if i % j == 0 or j % i == 0:
            t.add(j)
    next_choices[i] = frozenset(t)


@lru_cache()
def is_losing(a: tuple, b: frozenset):
    for i in b:
        a1 = iter(a)
        a2 = []

        for j, k in a1:
            if i == j:
                if k != 1:
                    a2.append((j, k - 1))
                a2.extend(a1)
                break
            else:
                a2.append((j, k))
        else:
            continue

        if is_losing(tuple(a2), next_choices[i]) is True:
            return i

    return True


t = is_losing(a, b)
if t is True:
    print(-1)
else:
    print(t)
