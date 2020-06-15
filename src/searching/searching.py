def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # Set boundaries for low and high marks to search
    low = 0
    high = len(arr)
    # While low and high to not overlap
    while low < high:
        # Check the midpoints
        mid = (low + high) // 2
        # If equal, return true
        if arr[mid] == target:
            return mid
        # Else if target is smaller
        elif target < arr[mid]:
            # set the high to be the midpoint
            high = mid
        # Else if target is bigger
        else:
            # set the low to be midpoint
            low = mid + 1

    # If we get to the end return False
    return -1  # not found
