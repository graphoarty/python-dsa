import random

def InsertionSort(array):

    for x in range (1, len(array)):
        for i in range(x, 0, -1):
            if array[i] < array[i - 1]:
                t = array[i]
                array[i] = array[i - 1]
                array[i - 1] = t
            else:
                break
            i = i - 1
    return array

def Merge(aArr, bArr):
    
    a = 0
    b = 0
    cArr = []

    while a < len(aArr) and b < len(bArr):
        if aArr[a] < bArr[b]:
            cArr.append(aArr[a])
            a = a + 1
        elif aArr[a] > bArr[b]:
            cArr.append(bArr[b])
            b = b + 1
        else:
            cArr.append(aArr[a])
            cArr.append(bArr[b])
            a = a + 1
            b = b + 1

    while a < len(aArr):
        cArr.append(aArr[a])
        a = a + 1

    while b < len(bArr):
        cArr.append(bArr[b])
        b = b + 1

    return cArr

def TimSort():

    for x in range(0, len(arr), RUN):
        arr[x : x + RUN] = InsertionSort(arr[x : x + RUN])
    RUNinc = RUN
    while RUNinc < len(arr):
        for x in range(0, len(arr), 2 * RUNinc):
            arr[x : x + 2 * RUNinc] = Merge(arr[x : x + RUNinc], arr[x + RUNinc: x + 2 * RUNinc])
        RUNinc = RUNinc * 2


arr = []
RUN = 32
for x in range(0, 50):
    arr.append(random.randint(0, 100))
TimSort()
print(arr)