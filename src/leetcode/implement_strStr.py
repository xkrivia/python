class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle != '':
            return haystack.find(needle)
        else:
            return 0


def test_hi():
    assert Solution().strStr('hello', 'll') is 2


def test_a():
    assert Solution().strStr('aaaaa', 'bba') is -1


def test_empty():
    assert Solution().strStr('test', '') is 0
