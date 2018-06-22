combinations = []

def CombinationsWithRepitition(array, tempArray, r):

    if len(tempArray) == r:
        
        combinations.append("".join(tempArray))

    else:    

        for x in range(0, len(array)):
            tempArray.append(array[x])
            CombinationsWithRepitition(array, tempArray, r)
            tempArray.pop(len(tempArray) - 1)

def CombinationsWithoutRepitition(array, tempArray, r):

    if len(tempArray) == r:
        
        combinationExists = False
        for combination in combinations:
            if set(list(combination)) == set(tempArray):
                combinationExists = True

        if not combinationExists:
            combinations.append("".join(tempArray))

    else:    

        for x in range(0, len(array)):
            if not array[x] in tempArray:
                tempArray.append(array[x])
                CombinationsWithoutRepitition(array, tempArray, r)
                tempArray.pop(len(tempArray) - 1)

arr = ['a', 'b', 'c', 'd']

CombinationsWithRepitition(arr, [], 3)
print(combinations)
print("Count: " + str(len(combinations)))

combinations = []

CombinationsWithoutRepitition(arr, [], 3)
print(combinations)
print("Count: " + str(len(combinations)))

