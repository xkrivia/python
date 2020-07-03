class Solution:
    def __init__(self, num="", k=0):
        self.num = num
        self.k = k

    def remove_K_digits_naive(self, num: str, k: int) -> str:
        # Edge cases
        if (len(num) == 1):
            return str(num)
        if (len(num) == k):
            return str(num)
        elif (len(num) < k):
            return -1
        # Base case
        candidates = []
        for i in range(len(num)-1):
            t1 = num[i:i+k]
            t2 = num.replace(t1, "")
            candidates.append(t2)
        candidates.sort()
        if(candidates[0].lstrip("0") == ""):
            return("0")
        elif(candidates[0].lstrip("0") != ""):
            return(candidates[0].lstrip("0"))

    def remove_K_digits_O_of_N(self, num: str, k: int) -> str:
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


def test_remove_K_digits():
    test = Solution()
    assert test.remove_K_digits_O_of_N("14322219", 3) == "12219"
    assert test.remove_K_digits_O_of_N("10200", 1) == "200"
    assert test.remove_K_digits_O_of_N("0", 1) == "0"
    assert test.remove_K_digits_O_of_N("10", 1) == "0"
    assert test.remove_K_digits_O_of_N("9", 1) == "0"


def test_remove_K_digits_2():
    test = Solution()
    assert test.remove_K_digits_O_of_N("123456789", 5) == "1234"
    assert test.remove_K_digits_O_of_N("999999999", 9) == "0"
    assert test.remove_K_digits_O_of_N("999999999", 5) == "9999"
    assert test.remove_K_digits_O_of_N("abcdefghij", 6) == "abcd"
    assert test.remove_K_digits_O_of_N("00000000001", 1) == "0"
