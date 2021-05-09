def Union(arr1, arr2):

    arr3 = arr1

    for i in range(0, len(arr2)):

        present = False

        for j in range(0, len(arr3)):

            if arr2[i] == arr3[j]:

                present = True

                break

        if not present:

            arr3.append(arr2[i])

    return arr3

            