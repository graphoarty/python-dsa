def LinearSearchRecursive(arr, key, index = 0):
    
    if index >= len(arr):
        return -1
    
    if arr[index] == key:
        return index

    return LinearSearchRecursive(arr, key, index + 1)