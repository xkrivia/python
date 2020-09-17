class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle != '':
            if needle in haystack:
                print('yes')
                return 1
            else:
                return -1
        else:
            return 0


def test_hi():
    assert Solution().strStr('hello', 'll') is 1


def test_a():
    assert Solution().strStr('aaaaa', 'bba') is -1


def test_empty():
    assert Solution().strStr('test', '') is 0
