# CHRIS FELLI, 2019
# Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.


class Solution:
    def __init__(self, num="", k=0):
        self.num = num
        self.k = k

    def removeKdigits(self, num: str, k: int) -> str:
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

    def removeKdigitsON(self, num, k):
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


# Testcases
test = Solution()
print(test.removeKdigits("1432219", 3))
print(test.removeKdigits("10200", 1))
print(test.removeKdigits("0", 1))
print(test.removeKdigits("10", 1))
print(test.removeKdigits("9", 1))
