def up3(seq):
    arr = [0] * len(seq)
    for i in range(len(seq)):
        counter = 0
        for j in range(i + 1, len(seq)):
            if seq[j] > seq[i]:
                counter += 1
        arr[i] = counter

    total = 0
    for i in range(1, len(seq)):
        total += sum(arr[i:])
    return total


mat = [list(range(i, i + 9)) for i in range(9)]

for row in mat:
    up3(row)

for col in range(50):
    col = [i[col] for i in mat]
    up3(col)
