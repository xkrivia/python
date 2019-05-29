# CHRIS FELLI, 2019
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# nums = [2, 7, 11, 15], target = 9
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
from typing import List

class Solution:
    def __init__(self, nums=[], target=0):
        self.nums = nums
        self.target = target

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print(buff_dict)
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

test = Solution()
print(test.twoSum([1,2,3,4,5], 9))