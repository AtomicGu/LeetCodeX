from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = height
        lh = len(h)

        if h[0] > h[1]:
            a, b = 0, 1
        else:
            a, b = 1, 0

        for i in range(2, lh):
            if h[i] > h[a]:
                b = a
                a = i
            elif h[i] > h[b]:
                b = i

        if a < b:
            now_left, now_right = a, b
        else:
            now_left, now_right = b, a

        now_val = (now_right - now_left) * min(h[now_left], h[now_right])
        left = now_left
        right = now_right
        while True:
            if left == 0:
                if right == lh - 1:
                    break
                flag = True  # 向右扩展
            elif right == lh - 1:
                flag = False
            else:
                flag = h[left] < h[right]
            if flag:
                val = (right - left) * min(h[left], h[right])
                if val > now_val:
                    now_val = val
                    now_left = left
                    now_right = right
            else:
                val = 
        return now_val


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sln = Solution()
ans = sln.maxArea(height)
print(ans)
