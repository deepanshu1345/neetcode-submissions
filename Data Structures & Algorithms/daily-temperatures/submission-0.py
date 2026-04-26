class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp =temperatures
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temp[j] > temp[i]:
                    sub = j-i
                    res[i] = sub
                    break
        return res
