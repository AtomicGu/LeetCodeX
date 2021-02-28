a = input()
b = input()
c = [i != j for i, j in zip(a, b)]

counter = 0
for i in range(len(c) - 1):
    if c[i]:
        counter += 1
        c[i] = not c[i]
        c[i + 1] = not c[i + 1]

print(counter)
