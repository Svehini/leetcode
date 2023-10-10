class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for k in range(n):
            nums1.pop()
        for i in nums2:
            smaller = "NA"
            bigger = "NA"
            for j in range(len(nums1)):
                if i < nums1[j]:
                    smaller = j
                elif i > nums1[j]:
                    bigger = j
            if smaller == "NA":
                nums1.insert(len(nums1), i)
            elif bigger == "NA":
                nums1.insert(0, i)
            else:
                nums1.insert(bigger+1, i)
