# CHRIS FELLI, 2019
# Reverse a string without a built-in function

class Solution:
    def _init_(self, x):
        self.x = x

    def reverse(self, x: int) -> int:
        isNeg = False
        x = str(x)  # Convert to str
        if x.startswith("-"):
            isNeg = True
            x = x[1:] # Strip neg
        x = x[::-1] # Reverse it
        x = x.lstrip("0") # Strip leading zeros
        try: # Try to cast 
            x = int(x)
            if isNeg==True:
                x *= -1
            if x>2147483647 or x<-2147483647:
                return 0
            return x
        except ValueError:
            return 0

# Driver
test = Solution()
print(test.reverse("12345000"))
print(test.reverse("123"))
print(test.reverse("120"))
print(test.reverse("-123"))
print(test.reverse("1534236469"))
print(test.reverse("-2147483648"))