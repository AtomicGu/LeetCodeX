from collections import Counter

c = Counter()
for i in range(1, 2020 + 1):
    c.update(str(i))
print(c)
