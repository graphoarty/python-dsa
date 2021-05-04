subsets = []

def PowerSetRecursiveHelper(arr, p_arr, start, end):

    global subsets

    if start >= end:

        subsets.append("".join(p_arr))

        if len(subsets) == 2 ** len(arr):
            return subsets

    else:

        p_arr.append(arr[start])
        PowerSetRecursiveHelper(arr, p_arr, start + 1, end)
        p_arr.pop()
        return PowerSetRecursiveHelper(arr, p_arr, start + 1, end)


def PowerSetRecursive(s):

    global subsets

    subsets = []
    return(PowerSetRecursiveHelper(list(s), [], 0, len(s)))


# print(PowerSetRecursive('abcd'))