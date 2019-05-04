# CHRIS FELLI, 2019
# Given a string of only parentheses, return the
# length of the longest valid substring

class Solution:
    def _init_(self, s=""):
        self.s = s

    # dp[i] = the number of longest valid Parentheses ended with the 
    # i - 1 position of s, then we have the following relationship:
    # dp[i + 1] = dp[p] + i - p + 1
    # where p is the position of '(' which can matches current ')' in the stack.
    def longestValidParentheses(self, s):
        dp = [0]*(len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p]+i-p+1
        return max(dp)


test = Solution()
print(test.longestValidParentheses("()"))
print(test.longestValidParentheses("(()"))
print(test.longestValidParentheses(")()())"))