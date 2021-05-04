permutations = []

def GeneratePermutations(array, start, end):

    current = 0

    if start >= end:

        permutations.append(list("".join(array)))

    else:

        for current in range(start, end):
            
            array[start], array[current] = array[current], array[start]            
            GeneratePermutations(array, start + 1, end)            
            array[start], array[current] = array[current], array[start]

    return permutations

def Permutations(array):

    return GeneratePermutations(array, 0, len(array))