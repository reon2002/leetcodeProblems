class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        k=0
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]]=dict[nums[i]]+1
            else:
                dict[nums[i]]=1
        for key,value in dict.items():
            if value==1:
                k=key
        return k