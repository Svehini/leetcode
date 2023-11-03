class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterList = []
        for i in nums1:
            foundSame = False
            added = False
            for j in nums2:
                if i == j:
                    foundSame = True
                if foundSame == True:
                    if i < j:
                        nextGreaterList.append(j)
                        added = True
                        break
            if added == False:
                nextGreaterList.append(-1)
        return nextGreaterList
