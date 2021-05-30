from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        heap_free = [(servers[i], i) for i in range(len(servers))]
        heapify(heap_free)
        heap_busy = []

        task_i = 0
        now = 0
        ans = []
        while task_i < len(tasks):
            # 把完成任务的机器加入空闲堆
            while heap_busy:
                time, weight, index = heap_busy[0]
                if time <= now:
                    heappush(heap_free, (weight, index))
                    heappop(heap_busy)
                else:
                    break

            # 无空闲机器就推进时间
            if not heap_free:
                now = heap_busy[0][0]
                continue

            # 无可分配任务就推进时间
            if task_i > now:
                now = task_i
                continue

            # 从空闲堆中选一个
            weight, index = heappop(heap_free)
            ans.append(index)
            heappush(heap_busy, (now + tasks[task_i], weight, index))
            task_i += 1

        return ans
