# Code works, but time limit exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggestArea = 0
        biggestValue = max(height)
        usedBiggest = False
        for i in range(len(height)-1):
            if ((len(height)-i) * height[i]) > biggestArea:
                if usedBiggest == True:
                    thisArea = (BV-i) * min(height[BV], height[i])
                    if thisArea > biggestArea:
                        biggestArea = thisArea
                else:
                    for n in range(i,len(height)):
                        thisArea = (n-i) * min(height[n], height[i])
                        if thisArea >= biggestArea:
                            biggestArea = thisArea
                            print(f"Biggest area is {biggestArea}")
                            if height[n] == biggestValue:
                                print(f"Biggest: {biggestArea}, i: {i}, n: {n}")
                                BV = n
                                usedBiggest = True
                            else:
                                usedBiggest = False
        return biggestArea
