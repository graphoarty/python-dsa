
def RecursiveSearch( searchArray, index, valueOfNumberToFind):
    
    if index >= len(searchArray):
        return -1
    
    if searchArray[index] == valueOfNumberToFind:
        return index + 1

    return RecursiveSearch(searchArray, index + 1, valueOfNumberToFind)
 

searchArray = [12, 34, 54, 2, 3]
valueOfNumberToFind = 3

print(RecursiveSearch(searchArray, 0, valueOfNumberToFind))
