class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        checkDict = {}
        outputList = []
        nums1 = list(dict.fromkeys(nums1)) + list(dict.fromkeys(nums2))+ list(dict.fromkeys(nums3))
        for i in nums1:
            if i not in checkDict:
                checkDict[i] = 1
            else:
                outputList.append(i)
        return list(dict.fromkeys(outputList))
