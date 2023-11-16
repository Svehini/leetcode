class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        returnedBinary = ""
        i = 0
        while nums != []:
            last = nums.pop(0)[i]
            if last == "0":
                returnedBinary += "1"
            else:
                returnedBinary += "0"
            i += 1
        return returnedBinary
            
#        returnedBinary = ""
#        for i in range(len(nums)):
#            thisNum = nums[i]
#            if thisNum[i] == "0":
#                returnedBinary += "1"
#            else:
#                returnedBinary += "0"
#        return returnedBinary
