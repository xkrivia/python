# CHRIS FELLI, 2019
# Flatten a list of arrays of n depth
from typing import Iterable            

def flattenGenerator(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

def flatten(items):
    return list(flattenGenerator(items))

print(flatten([[1, 2, 3], [4, [5, 6]], [7], [8, 9]]))
print(flatten([[1, [2]], (3, 4, {5, 6}, 7), 8, "9"]))