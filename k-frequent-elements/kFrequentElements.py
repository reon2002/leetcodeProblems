class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def getKey(val):
            for key,value in dict.items():
                if value==val:
                    return key
        dict=Counter(nums)
        l=sorted(dict.values(),reverse=True)
        res=[]
        for i in range(len(l)):
            res.append(getKey(l[i]))
            dict.pop(getKey(l[i]))
        return res[0:k]