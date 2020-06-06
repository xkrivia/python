# CHRIS FELLI, 2019

#!/bin/python3

import os
import sys


def timeConversion(time):
    # 11:15:45PM -> 23:15:45
    hh = time[0:2]
    period = time[-2:]

    if period == 'AM':
        if hh == '12':
            output = '00' + time[2:-2]
            return output
        else:
            output = time[0:-2]
            return output
    elif period == 'PM':
        hh = time[0:2]
        if hh == '12':
            output = time[0:-2]
            return output
        else:
            output = str(int(hh) + 12) + time[2:-2]
            return output
    else:
        assert False


print(timeConversion("12:40:22AM"))  # 00:40:22
print(timeConversion("12:05:39AM"))  # 00:05:39
print(timeConversion("04:59:59AM"))  # 04:59:59
print(timeConversion("12:00:00AM"))  # 00:00:00
