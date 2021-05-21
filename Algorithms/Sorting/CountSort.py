
# Note: Only works for Positive Numbers.
def CountSort(arr):

    max = -999999
    result = []

    for item in arr:
        if item > max:
            max = item

    count_arr = [0] * (max + 1)

    for item in arr:
        count_arr[item] += 1

    for x in range(0, len(count_arr)):
        while not count_arr[x] == 0:
            result.append(x)
            count_arr[x] -= 1

    return result