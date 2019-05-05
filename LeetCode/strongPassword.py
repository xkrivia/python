# CHRIS FELLI, 2019
# A password is strong if ALL conditions are met:
# 1) It has at least 6 characters and at most 20 characters.
# 2) It must contain at least one lowercase letter, at least one uppercase letter, 
#       and at least one digit.
# 3) It must NOT contain three repeating characters in a row
#   ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

# TODO: NOT FUNCTIONAL
class Solution:
    def __init__(self, str=""):
        str = self
        
    def strongPasswordChecker(self, s):
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < len(s) and s[p] == s[p-1]:
                    length += 1
                    p += 1
                    
                change += length / 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1
        
        if len(s) < 6:
            return max(missing_type, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_type, change)
        else:
            delete = len(s) - 20
            
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) / 2
            change -= max(delete - one - 2 * two, 0) / 3
                
            return int(delete + max(missing_type, change))

test = Solution()
print(test.strongPasswordChecker("abc"))
print(test.strongPasswordChecker("abc123abc9yz"))
print(test.strongPasswordChecker("CorrectHorseBatteryStaple95"))