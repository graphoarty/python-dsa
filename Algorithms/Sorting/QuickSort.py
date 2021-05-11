
def QuickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = 0

    i = 1
    j = len(arr) - 1

    while i <= j:

        while i < len(arr) and arr[i] < arr[pivot]:
            i += 1

        while j > pivot and arr[j] >= arr[pivot]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    return QuickSort(arr[: j]) + [arr[j]] + QuickSort(arr[j + 1 :])