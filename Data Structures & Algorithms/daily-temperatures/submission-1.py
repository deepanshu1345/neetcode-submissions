class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prv_index = stack.pop()
                res[prv_index] = i - prv_index
            stack.append(i)

        return res