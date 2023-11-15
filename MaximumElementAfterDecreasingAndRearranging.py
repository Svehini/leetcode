class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        if arr[0] != 1:
            arr.pop(0)
            arr.insert(0,1)
        first = 0
        for i in range(1,len(arr)):
            seccond = i
            if (arr[seccond] - arr[first]) > 1:
                arr.pop(i)
                arr.insert(i, arr[first]+1)
            first = seccond
        return arr[-1]
