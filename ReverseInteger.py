class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        minus = False
        x = str(x)
        if x[0] == "-":
            minus = True
            x = x.replace("-", "")
        x = x[::-1]
        if x[0] == "0":
            x = x[1:]
        if minus == True:
            x = "-"+x
        x = int(x)
        if (x > ((2**31)-1)) or (x < (-2**31)):
            return 0
        return x
