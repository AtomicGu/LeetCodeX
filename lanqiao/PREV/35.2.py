string = "xx|xxx$"  # 这样设计的语法，或运算和连接变成同级运算符了（左结合）
p = 0


def panic():
    print(string)
    print(" " * (p - 1), end="!\n")
    raise AssertionError()


def S() -> int:
    global p
    c = string[p]

    if c in "x":
        p += 1
        return B(1)

    if c in "(":
        p += 1
        a = S()
        p += 1  # ")"
        return B(a)

    panic()


def A(i0: int) -> int:
    global p
    c = string[p]

    if c in "x(":
        a = S()
        return i0 + a

    if c in "|":
        p += 1
        a = S()
        return max(i0, a)

    panic()


def B(i0) -> int:
    global p
    c = string[p]

    if c in "x(|":
        a = A(i0)
        return B(a)

    if c in "$)":
        return i0

    panic()


print(S())
