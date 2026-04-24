class Solution:
    def trap(self, height: List[int]) -> int:
        l_arr = []
        r_arr = []
        min_lr = []
        res = []
        temp = 0
        for i in height:
            temp = max(temp, i)
            l_arr.append(temp)
        temp = 0
        for i in height[::-1]:
            temp = max(temp, i)
            r_arr.append(temp)
        r_arr.reverse()
        for i in range(len(height)):
            min_lr.append((min(l_arr[i], r_arr[i])))
        for i in range(len(height)):
            subb = min_lr[i] - height[i]
            if subb > 0:
                res.append(subb)
            elif subb <= 0:
                res.append(0)
        return sum(res)