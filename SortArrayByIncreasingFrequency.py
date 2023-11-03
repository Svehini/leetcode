class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countDict = {}
        for i in nums:
            if i not in countDict:
                countDict[i] = 1
            else: 
                countDict[i] = countDict[i] + 1
        countDict = dict(sorted(countDict.items(), key = lambda x:x[0], reverse = True))
        countDict = dict(sorted(countDict.items(), key = lambda x:x[1]))
        endList = []
        for key, value in countDict.items():
            endList.extend(repeat(key, value))
        return endList
