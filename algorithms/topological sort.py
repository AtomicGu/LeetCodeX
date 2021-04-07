"""拓扑排序
"""

from collections import deque

from gte import input_graph

graph = input_graph(True)

q = deque()

for i in graph:
    if len(i.frs) == 0:
        q.append(i)

ans = []

while q:
    p = q.popleft()
    ans.append(p)
    for to in list(p.tos):
        p.unlink_to(to)
        if len(to.frs) == 0:
            q.append(to)

if len(ans) != len(graph):
    print("有环")

print([i.index for i in ans])
