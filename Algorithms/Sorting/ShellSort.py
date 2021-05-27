
def ShellSort(arr):

    gap = int(len(arr) / 2)

    while gap > 0:

        j = gap

        while j < len(arr):

            if arr[j] < arr[j - gap]:
                temp = arr[j]
                arr[j] = arr[j - gap]
                arr[j - gap] = temp

            j += 1


        gap = int(gap / 2)

    return arr