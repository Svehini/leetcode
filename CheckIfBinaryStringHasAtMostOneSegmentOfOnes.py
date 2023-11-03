class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first = s[0]
        for i in range(1,len(s)):
            if s[i] != first:
                for j in range(i,len(s)):
                    if s[j] == first:
                        return False
                return True
        return True
