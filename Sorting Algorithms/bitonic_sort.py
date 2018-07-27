ASCENDING = 1
DECENDING = 0

def CompareAndSwap(array, i, j, direction):

    if direction == ASCENDING:

        if array[i] > array[j]:

           array[i], array[j] = array[j], array[i] 

    elif direction == DECENDING:

        if array[i] < array[j]:

            array[i], array[j] = array[j], array[i]

def BitonicMerge(array, low, high, direction):

    if high > 1:

        split = high / 2
        for x in range(low, low + split):
            CompareAndSwap(array, x, split + x, direction)
        BitonicMerge(array, low, split, direction)
        BitonicMerge(array, low + split, split, direction)

def BitonicSort(array, low, high, direction):

    if high > 1:

        split = high / 2
        BitonicSort(array, low, split, ASCENDING)
        BitonicSort(array, low + split, split, DECENDING)
        BitonicMerge(array, low, high, direction)

array = [3, 7, 4, 8, 6, 2, 1, 5]
BitonicSort(array, 0, len(array), ASCENDING)
print(array)