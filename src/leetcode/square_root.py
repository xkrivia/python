import math

class Solution:
    def mySqrt(self, x):
        if isinstance(math.sqrt(x), int) is True:
            return math.sqrt(x)
        else:
            return math.floor(math.sqrt(x))


def test_four():
    assert Solution().mySqrt(4) == 2


def test_eight():
    assert Solution().mySqrt(8) == 2
