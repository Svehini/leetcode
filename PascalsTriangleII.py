class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        lastRow = [1,1]
        newRow = []
        for i in range(1, rowIndex):
            newRow = []
            n=0
            while n+1 <= len(lastRow)-1:
                newRow.append(lastRow[n]+lastRow[n+1])
                n+=1
            newRow.insert(0, 1)
            newRow.insert(len(newRow), 1)
            lastRow = newRow
        return newRow
