class Solution:

    def traverser(self, root):
        traversed = []
        if root:
            traversed.append(root.val)
            traversed = traversed + self.traverser(root.left)
            traversed = traversed + self.traverser(root.right)
        return traversed

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        traversed = self.traverser(root)

        countDict = {}
        for i in traversed:
            if i not in countDict:
                countDict[i] = 1
            else:
                countDict[i] = countDict[i]+1

        mostOccurs = []
        mostOccursInt = 0
        for key, value in countDict.items():
            if value > mostOccursInt:
                mostOccurs = [key]
                mostOccursInt = value
            elif value == mostOccursInt:
                mostOccurs.append(key)

        return mostOccurs
