def Difference(arr1, arr2):

    arr3 = []

    for i in range(0, len(arr1)):

        present = False

        for j in range(0, len(arr2)):

            if arr1[i] == arr2[j]:

                present = True

                break

        if not present:

            arr3.append(arr1[i])

    return arr3