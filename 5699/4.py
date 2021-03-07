from typing import *


class Item:
    def __init__(self, obj, key, pos):
        self.obj = obj
        self.key = key  # 优先键值
        self.pos = pos  # 堆中位置
        return

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self) -> str:
        return f"<{self.key}:{self.obj} at {self.pos}>"


class HeapQueue:
    def __init__(self):
        self.heap = []
        self.map = {}
        return

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                parent.pos = pos
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
        newitem.pos = pos
        return

    def _siftup(self, pos):
        heap = self.heap
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        childpos = (pos << 1) + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            child = heap[childpos]
            heap[pos] = child
            child.pos = pos
            pos = childpos
            childpos = (pos << 1) + 1
        heap[pos] = newitem
        newitem.pos = pos
        self._siftdown(startpos, pos)
        return

    def __setitem__(self, obj, key):
        item = self.map.get(obj)
        if item is None:
            item = Item(obj, key, len(self.heap))
            self.heap.append(item)
            self.map[obj] = item
            self._siftdown(0, len(self.heap) - 1)
        else:
            if key == item.key:
                return
            if key < item.key:  # 由于Dij算法只会更新更小的值，这里还能优化！
                item.key = key
                self._siftdown(0, item.pos)
            else:
                item.key = key
                self._siftup(item.pos)
        return

    def __getitem__(self, obj):
        return self.map[obj].key

    def heappop(self):
        heap = self.heap
        lastelt = heap.pop()
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            self._siftup(0)
            return returnitem.obj, returnitem.key
        return lastelt.obj, lastelt.key


class Node:
    def __init__(self, index):
        self.tos = {}
        self.index = index
        self.dtln = None  # distanceToLastNode
        self.hfljs = None  # 合法路径数
        return

    def __repr__(self) -> str:
        return f"<{self.index}->{[i.index for i in self.tos]}>"

    def link(self, other, dist):
        self.tos[other] = dist
        other.tos[self] = dist
        return


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        nodes = [None] + [Node(i) for i in range(1, n + 1)]
        for fr, to, dist in edges:
            nodes[fr].link(nodes[to], dist)

        hq = HeapQueue()
        hq[nodes[n]] = 0
        while hq.heap:
            fr, dis = hq.heappop()
            fr.dtln = dis
            for to, dist in fr.tos.items():
                if to.dtln is None:
                    dist += dis
                    if to not in hq.map or hq[to] > dist:
                        hq[to] = dist

        nodes[1].hfljs = 1

        def hfljs(to=nodes[n]) -> int:
            """求点1到to的合法路径数
            """
            if to.hfljs is not None:
                return to.hfljs

            to.hfljs = 0
            for fr in to.tos:
                if fr.dtln > to.dtln:
                    to.hfljs += hfljs(fr)
            return to.hfljs

        return hfljs() % (10**9 + 7)


n = 10
edges = [
    [9, 10, 8],
    [9, 6, 5],
    [1, 5, 9],
    [6, 8, 10],
    [1, 8, 1],
    [8, 10, 7],
    [10, 7, 9],
    [5, 7, 3],
    [4, 2, 9],
    [2, 3, 9],
    [3, 10, 4],
    [1, 4, 7],
    [7, 6, 1],
    [3, 9, 8],
    [9, 1, 6],
    [4, 7, 10],
    [9, 4, 9],
]

sln = Solution()
ans = sln.countRestrictedPaths(n, edges)
print(ans)
