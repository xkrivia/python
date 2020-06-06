# CHRIS FELLI, 2019
# Given an array of integers, merge the values of the
# array at lowest cost. For example:
# Given 4, [18, 5, 11, 2]:
# I)  [18, 5, 13]     13=11+2 is lowest of those costs
# II) [18, 18]        18=5+13
# III)[36]            36=18+18
# IV) return 67       = 13+18+36

# Global variables
total = 0
final = 0
iteration = 1


def mergeSubfiles(arr) -> int:
    global total
    global iteration
    global final

    # Edge case: Array length of one
    if len(arr) == 1 & iteration == 1:
        return 0

    print("Array is: ", arr)

    # Define delta array, the derivative of arr
    delta = [0] * (len(arr)-1)
    for i in range(len(arr)-1):
        delta[i] = arr[i] + arr[i+1]
    #print("Delta array is: ", delta)

    # Find lowest index
    total += min(delta)
    minIndex = delta.index(min(delta))

    # At lowest index, add next index's value and POP it
    arr[minIndex] = arr[minIndex]+arr[minIndex+1]
    arr.pop(minIndex+1)

    print("New array is: ", arr)
    print("Current total is: ", total)
    iteration += 1

    # If array bigger than one, recurse (sic(?))
    if len(arr) != 1:
        mergeSubfiles(arr)
    # Otherwise, reset variables and return final
    elif len(arr) == 1:
        final = total
        total = 0
        iteration = 1
        print("FINAL TOTAL:", final)
    return final


# Testcases
print(mergeSubfiles([18]))
print(mergeSubfiles([18, 5, 11, 2]))
print(mergeSubfiles([16, 13, 1, 5]))
