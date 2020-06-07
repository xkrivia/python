import pytest


class reverse:
    def __init__(self, x):
        self.x = x
        self.reversed = self._reverse(x)

    def _reverse(self, x: int) -> int:
        is_neg = False
        x = str(x)
        if x.startswith("-"):
            is_neg = True
            x = x[1:]
        x = x[::-1]
        x = x.lstrip("0")
        try:
            x = int(x)
            if is_neg is True:
                x *= -1
            if x > 2147483647 or x < -2147483647:
                return 0
            return x
        except ValueError:
            return 0


def test_reverse_suite_1():
    test_1 = reverse(8675309)
    test_2 = reverse(-123456789)
    test_3 = reverse(5550101)
    test_4 = reverse(-98101)
    test_5 = reverse(44444)
    test_6 = reverse(-10000)
    assert(test_1.reversed == 9035768)
    assert(test_2.reversed == -987654321)
    assert(test_3.reversed == 1010555)
    assert(test_4.reversed == -10189)
    assert(test_5.reversed == 44444)
    assert(test_6.reversed == -1)


def test_reverse_zero_handling():
    test_1 = reverse(1)
    test_2 = reverse(10)
    test_3 = reverse(101)
    test_4 = reverse(1001)
    test_5 = reverse(1010)
    test_6 = reverse(101011000000000)
    assert(test_1.reversed == 1)
    assert(test_2.reversed == 1)
    assert(test_3.reversed == 101)
    assert(test_4.reversed == 1001)
    assert(test_5.reversed == 101)
    assert(test_6.reversed == 110101)


def test_is_same_tree_edge_cases():
    test = reverse(2147483647)
    assert(test.reversed == 0)
