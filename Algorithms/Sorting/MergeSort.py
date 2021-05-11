import sys
sys.path.append('..')

from Algorithms.Array.Merge import *

def MergeSort(arr):

    if len(arr) <= 1:
        return arr

    m = int(len(arr) / 2)

    arr1 = MergeSort(arr[: m])
    arr2 = MergeSort(arr[m :])

    # Use either MergeAscending or MergeDescending
    return MergeAscending(arr1, arr2)