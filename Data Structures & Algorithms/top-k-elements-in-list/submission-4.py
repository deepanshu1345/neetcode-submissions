class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        res = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        sor = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        for j, v in sor[:k]:
            res.append(j)
        return res