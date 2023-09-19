class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_index = nums[0]
        for i in nums[1:]:
            if i == last_index:
                nums.remove(i)
            last_index = i
        return len(nums)
