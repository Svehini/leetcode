class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitDict = {}
        extras = []
        arr = sorted(arr)
        for num in arr:
            binNum = str(bin(num))
            numOf1 = len(binNum.split("1"))-1
            if num not in bitDict:
                bitDict[num] = numOf1
            else:
                extras.append(num)
        returnList = list(dict(sorted(bitDict.items(), key=lambda x:x[1])).keys())
        for i in extras:
            for n in range(len(returnList)):
                if i == returnList[n]:
                    returnList.insert(n,i)
                    break
        return returnList
