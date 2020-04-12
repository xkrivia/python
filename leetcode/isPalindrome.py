# CHRIS FELLI, 2019
# Given a string, is it a palindome? For example:
# Given "ufo tofu", return TRUE
# Given "tomato", return FALSE

def isPalindrome(s: str) -> bool:
    # Remove whitespace and caps, not always necessary
    s = s.replace(' ', '')
    s = s.lower()
    # Edge case, length of one
    if len(s) < 1:
        return True
    else:
        # If first and last char match, slice them off and recurse
        if s[0] == s[-1]:
            s = s[1:-1]
            #print(s)
            return(isPalindrome(s))
        # If neither is true, return false
        else:
            return False

# Testcases
print("UFO Tofu")
print(isPalindrome("UFO Tofu"))
print("Racecar")
print(isPalindrome("Racecar"))
print("Hello, world!")
print(isPalindrome("Hello, world!"))
print("Potato flute")
print(isPalindrome("Potato flute"))