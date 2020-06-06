from typing import List


def twosum(nums: List[int], target: int) -> List[int]:
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            print(buff_dict)
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


def test_1_2_3_4_5_target_9():
    """[1, 2, 3, 4, 5] target 9 returns [4, 5] at indices [3, 4]"""
    assert twosum([1, 2, 3, 4, 5], 9) == [3, 4]


def test_1_target_9():
    """[1] target 9 returns false"""
    assert twosum([1], 9) is False


def test_empty_target_9():
    """[] target 9 returns false"""
    assert twosum([], 9) is False


def test_1_2_3_4_5_target_7():
    """[1, 2, 3, 4, 5] target 7 returns [3, 4] at indices [2, 3]"""
    assert twosum([1, 2, 3, 4, 5], 7) == [2, 3]


def test_1_2_3_4_5_target_3():
    """[1, 2, 3, 4, 5] target 3 returns [1, 2] at indices [0, 1]"""
    assert twosum([1, 2, 3, 4, 5], 3) == [0, 1]


def test_1_2_3_4_5_target_0():
    """[1, 2, 3, 4, 5] target 0 returns false"""
    assert twosum([1, 2, 3, 4, 5], 0) is None
