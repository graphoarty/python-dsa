# The Pigeonhole Sort is a sorting algorithm that
# works only for an array of integers.
# It works best when the number of elements and
# the number of possible key values is the same
# which basically means every element is unique

def PigeonHoleSort(array):

    # Get the smallest element in the array
    smallestIntegerInArray = min(array)

    # Get the largest element in the array
    largestIntegerInArray = max(array)

    # Get an estimate of the number of holes needed
    numberOfHoles = largestIntegerInArray - smallestIntegerInArray + 1

    # Generate the holes
    holes = []
    for x in range(0, numberOfHoles):
        holes.append(0)

    # Fill the holes
    # The elements k
    for x in array:
        holes[x - smallestIntegerInArray] += 1

    # pick out the elements from the holes
    # one by one and generate the sorted array
    sortedArray = []

    # your range is the number of holes there are
    for count in range(numberOfHoles):
        # also, the number of elements inside those holes
        while holes[count] > 0:
            holes[count] -= 1
            # the actual element is count + smallestIntegerInArray
            # because we subtracted it earlier
            sortedArray.append(count + smallestIntegerInArray)

    return sortedArray
 
array = [8, 8, 10, 6, 5, 2, 4, 7, 3, 1]
print(PigeonHoleSort(array))