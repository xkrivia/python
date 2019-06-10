# CHRIS FELLI, 2019
from typing import List

class Solution:
    def __init__(self, height=[]):
        self.height = height

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        water = 0
        # Start with outermost points, work your way towards the middle
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

# Driver
test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))