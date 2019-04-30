# CHRIS FELLI, 2019
# Given a positive integer N, return the number of positive integers less than or 
# equal to N that have at least 1 repeated digit. For example:
# Inputting 100 would return 10, because in that range is
# 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

class Solution:
    # This helper checks if a given number has duplicate digits
    def __init__(self, L=0, N=0):
        self.L = L
        self.N = N

    def duplicateDigits(self, L: int) -> bool:
        digits = [int(x) for x in str(L)]
        # Edge case: length of one
        if len(digits) == 1:
            return False
        # Normal case
        digits = sorted(digits)
        for i in (range(len(digits)-1)):
            if digits[i] == digits[i+1]:
                return True
        # If not satisfied ...
        return False
        
    def numDupDigitsAtMostN(self, N: int) -> int:
        counterList = []
        counter = 0
        for i in range(N+1):
            if Bob.duplicateDigits(i):
                counter += 1
                counterList.append(i)
        print(counterList)
        return counter

# Testcases
Bob = Solution(0, 0)
print(Bob.duplicateDigits(9))
print(Bob.duplicateDigits(11))
print(Bob.duplicateDigits(95))
print(Bob.duplicateDigits(666))
print(Bob.duplicateDigits(6766))
print(Bob.duplicateDigits(100))
print(Bob.duplicateDigits(909))
print(Bob.numDupDigitsAtMostN(20))
print(Bob.numDupDigitsAtMostN(100))
print(Bob.numDupDigitsAtMostN(1000))