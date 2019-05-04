# CHRIS FELLI,2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    final = 0
    for i in range(len(ar)):
        final = final + ar[i]
        print("Current: ", final)
    return final

print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))