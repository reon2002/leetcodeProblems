class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setnum=set(nums)
        i=1
        while i in setnum:
            i=i+1
        return i