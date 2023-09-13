class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)-1):
            for n in range(i+1,len(nums)):
                if (nums[i]+nums[n])==target:
                    indices.append(i), indices.append(n)
                    return indices
