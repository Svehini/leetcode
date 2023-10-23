import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:
            return False
        return (log(n) / log(4)).is_integer() 

# Another way to do it, but using a while loop

#        if n == 1:
#            return True
#        else:
#            i = 0
#            while 4**i <= n:
#                if 4**i == n:
#                    return True
#                i+=1
#        return False
