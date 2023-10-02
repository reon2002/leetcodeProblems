class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>0:
            if s.isspace() or len(s)==1:
                return 1
            else:
                res=""
                substrings=[]
                for i in range(len(s)):
                    for j in range(i,len(s)):
                        if s[j] not in res:
                            res+=s[j]
                        else:
                            substrings.append(res)
                            res=""
                            i=j-1
                            break
                largest=len(substrings[0])
                for i in substrings:
                    if len(i)>largest:
                        largest=len(i)
                return largest
        else:
            return 0