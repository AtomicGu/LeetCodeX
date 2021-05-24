import io
import sys

sys.stdin = io.StringIO(
    """3
2 2 4
"""
)

N = int(input())
nums = list(map(int, input().split()))

count = 0
while not all(map(lambda x: x == nums[0], nums)):
    nums[0] >>= 1
    add_to_last = nums[0]
    for i in range(1, len(nums)):
        nums[i] >>= 1
        nums[i - 1] += nums[i]
        if nums[i - 1] & 1:
            count += 1
            nums[i - 1] += 1
    nums[-1] += add_to_last
    if nums[-1] & 1:
        count += 1
        nums[-1] += 1

print(count)
