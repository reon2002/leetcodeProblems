class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max=nums[0]
        dict={}
        for i in nums:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]+=1
        for key in dict.keys():
            if dict[key]>dict[max]:
                max=key
            else:
                continue
        return max