class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S,T  = list(s),list(t)
        S.sort()
        T.sort()
        if  S==T:
            return True
        else:
            return False