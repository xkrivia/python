class Solution:
    def reverse(self, x: int) -> int:
        x = Solution().range_check(x)
        solution = 0
        if x < 0:
            rev = str(abs(x))[::-1]
            solution = Solution().range_check(int(rev))
            return 0 - solution
        else:
            rev = str(x)[::-1]
            solution = Solution().range_check(int(rev))
            return solution

    def range_check(self, x: int) -> int:
        if x not in range(-2**31, 2**31 - 1):
            x = 0
            return x
        else:
            return x

def test_one():
    assert Solution().reverse(123) == 321

def test_two():
    assert Solution().reverse(-123) == -321

def test_three():
    assert Solution().reverse(120) == 21

def test_four():
    assert Solution().reverse(1534236469) == 0
