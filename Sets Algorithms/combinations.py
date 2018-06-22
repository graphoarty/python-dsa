combinations = []

def CombinationsWithRepitition(array, tempArray, r, i):

    if len(tempArray) == r:
        
        combinations.append("".join(tempArray))

    else:    

        for x in range(0, len(array)):
            tempArray.append(array[x])
            CombinationsWithRepitition(array, tempArray, r, i + 1)
            tempArray.pop(len(tempArray) - 1)

def CombinationsWithoutRepitition(array, tempArray, r, i):

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
                CombinationsWithoutRepitition(array, tempArray, r, i + 1)
                tempArray.pop(len(tempArray) - 1)

arr = ['a', 'b', 'c']

CombinationsWithoutRepitition(arr, [], 3, 0)

print(combinations)
print(len(combinations))
print(set([1, 2, 4]) == set([4, 2, 1]))
