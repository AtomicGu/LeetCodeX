class Solution:
    def __init__(self):
        self.normal = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        self.unormal = {
            "I": {
                "V": 4,
                "X": 9
            },
            "X": {
                "L": 40,
                "C": 90
            },
            "C": {
                "D": 400,
                "M": 900
            },
        }
        return

    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            un = self.unormal.get(c)
            if un is not None and i + 1 < len(s):
                c2 = un.get(s[i + 1])
                if c2 is not None:
                    num += c2
                    i += 2
                    continue
            num += self.normal[c]
            i += 1
        return num


sln = Solution()
ans = sln.romanToInt("IV")
print(ans)
