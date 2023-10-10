class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        triangle = [[1], [1,1]]
        for i in range(1, numRows-1):
            newRow = []
            lastRow = triangle[-1]
            n=0
            while n+1 <= len(lastRow)-1:
                newRow.append(lastRow[n]+lastRow[n+1])
                n+=1
            newRow.insert(0, 1)
            newRow.insert(len(newRow), 1)
            triangle.append(newRow)
        return triangle
