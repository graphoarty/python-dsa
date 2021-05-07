def LeftShift(arr, shift):

    if shift < 0:
        return arr

    i = 0
    j = shift

    while j < len(arr):

        arr[i] = arr[j]

        i += 1
        j += 1

    while i < len(arr):
        
        arr[i] = 0

        i += 1

    return arr


def RightShift(arr, shift):

    if shift < 0:
        return arr

    i = len(arr) - 1 - shift
    j = len(arr) - 1

    while i >= 0:

        arr[j] = arr[i]

        i -= 1
        j -= 1

    while j >= 0:
        
        arr[j] = 0

        j -= 1

    return arr