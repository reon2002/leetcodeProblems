class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(len(nums)):
            
            if nums[i] not in dict.keys():
                key=nums[i]
                dict[key]=1
            else:
                dict[key]=dict[key]+1
        flag=0        
        for i in dict.values():
            if i>1:
                flag=1
                break
        if flag==0:
            return False
        else:
            return True