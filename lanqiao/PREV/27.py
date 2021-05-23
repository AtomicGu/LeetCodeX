n = int(input())

pos = list(map(int, input().split()))

a = pos[0]

if a > 0:
    count = 1
    for i in pos:
        if i < 0 and -i > a:
            count += 1

    if count != 0:
        for i in pos:
            if i > 0 and i < a:
                count += 1

else:
    count = 1
    for i in pos:
        if i > 0 and i < -a:
            count += 1

    if count != 0:
        for i in pos:
            if i < 0 and -i > -a:
                count += 1

print(count)
