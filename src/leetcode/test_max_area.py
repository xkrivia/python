from typing import List


def max_area(height: List[int]) -> int:
	i, j = 0, len(height) - 1
	water = 0	
	
	# start with outermost points, work your way towards the middle
	while i < j:
		water = max(water, (j - i) * min(height[i], height[j]))
		if height[i] < height[j]:
			i += 1
		else:
			j -= 1
	return water

def test_max_area():
	assert max_area([8,6,7,5,3,0,9]) == 48
	assert max_area([9,8,1,0,1]) == 8
	assert max_area([0,0]) == 0
	
def test_max_area_edge_cases():
	assert max_area([0]) == 0
	assert max_area([]) == 0
