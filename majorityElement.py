from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        num, count = sortedNums[0], 0
        res, resCount = sortedNums[0], 0
        print(sortedNums)

        for i in range(len(nums)):
            if i < len(nums) - 1 and sortedNums[i] != sortedNums[i + 1]:
                num = sortedNums[i + 1]
                count = 1
            elif i < len(nums) - 1:
                count += 1

            if count > resCount:
                res = num
                resCount = count


        return res



# print(Solution().majorityElement([2,2,1,1,1,2,2]))
# print(Solution().majorityElement([1,1,1,1,3,3,1,3,3,3,1]))
print(Solution().majorityElement([1]))
