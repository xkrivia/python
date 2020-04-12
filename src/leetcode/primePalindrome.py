# CHRIS FELLI, 2019
# Return a prime palindrome equivalent to or greater than the given number
# Hence, 6 returns 7, 8 returns 11, 13 returns 101

# TODO: This algorithm is O(N^2) and not performant, runs out of memory.
# Need to improve it. Line 44 stalls.
class Solution:
    def __init__(self, N=0, s=""):
        self.N = N
        self.s = s

    # Helper
    def isPrime(self, N) -> bool:
        if N==1:
            return False
        for i in range(2,int(N**0.5)+1):
            if N%i==0:
                return False
        return True

    # Another helper
    def isPalindrome(self, s) -> bool:
        s = s.replace(' ', '')
        s = s.lower()
        if len(s) < 1:
            return True
        else:
            if s[0] == s[-1]:
                s = s[1:-1]
                return(self.isPalindrome(s))
            else:
                return False

    def primePalindrome(self, N: int) -> int:
        for i in range(N, N+1000000000):
            if self.isPrime(i) and self.isPalindrome(str(i)):
                return i
        return 0

test = Solution()
print(test.primePalindrome(6))
print(test.primePalindrome(8))
print(test.primePalindrome(13))
#print(test.primePalindrome(9989900))