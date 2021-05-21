
# Note: Only works for Positive Numbers.
def RadixSort(arr):

    max = -999999

    for item in arr:
        if item > max:
            max = item

    n = len(str(max))

    iterations = 0
    while iterations < n:

        bins = []
        for x in range(0, 10):
            bins.append([])

        for item in arr:
            bins[ int(item / pow(10, iterations)) % 10 ].append(item)

        new_arr = []
        for bin in bins:
            for item in bin:
                new_arr.append(item)

        arr = new_arr

        iterations += 1

    print(arr)