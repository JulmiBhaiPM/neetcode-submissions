class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tup=tuple(s)
        t_tup=tuple(t)
        d=0
        if len(s_tup) == len(t_tup) :
            for i in s_tup:
                for j in t_tup:
                    if i == j :
                        d=d+1
                        break
            if d == len(s_tup):
                return True
            else :
                return False
        else:
            return False
        