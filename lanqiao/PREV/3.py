from itertools import permutations

N = int(input())
n = len(str(N))

numbers = [chr(i) for i in range(ord("1"), ord("9") + 1)]

counter = 0
for comb in permutations(numbers, n):
    for i in range(1, n):
        a = "".join(comb[:i])
        a = int(a)
        if a >= N:
            break
        t = N - a
        for j in range(i + 1, 8):
            b = int("".join(comb[i:j]))
            c = int("".join(comb[j:]))
            if t * c == b:
                counter += 1

print(counter)
