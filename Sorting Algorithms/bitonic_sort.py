def BitonicSort(direction, arr):

    if len(arr) <= 1:
        return arr
    else: 
        first = BitonicSort(True, arr[:len(arr) // 2])
        second = BitonicSort(False, arr[len(arr) // 2:])
        return BitonicMerge(direction, first + second)

def BitonicMerge(direction, arr): 

    if len(arr) == 1:
        return arr
    else:
        BitonicCompare(direction, arr)
        first = BitonicMerge(direction, arr[:len(arr) // 2])
        second = BitonicMerge(direction, arr[len(arr) // 2:])
        return first + second

def BitonicCompare(direction, arr):

    dist = len(arr) // 2
    
    for i in range(dist):  
        if (arr[i] > arr[i + dist]) == direction:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]

array = [ 3, 7, 4, 8, 6, 2, 1, 5 ]
array = BitonicSort(True, array)
print(array)