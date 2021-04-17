# import io
# import sys
#
# sys.stdin = io.StringIO("""4 4
# 1 2
# 2 3
# 3 1
# 1 4
# """)

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

counter = 0
for a in range(1, N + 1):
    for b in graph[a]:
        # a->b方向
        for c in graph[b]:
            if c == a:
                continue
            counter += len(graph[c]) - 1

        # b->a方向
        # for c in graph[a]:
        #     if c == b:
        #         continue
        #     counter += len(graph[c]) - 1

print(counter)
