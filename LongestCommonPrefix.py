class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            for n in range(len(strs[:-1])):
                if strs[n][i] != strs[n+1][i]: #FIX THIS LINE
                    return prefix
            prefix+=strs[0][i]
        return prefix
