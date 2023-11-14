class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        first = 1
        seccond = 1
        third = 0
        i = 3
        total = 0
        while i <= n:
            total = first + seccond + third
            third = seccond
            seccond = first
            first = total
            i+=1
        return total
