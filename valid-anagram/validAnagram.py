class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1
        # s_dict={}
        # for i in s:
        #     if i not in s_dict.keys():
        #         s_dict[i]=1
        #     else:
        #         s_dict[i]+=1
        # t_dict={}
        # for i in t:
        #     if i not in t_dict.keys():
        #         t_dict[i]=1
        #     else:
        #         t_dict[i]+=1
        # return s_dict==t_dict
        
        #method 2
        s_dict,t_dict=Counter(s),Counter(t)
        return s_dict==t_dict
        