from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        '''
        Takes a string and adjusts it according to a given list of indices.
        '''
        if len(s) == len(indices):
            newstr = ''
            map = {}
            for i in range(len(indices)):
                map[indices[i]] = s[i]
            for i in range(len(map)):
                newstr += map[i]
            return newstr
        else:
            return 'Input doesnt match length of indices'


def test_restore_string_exists():
    assert Solution.restoreString


def test_leetcode():
    '''
    Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    Output: "leetcode"
    Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
    '''
    assert Solution().restoreString(
        'codeleet', [4, 5, 6, 7, 0, 2, 1, 3]
    ) == 'leetcode'


def test_abc():
    '''
    Input: s = abc, indices = [0, 1, 2]
    Output: abc
    '''
    assert Solution().restoreString(
        'abc', [0, 1, 2]
    ) == 'abc'


def test_nihao():
    '''
    Input: s = aiohn, indices = [3, 1, 4, 2, 0]
    Output: nihao
    '''
    assert Solution().restoreString(
        'aiohn', [3, 1, 4, 2, 0]
    ) == 'nihao'


def test_arigatou():
    '''
    Input: s = aaiougrt, indices = [4, 0, 2, 6, 7, 3, 1, 5]
    Output: arigatou
    '''
    assert Solution().restoreString(
        'aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]
    ) == 'arigatou'


def test_rat():
    '''
    Input: s = art, indices = [1, 0, 2]
    Output: rat
    '''
    assert Solution().restoreString(
        'art', [1, 0, 2]
    ) == 'rat'
