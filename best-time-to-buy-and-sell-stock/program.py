class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        lowest=prices[0]
        for i in range(len(prices)):
            lowest=min(prices[i],lowest)
            diff=prices[i]-lowest
            res=max(diff,res)
        return res