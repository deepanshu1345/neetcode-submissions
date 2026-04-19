class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            hash_set[i] = 1 + hash_set.get(i, 0)
        for n, c in hash_set.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res