class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = True
        x_str = str(x)
        x_list = list(x_str.strip())
        y_list = x_list[::-1]
        if x_list != y_list:
            isPalindrome = False
        return isPalindrome
