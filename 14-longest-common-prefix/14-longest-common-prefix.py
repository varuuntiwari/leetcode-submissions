class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_lens = [len(x) for x in strs]
        res = ""
        for i in range(min(str_lens)):
            tmp = [strs[n][i] for n in range(len(strs))]
            if len(set(tmp)) == 1:
                res += strs[0][i]
            else:
                return res
        return res