class Solution:

    def palindromeFinder(self, s, first, last):
        usedLetters = []
        total = 0
        for letter in range(first+1,last):
            if (s[letter] not in usedLetters): 
                usedLetters.append(s[letter])
                total += 1
        return total

    def countPalindromicSubsequence(self, s: str) -> int:
        usedFirst = []
        total = 0
        potentialPalindrome = True
        for letter in range(len(s)):
            if (s[letter] not in usedFirst):
                last = len(s)-1
                while s[last] != s[letter]:
                    if letter == last:
                        potentialPalindrome = False
                        break
                    last -= 1
                if potentialPalindrome == True:
                    total += self.palindromeFinder(s, letter, last)
                    usedFirst.append(s[letter])
        
        return total
