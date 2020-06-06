# CHRIS FELLI, 2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.


def staircase(n):
    for i in range(n+1):
        if i == 0:
            continue
        print(("#"*i).rjust(n))


staircase(3)
staircase(5)
staircase(10)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
