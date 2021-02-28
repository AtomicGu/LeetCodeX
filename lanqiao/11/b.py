import re

state = 0
map_dict = {
    0: {
        "0": 0,
        "2": 1
    },
    1: {
        "0": 2,
        "2": 1
    },
    2: {
        "0": 0,
        "2": 3
    },
    3: {
        "0": 4,
        "2": 1
    },
    4: {
        "0": 0,
        "2": 3
    },
}
counter = 0


def transist(c):
    global state, counter
    t = map_dict[state][c]
    if state == 3 and t == 4:
        counter += 1
    state = t
    return


text = """220000
000000
002202
000000
000022
002020"""

mat = [i.strip() for i in text.split()]
w = len(mat[0])

for row in mat:
    state = 0
    for c in row:
        transist(c)

for i in range(w):
    state = 0
    for row in mat:
        transist(row[i])

h = len(mat)
for i in range(h):
    state = 0
    for j, k in zip(range(i, h), range(w)):
        transist(mat[j][k])
for i in range(1, w):
    state = 0
    for j, k in zip(range(h), range(i, w)):
        transist(mat[j][k])

print(counter)
