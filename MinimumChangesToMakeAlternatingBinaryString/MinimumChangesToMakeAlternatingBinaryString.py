class Solution:
    def minOperations(self, s: str) -> int:
        res1, res2 = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    res1 += 1
                else:
                    res2 += 1
            else:
                if s[i] == '0':
                    res2 += 1
                else:
                    res1 += 1
        return min(res1, res2)
