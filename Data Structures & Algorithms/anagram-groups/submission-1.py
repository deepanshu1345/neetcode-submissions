class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            hash_map[key].append(s)
        
        res = []
        for item in hash_map.values():
            res.append(item)
        return res