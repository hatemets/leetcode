# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        m: int = int((l + r) / 2)
        prev: bool = False
        pm: int = -1

        while l < r:
            if m == pm:
                m -= 1

            if abs(pm - m) == 1 and not isBadVersion(m) and prev:
                return pm
            elif abs(pm - m) == 1 and isBadVersion(m) and not prev:
                return m
            elif isBadVersion(m):
                r = m
            else:
                l = m

            prev, pm = isBadVersion(m), m
            m = int((l + r) / 2) + 1

        return m

sol = Solution()
print(sol.firstBadVersion(100000))
