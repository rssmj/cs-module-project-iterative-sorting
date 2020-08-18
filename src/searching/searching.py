def linear_search(arr, target):
    # Your code here
    # loop through array
    for i in range(len(arr)):
        # item is equal to target
        if arr[i] == target:
            # update item
            return i
    return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # high point set last in array
    high = len(arr) - 1
    # middle and low point
    middle = 0
    low = 0
    # while loop
    while low <= high:
        # find middle point
        middle = (high + low) // 2
        # middle is lower
        if arr[middle] < target:
            # bypass left side of array
            low = middle + 1
        # middle is higher
        elif arr[middle] > target:
            # bypass right side of array
            high = middle - 1
        else:
            return middle
    return -1  # not found
