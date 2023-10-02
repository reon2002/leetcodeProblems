class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)
        if nums1==[]:
            merged=nums2
        elif nums2==[]:
            merged=nums1
        else:
            merged=nums1+nums2
        merged.sort()
        # if (l1+l2)%2==1:
        #     res= merged[int(l1+l2/2)-1]
        #     return float(res)
        # elif (l1+l2)%2==0:
        #     halfSize=int(l1+l2/2)-1
        #     first=merged[halfSize-1]
        #     second=merged[halfSize]
        #     res=(first+second)/2
        #     return float(res)
        return statistics.median(merged)
