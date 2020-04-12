# CHRIS FELLI, 2019
# Identify anagrams from a list of strings
# Return a list of a list of strings!

from typing import List

# TIME COMPLEXITY: O(n)

# EXPLANATION: Since a 'for' loop is implemented, it cannot
# be O(1). Since the 'for' loop will always iterate once and
# ONLY once (no conditionals), it cannot be O(n log n). Ergo,
# it must be O(n).

# SPACE COMPLEXITY: O(n)

# EXPLANATION: If the list is of size 'n', and the dictionary
# is also of size 'n' (in this instance, it linearly increases
# along with the string array), space complexity is O(2n).
# Constants can be dropped when dealing with Big-O notation,
# ergo, space complexity is O(n).

class Solution:
    def __self__(self, words):
        self.words = words

    def Anagrams(self, words: List[str]) -> List[List[str]]:
        dict = {}
        for word in words:
            key = tuple(sorted(word))
            dict[key] = dict.get(key, []) + [word]
        return list(dict.values())

# Driver & testcases
t = Solution()
print(t.Anagrams([]))
print(t.Anagrams(['']))
print(t.Anagrams(['pots', 'post', 'chris']))
print(t.Anagrams(['abets', 'baste', 'betas', 'beast', 
'beats', 'amen', 'mane', 'mean', 'name', 'CHONK']))
print(t.Anagrams(['a', 'b', 'c']))