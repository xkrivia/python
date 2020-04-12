# CHRIS FELLI, 2019
# Convert Roman numerals to Arabic numerals
# Note these special cases:
#   - I can be placed before V (5) and X (10) to make 4 and 9. 
#   - X can be placed before L (50) and C (100) to make 40 and 90. 
#   - C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

# Testcases
test = Solution()
print(test.romanToInt('I'))
print(test.romanToInt('III'))
print(test.romanToInt('IV'))
print(test.romanToInt('LVIII'))
print(test.romanToInt('MCMXCIV'))
print(test.romanToInt('MCMXCV'))