class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a += "0" * (len(b) - len(a))
        elif len(b) < len(a):
            b += "0" * (len(a) - len(b))
        ab_sum_rev = ""
        carry = False
        for i in range(len(a)):
            if (a[i] == "0") and (b[i] == "0"):
                if carry == True:
                    ab_sum_rev += "1"
                    carry = False
                else:
                    ab_sum_rev += "0"

            elif (a[i] == "1") and (b[i] == "1"):
                if carry == True:
                    ab_sum_rev += "1"
                else:
                    ab_sum_rev += "0"
                    carry = True

            else:
                if carry == True:
                    ab_sum_rev += "0"
                    carry = True
                else:
                    ab_sum_rev += "1"
                    carry = False
        
        if carry == True:
            ab_sum_rev += "1"    
        return ab_sum_rev[::-1]
