class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left == []:
            furthestToGoLeft = 0
        else:
            furthestToGoLeft = max(left)
        if right == []:
            furthestToGoRight = 0
        else:
            furthestToGoRight = n - min(right)
        return max(furthestToGoLeft, furthestToGoRight)
