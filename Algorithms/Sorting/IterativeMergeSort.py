
def Merge(arr, l, m, h):

    newArr = []

    i = l
    j = m + 1

    while i <= m and j <= h:

        if arr[i] < arr[j]:
            newArr.append(arr[i])
            i += 1
        elif arr[j] < arr[i]:
            newArr.append(arr[j])
            j += 1
        else:
            newArr.append(arr[i])
            i += 1
            newArr.append(arr[j])
            j += 1

    while i <= m:
        newArr.append(arr[i])
        i += 1

    while j <= h:
        newArr.append(arr[j])
        j += 1

    return arr[: l] + newArr + arr[h + 1 :]


def IterativeMergeSort(arr):

    p = 2

    while p <= len(arr):

        i = 0
        l = 0
        m = 0
        h = 0

        while i + p - 1 < len(arr):

            l = i
            h = i + p - 1
            m = int((l + h) / 2)

            print(f"{l} {m} {h}")

            arr = Merge(arr, l, m, h)

            i += p
    
        p *= 2

    if int(p/2) < len(arr):
        arr = Merge(arr, 0, int(p/2), len(arr) - 1)

    return arr