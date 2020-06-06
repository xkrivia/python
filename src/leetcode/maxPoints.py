# CHRIS FELLI, 2019
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
from typing import List

# NAIVE:
# If only one point, ignore it
# For second and onward points, compare slope to previous points

# TODO


class Solution:
    def __init__(self, points: List[List[int]]=0):
        self.points = points

    def maxPoints(self, points: List[List[int]]) -> int:
        maxLen = List[int]
        if len(points) == 1:
            return -1
        for i in range(len(points)):
            print(points[i])


# Testcases
test = Solution()
print(test.maxPoints([[1, 1], [1, 1]]))
print(test.maxPoints([[1, 1], [2, 2]]))
