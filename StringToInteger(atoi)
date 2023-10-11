class Solution:

    def intMaker(self, liste, negative):
        if liste == []:
            return 0
        if negative == True:
            liste.insert(0, "-")
        string = "".join(liste)
        integer = int(string)
        if integer > (2**31)-1:
            return (2**31)-1
        elif integer < -2**31:
            return -2**31
        else: 
            return integer

    def myAtoi(self, s: str) -> int:
        finalInteger = []
        digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        negative = False
        char_read = False
        for letter in s:
            if letter != " ":
                if letter in digit_list:
                    finalInteger.append(letter)
                elif char_read == True:
                    return self.intMaker(finalInteger, negative)
                elif letter == "-":
                    negative = True
                elif letter != "+":
                    return self.intMaker(finalInteger, negative)
                char_read = True
            elif char_read == True:
                return self.intMaker(finalInteger, negative)
        return self.intMaker(finalInteger, negative)
