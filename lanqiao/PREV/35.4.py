string = input() + "$"
p = 0


def find_max_length():
    global p
    c = string[p]

    length = 0
    while c != "$":
        if c == "x":
            p += 1
            length += 1
        if c == "(":
            p += 1
            length += find_max_length()
        if c == ")":
            p += 1
            return length
        if c == "|":
            p += 1
            length = max(length, find_max_length())
        c = string[p]
    return length


print(find_max_length())
