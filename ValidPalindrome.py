class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for letter in s:
            if letter.isalnum():
                new_str+=letter
        new_str = new_str.lower()
        s_rev = new_str[::-1]
        for i in range(len(new_str)):
            if new_str[i] != s_rev[i]:
                return False
        return True
