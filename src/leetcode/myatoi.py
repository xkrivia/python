# CHRIS FELLI, 2019
# Build your own atoi
import re
import string


class Solution:
    def _init_(self, s):
        self.s = s

    def myAtoi(self, str: str) -> int:
        # Strip whitespace
        str = str.lstrip(" ")
        # If negative, remove from str and NEVER FORGET
        isNeg = False
        if(str.startswith("-")):
            isNeg = True
            str = str[1:]
        # If first str char is alphabetic, return 0
        if(str.startswith(tuple(string.ascii_letters))):
            return 0
        # Strip whitespace/alphanumerics from right
        str = re.sub("[^0-9]", "", str)
        try:  # Try to cast
            fin = int(str)
            if isNeg == True:
                fin *= -1
            if fin > 2147483648:
                return 2147483648
            if fin < -2147483648:
                return -2147483648
            return fin
        except ValueError:
            return 0


# Driver
test = Solution()
print(test.myAtoi("42"))
print(test.myAtoi("    -42"))
print(test.myAtoi("4193 with words"))
print(test.myAtoi("words and 987"))
print(test.myAtoi("-91283472332"))
print(test.myAtoi("42"))
