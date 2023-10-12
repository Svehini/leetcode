class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        biggestArea = 0
        while right > left:
            thisArea = (right - left) * min(height[left], height[right])
            if thisArea > biggestArea:
                biggestArea = thisArea 
            if height[left] > height[right]:
                right-=1
            else:
                left +=1
        return biggestArea
