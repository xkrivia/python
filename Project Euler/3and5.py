# CHRIS FELLI, 2019
# This program adds all elements less than 1000 that are divisble by 3 or 5
# (Problem #2 on Project Euler)

# Checks divisibility by 3, returns BOOL
def MultOf3(mult3):
    div3 = int(mult3) % 3
    if div3 == 0: return True
    else: return False

# Checks divisibility by 5, returns BOOL
def MultOf5(mult5):
    div5 = int(mult5) % 5
    if div5 == 0: return True
    else: return False

# Iterate 1 through 1000, add 3 or 5 divisble elements to list35
list35 = []
for i in range(1000):
    if MultOf3(i) == True or MultOf5(i) == True:
        list35.append(i)

# Output sum
print(sum(list35))
