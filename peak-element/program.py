class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak=nums[0]
        id=0
        for i in range(len(nums)):
            if(peak<nums[i]):
                peak=nums[i]
                id=i
        return id