# CHRIS FELLI, 2019
# Given a string s1, we may represent it as a binary tree by partitioning it
# to two non-empty substrings recursively.

class Solution:
    def __init__(self, s1="", s2=""):
        self.s1 = s1
        self.s2 = s2

    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
            f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

Bob = Solution("great", "rgeat")
print(Bob.isScramble("great", "rgeat"))
Bob = Solution("abcde", "caebd")
print(Bob.isScramble("abcde", "caebd"))