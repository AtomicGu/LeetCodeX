from typing import Set
from itertools import combinations, product


class Node:
    def __init__(self, char: str) -> None:
        self.char = char
        self.edges: Set[Node] = set()
        return

    def link(self, other: "Node") -> None:
        self.edges.add(other)
        other.edges.add(self)
        return

    def __repr__(self) -> str:
        return "<Node char={} links={}>".format(self.char,
                                                [i.char for i in self.edges])


# 1
n, m = [int(i) for i in input().split()]

nodes = [Node(i) for i in input().strip()]

for i in range(m):
    a, b = [int(i) - 1 for i in input().split()]
    nodes[a].link(nodes[b])

# 2
nodes_c = []
nodes_s = []
nodes_p = []
for i in nodes:
    if i.char == "C":
        nodes_c.append(i)
    elif i.char == "S":
        nodes_s.append(i)
    elif i.char == "P":
        nodes_p.append(i)

# 3
counter = 0


def count_ccsp(a, b, c, d):
    def has_loop(a: Node, b: Node, c: Node) -> bool:
        return a in b.edges and b in c.edges and c in a.edges

    def foo(a, b, c, d) -> None:
        global counter
        counter += (a in d.edges) + (b in d.edges) + (c in d.edges)
        return

    if has_loop(a, b, c):
        foo(a, b, c, d)
    if has_loop(a, b, d):
        foo(a, b, d, c)
    if has_loop(a, c, d):
        foo(a, c, d, b)
    if has_loop(b, c, d):
        foo(b, c, d, a)
    return


for (c1, c2), s, p in product(combinations(nodes_c, 2), nodes_s, nodes_p):
    count_ccsp(c1, c2, s, p)

print(counter)
