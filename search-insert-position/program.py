class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=len(nums)
        if target<nums[0]:
            ans=0
        elif target in nums:
            ans= nums.index(target)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    ans= i+1
                    break
        return ans