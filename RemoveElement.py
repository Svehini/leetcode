class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[::-1]:
            if i == val:
                nums.remove(i)
        return len(nums)
