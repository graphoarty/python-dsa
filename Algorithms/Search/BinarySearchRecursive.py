
def BinarySearchRecursiveHelper(arr, key, start, end):

    if start <= end:

        mid = int((start + end) / 2)

        if key == arr[mid]:

            return mid

        if key > arr[mid]:

            return BinarySearchRecursiveHelper(arr, key, mid + 1, end)

        if key < arr[mid]:

            return BinarySearchRecursiveHelper(arr, key, start, mid - 1)

    else:

        return -1
    

def BinarySearchRecursive(arr, key):

    return BinarySearchRecursiveHelper(arr, key, 0, len(arr) - 1)