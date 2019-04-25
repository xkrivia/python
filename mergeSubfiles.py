# CHRIS FELLI, 2019
# Given an array of integers, merge the values of the
# array at lowest cost. For example:
# Given 4, [18, 5, 11, 2]:
# I)  [18, 5, 13]     13=11+2 is lowest of those costs
# II) [18, 18]        18=5+13
# III)[36]            36=18+18
# IV) return 67       =13+18+36

total = 0
final = 0
iteration = 1
def mergeSubfiles(arr):
    global total
    global iteration
    global final

    # Edge case: length of one
    if len(arr)==1 & iteration==1:
        return 0

    print("\nITERATION: ", iteration)
    print("Inputed array is: ", arr)
    delta = [0] * (len(arr)-1)
    for i in range(len(arr)-1):
        delta[i] = arr[i] + arr[i+1]
    print("Delta array is: ", delta)
    # find lowest index
    total += min(delta)
    minIndex = delta.index(min(delta))
    print("Minimum position in array is: ", minIndex)
    # At lowest index, 
    arr[minIndex] = arr[minIndex]+arr[minIndex+1]
    arr.pop(minIndex+1)
    print("New array is: ", arr)
    print("Current total is: ", total)
    iteration += 1
    if len(arr)!=1:
        mergeSubfiles(arr)
    elif len(arr)==1:
        final = total
        total = 0
        iteration = 1
        print("FINAL TOTAL:", final)
    return final

#mergeSubfiles([18, 5, 11, 2])
#print(mergeSubfiles([18, 5, 11, 2]))
print(mergeSubfiles([18]))
#print(mergeSubfiles([18]))