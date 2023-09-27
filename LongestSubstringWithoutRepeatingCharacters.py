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


# 2nd solution which is a little faster


class Solution:
    def getLength(self, first, listStr):
        listStr = listStr.split(first)
        for i in range(len(listStr)):
            string = list(dict.fromkeys(listStr[i]))
            if len(string) != len(listStr[i]):
                used_chars = []
                word = listStr[i]
                for n in range(len(word)):
                    if word[n] not in used_chars:
                        used_chars.append(word[n])
                    else:
                        listStr[i] = word[:n]
                        break
        for n in range(len(listStr)):
            listStr[n] = len(listStr[n])
        return (max(listStr)+1)

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lengthForEachChar = []
        used_char = []
        for i in range(len(s)):
            if s[i] not in used_char:
                used_char.append(s[i])
                lengthForEachChar.append(self.getLength(s[i], s[i:]))
        return max(lengthForEachChar)
