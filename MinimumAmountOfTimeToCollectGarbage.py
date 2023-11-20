class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        gLast = 0
        pLast = 0
        mLast = 0
        totalTime = 0

        for i in range(len(garbage)):
            if "G" in garbage[i]:
                gLast = i
            if "P" in garbage[i]:
                pLast = i
            if "M" in garbage[i]:
                mLast = i
            totalTime += len(garbage[i])

        totalTime += sum(travel[:gLast]) + sum(travel[:pLast]) + sum(travel[:mLast])

        return totalTime
