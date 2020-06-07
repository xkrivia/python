import pytest


class combination_sum_ii:
    def __init__(self, candidates=[], target=0):
        self.candidates = candidates
        self.target = target

    def combination_sum_ii(self, candidates, target):
        candidates.sort()
        result = []
        self._combinerator(candidates, 0, [], result, target)
        return result

    def _combinerator(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self._combinerator(nums, i + 1, path +
                               [nums[i]], result, target - nums[i])


def test_combination_sum_ii_success():
    test = combination_sum_ii()
    assert(test.combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8))


def test_combination_sum_ii_failures():
    test = combination_sum_ii()
    with pytest.raises(TypeError):
        test.combination_sum_ii(["text"], "text")
    with pytest.raises(TypeError):
        test.combination_sum_ii(["2020 is wild"], 2)
    with pytest.raises(TypeError):
        test.combination_sum_ii(["2020 is wild"])
    with pytest.raises(AttributeError):
        test.combination_sum_ii(0, 1)


def test_combination_sum_ii_edge_cases():
    test = combination_sum_ii()
    assert(test.combination_sum_ii([1], 1))
    assert(test.combination_sum_ii([], 0))
