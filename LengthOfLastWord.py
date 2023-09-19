class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = (s.split(" "))[::-1]
        for word in s_list:
            if word != '':
                return len(word)
