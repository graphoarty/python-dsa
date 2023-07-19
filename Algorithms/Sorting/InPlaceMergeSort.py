import sys
sys.path.append('..')

from Algorithms.Array.InPlaceMerge import *

def InPlaceMergeSort(arr, l, r):

    if r - l < 2:
        return
    
    m = int((r + l) / 2)

    InPlaceMergeSort(arr, l, m)
    InPlaceMergeSort(arr, m, r)
    InPlaceMergeAscending(arr, l, r)