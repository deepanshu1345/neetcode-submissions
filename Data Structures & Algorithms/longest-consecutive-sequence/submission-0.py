class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        count = 1
        maxi = 0
        for i in range(0, len(num)):
            if num[i] - num[i-1] == 1:
                count += 1
            else:
                count = 1
            maxi = max(count, maxi)

        return maxi