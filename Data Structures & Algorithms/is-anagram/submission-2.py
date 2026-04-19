class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = defaultdict()
        t_hash = defaultdict()

        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0)+ 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        
        for k, v in s_hash.items():
            t_val = t_hash.get(k)
            if v != t_val:
                return False
        return True