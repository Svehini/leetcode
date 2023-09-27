class Solution:
    def getLength(self, listStr):
        length = 0
        characters = []
        for char in listStr:
            if char not in characters:
                length+=1
                characters.append(char)
            else:
                return length
        return length

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lengthForEachChar = []
        for i in range(len(s)):
            lengthForEachChar.append(self.getLength(s[i:]))
        return max(lengthForEachChar)
