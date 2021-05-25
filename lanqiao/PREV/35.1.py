"""语法解析？！上 LL(1) ！
"""
string = input() + "$"
# string = "((xx|xxx)x|(x|xx))xx$"
p = 0


def S():
    global p
    c = string[p]

    if c == "x":
        p += 1
        return 1 + R()

    if c == "(":
        p += 1
        a = S()
        p += 1  # "|"
        b = S()
        p += 1  # ")"
        c = R()
        return max(a, b) + c

    print(string)
    print(" " * (p - 1), end="!\n")
    raise AssertionError()


def R():
    global p
    c = string[p]

    if c in "$|)":
        return 0

    if c in "x(":
        return S()

    print(string)
    print(" " * (p - 1), end="!\n")
    raise AssertionError()


print(S())
