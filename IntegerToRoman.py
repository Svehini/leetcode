class Solution:
    def intToRoman(self, num: int) -> str:
        romanDoubleNumbers = {
            "4" : "IV",
            "9" : "IX",
            "40" : "XL",
            "90" : "XC",
            "400" : "CD",
            "900" : "CM"
        }
        romanSingleNumbers = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }
        romanSingleRev = {
            1000 : "M",
            500 : "D",
            100 : "C",
            50 : "L",
            10 : "X",
            5 : "V",
            1 : "I"
        }

        romanNumber = ""
        numList = list(str(num))
        numberOfZeroes = len(numList)-1
        for siffer in numList:
            if (int(siffer) < 4):
                siffer += "0" * numberOfZeroes
                for num, roman in romanSingleRev.items():
                    if (int(siffer) / num) >= 1:
                        romanNumber += roman * int(int(siffer) / num)
                        break      
            elif (int(siffer) == 4) or (int(siffer) == 9):
                siffer += "0" * numberOfZeroes
                romanNumber += romanDoubleNumbers[siffer]
            else:
                siffer += "0" * numberOfZeroes
                siffer = int(siffer)
                for num, roman in romanSingleRev.items():
                    if (siffer / num) >= 1:
                        romanNumber += roman * int(siffer / num)
                        siffer -= (int(siffer / num) * num)
            numberOfZeroes -= 1
        return romanNumber
