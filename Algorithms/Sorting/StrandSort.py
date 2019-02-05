# Function to merge first and second array
def Merge(first, second):
    
    a = 0
    b = 0
    mergedArray = []

    while a < len(first) and b < len(second):
        if first[a] < second[b]:
            mergedArray.append(first[a])
            a = a + 1
        elif first[a] > second[b]:
            mergedArray.append(second[b])
            b = b + 1
        else:
            mergedArray.append(first[a])
            mergedArray.append(second[b])
            a = a + 1
            b = b + 1

    while a < len(first):
        mergedArray.append(first[a])
        a = a + 1

    while b < len(second):
        mergedArray.append(second[b])
        b = b + 1

    return mergedArray  


# The Strand Sort Function
def StrandSort(inputArray):

    # outputArray for accumulating results
    outputArray = []

    # run while loop while inputArray is not empty
    while len(inputArray) > 0:

        # clear the sublist and 
        # remove the first element from the 
        # input array and put in the sublist
        sublist = [ inputArray.pop(0) ]

        # loop over the inputArray
        x = 0
        while x < len(inputArray):
            
            # check if the current value in the inputArray is greater than the sublist
            # if it is, remove that element from the inputArray and put it at the end
            # of the sublist

            if inputArray[x] > sublist[-1]:
                sublist.append(inputArray.pop(x))
            # increment x to keep the while loop moving forward
            else:
                x = x + 1

        # merge sublist with outputArray and store the results in outputArray
        outputArray = Merge(sublist, outputArray)

    return outputArray

print(StrandSort([ 58, 38, 4, 91, 62 ]))
