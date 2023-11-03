class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        minimum = max(nums[0])
        for lists in nums:
            maximum = max(lists)
            if maximum < minimum:
                minimum = maximum
        returnList = []
        i = 0
        while (i < minimum) or ([] not in nums):
            inAll = True
            for item in nums:
                if i not in item:
                    inAll = False
                    break
                else:
                    item.remove(i)
            if inAll == True:
                returnList.append(i)
            i+=1
        return returnList
