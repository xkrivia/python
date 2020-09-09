class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Determines if input string is a palindrome
        '''
        s = Solution.prepInput(s)
        # Shorthand to reverse string [::-1]
        return s == s[::-1]

    def prepInput(self, s: str) -> str:
        '''
        Helper function to turn input string into only lowercase alphanumeric characters
        '''
        # casefold is faster and more efficient than .lower()
        s = s.casefold()
        # s = s.replace(' ', '') <maybe not needed after following code>
        # Alphanumeric strip courtesy of:
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        delchar = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
        s = s.translate(None, delchar)
        return s


def manTest():
    '''
    Tests 1st case in leetcode example
    '''
    assert Solution.isPalindrome('A man, a plan, a canal: Panama')


def raceTest():
    '''
    Tests 2nd case in leetcode example
    '''
    assert Solution.isPalindrome('race a car')
