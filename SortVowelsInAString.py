class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [
            "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
        ]
        s = list(s)
        vowelsInString = []
        newS = []
        while s != []:
            last = s.pop(-1)
            if last in vowels:
                vowelsInString.append(last)
                newS.append("#")
            else:
                newS.append(last)

        vowelsInString = sorted(vowelsInString)[::-1]

        while newS != []:
            last = newS.pop(-1)
            if last == "#":
                s.append(vowelsInString.pop(-1))
            else:
                s.append(last)
        
        return "".join(s)
