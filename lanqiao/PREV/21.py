n = int(input())

r5 = []
r6 = []

for a in range(1, 10):
    for b in range(10):
        c = n - 2 * (a + b)
        if c >= 20 or c < 0:
            continue
        if c < 10:
            r5.append(f"{a}{b}{c}{b}{a}")
        c, d = divmod(c, 2)
        if d == 0:
            r6.append(f"{a}{b}{c}{c}{b}{a}")

results = r5 + r6
if not results:
    print(-1)
for i in results:
    print(i)
