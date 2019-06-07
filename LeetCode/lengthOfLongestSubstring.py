# CHRIS FELLI, 2019
# Given a string, find the length of the longest 
# substring without repeating characters.

# NAIVE:
# Memoize! Take the string, recurse through 

class Solution:
    def _init(self, s):
        self.s = s

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

# Driver
test = Solution()
print(test.lengthOfLongestSubstring("bbbbb"))
print(test.lengthOfLongestSubstring("abcabcbb"))