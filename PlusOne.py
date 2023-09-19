class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        digits_reverse = digits[::-1]
        for i in range(len(digits_reverse)):
            if digits_reverse[i] == 9:
                digits_reverse[i] = 0
                if i == len(digits_reverse)-1:
                    digits_reverse.append(1)
            else:
                digits_reverse[i]+=1
                break
        return digits_reverse[::-1]
