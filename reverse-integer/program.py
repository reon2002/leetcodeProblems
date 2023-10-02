class Solution:
    def reverse(self, x: int):
        res=0
        s=""
        rev=""
        flag=True
        if x<0 and x>=pow(-2,31):
            rev=str(x)
            rev=rev[1:]
            s="-"+rev[::-1]
            res=int(s)
        elif x>0 and x<pow(2,31):
            rev=str(x)
            s=rev[::-1]
            res=int(s)
        if res not in range(pow(-2,31),pow(2,31)):
            res=0
        return res