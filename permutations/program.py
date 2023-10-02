from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums)==0:
        #     return []
        # elif len(nums)==1:
        #     return nums
        # else:
        #     l=[]
        #     for i in range(len(nums)):
        #         m=nums[i]
        #         remList= nums[:i]+nums[i+1:]
        #         for p in permute(remList):
        #             l.append([m]+p)
        # return l
        l=list(permutations(nums))
        return l