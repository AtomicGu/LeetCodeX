"""字符串匹配算法

巧妙处理了边界情况的代码，比原题解更好：
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0028.%E5%AE%9E%E7%8E%B0strStr.md
"""


def calc_next(needle) -> list[int]:
    """更好就体现在构造出的next表中

    next[i] 的含义是，当 needle[i] 匹配失败后，下一次该和 needle[next[i]] 匹配
    并且保证 needle[next[i]] != needle[i]

    比如对于 "aabaacaab"，原方法构建出的最后一个 b 处为 2，而我是 -1，省去了和第一个 b 作比较
    """
    next = [-1] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        if needle[i] == needle[j]:
            while True:
                k = next[j]
                if k == -1 or needle[i] != needle[k]:
                    break
            next[i] = k
        else:
            next[i] = j
            while True:
                j = next[j]
                if j == -1 or needle[i] == needle[j]:
                    break
        j += 1
    return next


def kmp(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    # 可选，不影响正确性，但可能会提高性能
    # if len(needle) > len(haystack):
    #     return -1

    next = calc_next(needle)
    j = 0
    for i in range(len(haystack)):
        while j != -1 and needle[j] != haystack[i]:
            j = next[j]
        j += 1
        if j == len(needle):
            break
    else:
        return -1
    return i - j + 1


print(kmp("hello", "ll"))
