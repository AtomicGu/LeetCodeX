def sort(x):
    counter = 0
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                counter += 1
                t = x[j]
                x[j] = x[j + 1]
                x[j + 1] = t
    return x, counter


print(sort(list(range(15, 0, -1))))
a = list(range(15, 6, -1)) + [1, 6, 5, 4, 3, 2]
print("".join([chr(ord("a") - 1 + i) for i in a]))
print(sort(a))
