# CHRIS FELLI, 2019
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
# number could represent.
from typing import List


class Solution:
    def __init__(self, digits=""):
        self.digits = digits

    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': "abc", '3': "def",
                   '4': "ghi", '5': "jkl", '6': "mno",
                   '7': "pqrs", '8': "tuv", '9': "wxyz"}
        # Edge case: Length of zero? Return zero
        if len(digits) == 0:
            return []
        # Edge case: Length of one? Just map
        if len(digits) == 1:
            return list(mapping[digits[0]])
        # Main case
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]


# Testcase
test = Solution()
print(test.letterCombinations("2"))
print(test.letterCombinations("23"))
print(test.letterCombinations("423"))
