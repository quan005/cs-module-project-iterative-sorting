def linear_search(arr, target):
    # Your code here

    # Set i to 0
    i = 0
    # Iterate through each value
    while i < len(arr):
        # Check if i is equal to the target value
        if arr[i] == target:
            # If so, return 1 or True or i/index
            return i
        # If its not equal
        else:
            # Increment i by 1 to go to the next index
            i += 1
    # If nothing is returned then return False or -1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 0:
        return -1 # array empty
    
    start = 0
    end = len(arr)-1

    # TO-DO: add missing code

    # While the start point is less than or equal to the end point
    while start <= end:
        # Find the middle point
        middle = (start + end) // 2
        # Check if the middle point is equal to the target
        if arr[middle] == target:
            # If so, return True or 1 or the index
            print('found at', middle)
            return middle
        # Check if the middle point is greater than the target
        elif arr[middle] > target:
            # If so, change the end point to equal the middle point minus 1
            end = middle - 1
        # Check if the middle point is less than the target
        elif arr[middle] < target:
            # If so, change the start point to equal the middle point plus 1
            start = middle + 1
    # IF nothing is returned then return False or -1
    print('not found')
    return -1  # not found
