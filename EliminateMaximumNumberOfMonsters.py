class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        realDist = []
        elims = 0
        while dist != []:
            realDist.append(dist.pop(0) / speed.pop(0))
        realDist = sorted(realDist)
        print(realDist)
        for i in range(len(realDist)):
            if realDist[i] <= i:
                break
            else:
                elims += 1
        return elims
