class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        totalOperations = 0
        nums.sort()
        numberOfBigger = 0
        last = nums[0]
        first = nums[0]
        for num in nums:
            if num > first:
                if num > last:
                    last = num
                    numberOfBigger += 1
                    totalOperations += numberOfBigger

                else:
                    totalOperations += numberOfBigger
        return totalOperations
