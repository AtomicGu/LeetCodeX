def calc_next(s: str) -> list[int]:
    next = [-1] * len(s)
    j = 0
    for i in range(1, len(s)):
        if s[i] == s[j]:
            next[i] = next[j]
        else:
            next[i] = j
            while True:
                j = next[j]
                if j == -1 or s[j] == s[i]:
                    break
        j += 1
    return j


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = calc_next(s)
        r = len(s) - j
        return len(s) % r == 0 and j != 0


sln = Solution()
print(sln.repeatedSubstringPattern("babbabbabbabbab"))
