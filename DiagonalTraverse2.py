class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        newDict = {}
        newList = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j not in newDict:
                    newDict[i+j] = [nums[i][j]]
                else:
                    newDict[i+j].append(nums[i][j])
        for i in newDict:
            newList.extend(newDict[i][::-1])
        return newList
