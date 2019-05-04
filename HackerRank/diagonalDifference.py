# CHRIS FELLI, 2019

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    diag1 = 0
    diag2 = 0
    size = len(arr[0])
    for i in range(size):
        # Main diag: [0, 0] to [size, size]
        diag1 += arr[i][i]
        # Second diag: going from [0, size] to [size, 0]
        diag2 += arr[i][size-i-1]
    return abs(diag1-diag2)

print(diagonalDifference([[11,2,4],
                        [4,5,6],
                        [10,8,-12]]))