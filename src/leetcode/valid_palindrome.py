class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Determines if input string is a palindrome
        '''
        s = Solution.prepInput(s)
        # Shorthand to reverse string [::-1]
        return s == s[::-1]

    def prepInput(s: str) -> str:
        '''
        Helper function to turn input string into only lowercase alphanumeric characters
        '''
        # casefold is faster and more efficient than .lower()
        print(s)
        s = s.casefold()
        s = ''.join(c for c in s if c.isalnum())
        print('final s:', s)
        return s


def test_man():
    '''
    Tests 1st case in leetcode example
    '''
    assert Solution().isPalindrome('A man, a plan, a canal: Panama')


def test_race():
    '''
    Tests 2nd case in leetcode example
    '''
    assert Solution().isPalindrome('race a car') is False
