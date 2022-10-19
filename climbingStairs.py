import math

class Solution:
    def climbStairs(self, n: int) -> int:
        res: int = 0

        for i in range(n, -1, -2):
            b: int = int((n - i) / 2) 
            res += math.comb(i + b, b)

        return res

print(Solution().climbStairs(5))
