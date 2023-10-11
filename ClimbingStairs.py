# This one works
class Solution:
    def climbStairs(self, n: int) -> int:
        this = 1
        last = 0
        for i in range(1, n+1):
            this_saved = last
            last = this
            this += this_saved
        return this



# this one "works", but it gets runtime Exeeded since it uses reccursion
class Solution:
    def addForTwos(self, n):
        if n > 1:
            return self.addForTwos(n-2) + self.addForOnes(n-1)
        return n
    
    def addForOnes(self, n):
        if n > 1:
            return self.addForOnes(n-1) + self.addForTwos(n-2)
        return n

    def climbStairs(self, n: int) -> int:
        if n == (1 or 2):
            return n
        n += 1
        total = 0
        total+=self.addForOnes(n-1)
        total+=self.addForTwos(n-2)
        return total
