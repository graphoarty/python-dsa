permutations = []

def GeneratePermutations(array, start, end):

    current = 0

    if start == end - 1:
        
        # -----------------
        # Without repitition
        arrString = "".join(array)
        if not arrString in permutations:
            permutations.append(arrString)
        # -----------------
        # or
        # -----------------
        # With repitition
        # permutations.append("".join(array))
        # -----------------

    else:
        for current in range(start, end):
            array[start], array[current] = array[current], array[start]
            GeneratePermutations(array, start + 1, end)
            array[current], array[start] = array[start], array[current]


arr = ['a', 'b', 'c', 'c']
GeneratePermutations(arr, 0, len(arr))
print(permutations)
print(len(permutations))