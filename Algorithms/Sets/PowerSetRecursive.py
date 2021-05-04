subsets = []

def PowerSetRecursiveHelper(arr, p_arr, start, end):

    global subsets

    if start >= end:

        subsets.append(list("".join(p_arr)))

        if len(subsets) == 2 ** len(arr):
            return subsets

    else:

        p_arr.append(arr[start])
        PowerSetRecursiveHelper(arr, p_arr, start + 1, end)
        p_arr.pop()
        return PowerSetRecursiveHelper(arr, p_arr, start + 1, end)


def PowerSetRecursive(arr):

    global subsets

    subsets = []
    return(PowerSetRecursiveHelper(arr, [], 0, len(arr)))


# print(PowerSetRecursive(['a', 'b', 'c']))