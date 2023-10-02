class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for nums in nums:
            xor=xor^nums
        return xor
    