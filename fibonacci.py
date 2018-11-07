# fibonacci.py
# Written by: ChrisTheCaribou
# This program outputs fibonacci sequence between 1 and 100,000,000
import time

# Defines fibonacci sequence core logic
# 1,1,2,3,5,8,13 ...
def Fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

# Defines iterative sequence
def SubFibonacci(num_0, num_1):
    for cur in Fibonacci():
        if cur > num_1: return
        if cur >= num_0: yield cur

# Outputs results
for i in SubFibonacci(1, 100000000):
    print(i)
    time.sleep(0.1) # Wait tenth of second, just for fun
