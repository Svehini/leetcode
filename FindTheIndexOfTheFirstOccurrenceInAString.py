class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_list = haystack.split(needle)
        if haystack_list[0] == "":
            return 0
        elif len(haystack_list) > 1:
            return len(haystack_list[0])
        else:
            return -1

