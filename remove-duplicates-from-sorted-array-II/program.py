class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]=dict[i]+1
        for i in dict.keys():
            if dict[i]>2:
                dict[i]=2
        nums.clear()
        for key in dict.keys():
            for i in range(dict[key]):
                nums.append(key)
        return len(nums)
        
