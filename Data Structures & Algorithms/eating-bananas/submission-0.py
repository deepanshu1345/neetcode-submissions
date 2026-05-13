import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high 
        while low <= high:
            mid = low + (high - low) // 2

            total = 0 
            for i in piles:
                total += math.ceil(i / mid)
            
            if total <= h:
                high = mid - 1
                res = mid
            else:
                low = mid +1 
        return res
                