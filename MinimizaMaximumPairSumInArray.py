class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        summedList = []
        nums = sorted(nums)
        mid = len(nums) // 2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        nums1 = nums1[::-1]
        while nums1 != []:
            summedList.append(nums1.pop(-1) + nums2.pop(-1))
        return max(summedList)
