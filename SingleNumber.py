class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums))[::2]:
            try:
                if nums[i] != nums[i+1]:
                    return nums[i]
            except:
                return nums[i]
        return nums[0]
