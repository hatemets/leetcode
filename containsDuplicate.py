from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visitedVals = set()

        for n in nums:
            if n in visitedVals:
                return True
            else:
                visitedVals.add(n)

        return False


print(Solution().containsDuplicate([1,2,3,9,4,6,5,7,8,10,43]))
