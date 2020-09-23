class Solution:
    def maxArea(self, height):
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area_tracker = (j - i) * min(height[i], height[j])
            if area_tracker >= area:
                area = area_tracker
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


def test_one():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

