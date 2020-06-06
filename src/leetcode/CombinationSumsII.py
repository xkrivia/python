# CHRIS FELLI, 2019
# Given a list of integers and a target integer,
# Return a list of lists of numbers that add up to the target
from typing import List


class Solution:
    def __init__(self, candidates=[], target=0):
        self.candidates = candidates
        self.target = target

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    # Helper
    def combine_sum_2(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.combine_sum_2(nums, i + 1, path + [nums[i]],
                               result, target - nums[i])


# Driver
test = Solution()
print(test.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
