# string = "xx|xxxx|xxxxx$"

import sys

sys.setrecursionlimit(1000000)

string = input() + "$"
p = 0


def panic():
    print(string)
    print(" " * p, end="!\n")
    raise AssertionError()


def match(c):
    global p
    if string[p] != c:
        panic()
    p += 1
    return


def P0() -> int:
    global p
    c = string[p]

    if c in "x":
        p += 1
        return 1

    if c in "(":
        p += 1
        a = S()
        match(")")
        return a

    panic()


def P1() -> int:
    global p
    c = string[p]

    if c in "x(":
        a = P0()
        return A(a)

    panic()


def A(i0: int) -> int:
    global p
    c = string[p]

    if c in "x(":
        a = P1()
        return A(i0 + a)

    if c in "|$)":
        return i0

    panic()


def P2() -> int:
    global p
    c = string[p]

    if c in "x(":
        a = P1()
        return B(a)

    panic()


def B(i0: int) -> int:
    global p
    c = string[p]

    if c in "|":
        p += 1
        a = P2()
        b = B(a)
        return max(i0, b)

    if c in "$)":
        return i0

    panic()


def S() -> int:
    global p
    c = string[p]

    if c in "x(":
        return P2()

    panic()


print(S())

# 奇怪，怎么还过不了？
