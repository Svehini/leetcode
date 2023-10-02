class Solution:

    def checker(self, listOfWords):
        listOfWords = sorted(listOfWords, key = len)
        listOfWords = listOfWords[::-1]
        for w in range(len(listOfWords)):
            returning = True
            word = listOfWords[w]
            rev_word = word[::-1]
            for letter in range(len(word)):
                if word[letter] != rev_word[letter]:
                    returning = False
                    break
            if returning == True:
                return word
        return ""

    def getWords(self, listOfWords):
        listOfWords = sorted(listOfWords, key = len)
        listOfWords = listOfWords[::-1]
        words = []
        for string in listOfWords:
            first = string[0]
            for i in range(1, len(string)):
                if string[i] == first:
                    if string[:i] != "":
                        words.append((string[:i+1]))
        if words != []:
            return self.checker(words)
        else:
            return first
        

    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        if len(s) == 1:
            return s
        allPalindromes = []
        allPossibilities = []
        for letter in range(len(s)):
            allPossibilities.append(s[letter:])
        longestPalindrome = (self.getWords(allPossibilities))
        if longestPalindrome == "":
            return s[0]
        return longestPalindrome
