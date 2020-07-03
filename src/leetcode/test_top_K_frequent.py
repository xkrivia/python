from typing import List


class Solution:
    def __init__(self, nums=[], k=0):
        self.nums = nums
        self.k = k

    def top_K_frequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            if nums[i] in dic:
                dic[nums[i]] += 1
        final = [int] * k
        for j in range(k):
            bigkey = max(dic, key=dic.get)
            final[j] = bigkey
            del dic[bigkey]
        return final


def test_top_K_frequent():
    test = Solution()
    test.top_K_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    test.top_K_frequent([1], 1)
