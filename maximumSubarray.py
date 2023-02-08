from typing import List

class Solution:
    def maxSubArray(self, vals: List[int]) -> int:
        if len(vals) == 0:
            return 0
        elif len(vals) == 1:
            return vals[0]

        res = vals[0]
        l = 0
        r = 1
        curr = 0
        newCurr = True

        while r < len(vals):
            if newCurr:
                curr = vals[l] + vals[r]
                newCurr = False
            else:
                curr += vals[r]

            res = max(curr, res)

            if curr < vals[r]:
                l = r
                if vals[l] > res:
                    res = vals[l]
                newCurr = True

            print(l, r, curr)
            r += 1

        return res




# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1, -5, 4]))
# print(Solution().maxSubArray([5,4,-1,7,8]))
print(Solution().maxSubArray([-2, 1]))

