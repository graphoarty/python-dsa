
# For number bigger than zero.
def BucketSort(arr):

    max = 0
    result = []

    for x in range(0, len(arr)):
        if arr[x] > max:
            max = arr[x]

    buckets = []
    for x in range(0, max + 1):
        buckets.append([])

    for x in range(0, len(arr)):
        buckets[arr[x]].append(arr[x])

    for bucket in buckets:
        for item in bucket:
            result.append(item)

    return result

