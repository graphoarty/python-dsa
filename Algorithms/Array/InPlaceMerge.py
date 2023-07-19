def InPlaceMerge(arr, l, r):

    m = int((l + r) / 2)

    i = l
    j = m

    while i < m and j < r:

        if arr[i] <= arr[j]:
            
            i = i + 1

        else:

            value = arr[j]
            index = j

            while index > i:
            
                arr[index] = arr[index - 1]
                index = index - 1

            arr[index] = value

            i = i + 1
            j = j + 1
            m = m + 1