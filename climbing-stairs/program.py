class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==0 or n==1:
        #     return 1
        # else
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        a,b=0,1
        for i in range(n):
            a,b= b,a+b
        return b