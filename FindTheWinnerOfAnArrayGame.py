class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        first = arr[0]
        seccond = arr[1]
        conWins = 0
        lastWon = ""
        biggest = max(arr)
        while conWins < k:
            if first > seccond:
                arr.pop(1)
                arr.append(seccond)
                seccond = arr[1]
                conWins += 1
                if first == biggest:
                    return biggest
            elif first < seccond:
                arr.pop(0)
                arr.append(first)
                first = arr[0]
                seccond = arr[1]
                conWins = 1
        return first
