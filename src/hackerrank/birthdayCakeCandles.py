# CHRIS FELLI, 2019

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar):
    return ar.count(max(ar))


print(birthdayCakeCandles([4, 4, 1, 3]))
