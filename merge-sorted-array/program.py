class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1=[]
        for i in range(m):
            n1.append(nums1[i])
        for j in range(n):
            n1.append(nums2[j])
        nums1.clear()
        n1.sort()
        for i in range(len(n1)):
            nums1.append(n1[i])