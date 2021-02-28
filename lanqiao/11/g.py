from collections import Counter

word = input()
c = Counter(word)
a = max(c.items(), key=lambda x: x[1])
print(a[0])
print(a[1])
