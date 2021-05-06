def LinearSearch(arr, key):

    for x in range(0, len(arr)):

        if arr[x] == key:

            return x

    return -1