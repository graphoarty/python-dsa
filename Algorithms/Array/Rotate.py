def LeftRotate(arr, rotate = 1):

    if rotate < 0:
        return arr

    while rotate > 0:

        i, j = 0, 1

        temp = arr[i]

        while j < len(arr):

            arr[i] = arr[j]

            i += 1
            j += 1

        arr[i] = temp

        rotate -= 1

    return arr


def RightRotate(arr, rotate = 1):

    if rotate < 0:
        return arr

    while rotate > 0:

        i, j = len(arr) - 2, len(arr) - 1

        temp = arr[j]

        while i >= 0:

            arr[j] = arr[i]

            i -= 1
            j -= 1

        arr[j] = temp

        rotate -= 1

    return arr