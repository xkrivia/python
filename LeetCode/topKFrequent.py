# CHRIS FELLI, 2019
# Given a non-zero array, return the K most frequent elements.
# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input: nums = [1], k = 1
# Output: [1]
from typing import List

class Solution:
    def __init__(self, nums=[], k=0):
        self.nums = nums
        self.k = k

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            if nums[i] in dic:
                dic[nums[i]] += 1
        final = [int] * k
        for j in range(k):
            bigkey=max(dic, key=dic.get)
            final[j]=bigkey
            del dic[bigkey]
        return final

test = Solution()
print(test.topKFrequent([1,1,1,2,3], 2))
print(test.topKFrequent([1], 1))