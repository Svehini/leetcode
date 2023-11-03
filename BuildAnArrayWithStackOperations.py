class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        lastNum = 1
        stack = []
        while i <= max(target):
            if stack == target:
                break
            stack.append("Push")
            lastNum = i
            if lastNum not in target:
                stack.append("Pop")
            i+=1
        return stack
