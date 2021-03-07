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
            if key < item.key:
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
