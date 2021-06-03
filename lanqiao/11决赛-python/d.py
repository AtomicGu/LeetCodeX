mat = [[0 for j in range(40)] for i in range(40)]

counter = 1
for i in range(40):
    if i % 2 == 1:
        for j in range(i + 1):
            mat[j][i - j] = counter
            counter += 1
    else:
        for j in range(i, -1, -1):
            mat[j][i - j] = counter
            counter += 1

# for row in mat:
#     print(row)
print(mat[19][19])
