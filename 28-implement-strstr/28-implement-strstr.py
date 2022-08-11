class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        if needle == haystack:
            return 0
        elif needle not in haystack:
            return -1
        for x in range(len(haystack) - len_needle + 1):
            if haystack[x:x+len_needle] == needle:
                return x