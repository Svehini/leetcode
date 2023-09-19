class Solution:
    def check_rest(self, haystack, needle):
        needle_len = len(needle)
        n = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[n]:
                n+=1
                if (n+1) > needle_len:
                    return True
            else:
                return False

    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        first_occur = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                first_occur = i
                if self.check_rest(haystack[i:], needle):
                    return first_occur
        return -1
