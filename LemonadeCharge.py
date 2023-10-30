class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billDict = {
            5 : 0,
            10 : 0,
            20 : 0
        }
        for i in bills:
            if i == 5:
                billDict[i] = billDict[i]+1
            elif i == 10:
                billDict[i] = billDict[i]+1
                billDict[5] = billDict[5]-1
            elif i == 20:
                billDict[i] = billDict[i]+1
                if (billDict[10] > 0) and (billDict[5] > 0):
                    billDict[10] = billDict[10]-1
                    billDict[5] = billDict[5]-1
                else:
                    billDict[5] = billDict[5]-3
            if min(billDict.values()) < 0:
                return False
        return True
