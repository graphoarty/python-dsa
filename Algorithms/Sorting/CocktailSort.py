def CocktailSort(array):

    isSwapped = True
    start = 0
    end = len(array) - 1

    while (isSwapped == True):

        isSwapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwapped = True

        if (isSwapped == False):
            break

        isSwapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                isSwapped = True

        start = start + 1

    return array

print(CocktailSort([31, 81, 84, 23, 63, 57, 16, 25, 63, 40]))