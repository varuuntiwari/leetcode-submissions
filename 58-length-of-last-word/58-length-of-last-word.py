class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        res = 0
        if " " not in s:
            return len(s)
        for i in range(len(s) - 1, 0, -1):
            if s[i] != " ":
                res += 1
            else:
                return res