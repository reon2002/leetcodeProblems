class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                s1=s1+i
            else:
                continue
        s1=s1.lower()
        pal=s1[::-1]
        if s1==pal:
            return True
        else:
            return False