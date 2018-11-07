# SquareSums.py
# Written by: ChrisTheCaribou
# Subtracts sum of squares from the square of the sums
# (Problem #6 on Project Euler)

# Calculates sum of squares
# 1^2 + 2^2 + 3^2 + ...
def SumOfSquares(firstNum, lastNum):
    sumInt = 0
    i = firstNum
    for i in range(lastNum + 1): sumInt += i * i
    return sumInt
    #print(sumInt)

# Calculates square of sums
# (1 + 2 + 3 + ...)^2
def SquareOfSums(firstNum, lastNum):
    sumInt = 0
    i = firstNum
    for i in range(lastNum + 1): sumInt += i
    sumInt = sumInt * sumInt
    return sumInt
    #print(sumInt)

# Calculates difference
def CalcDiff(firstNum, lastNum):
    print(SquareOfSums(firstNum, lastNum) - SumOfSquares(firstNum, lastNum))

# Outputs results
CalcDiff(1, 100)
