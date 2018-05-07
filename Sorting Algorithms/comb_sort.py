
# This function takes the value of the current inc
# divides it with the value of 1.3.
# 1.3 in this case is an arbitrary value that 'science' found
# to be the most ideal to be used in this case
def RecalibrateInc(inc):

    # divide the value of inc by 1.3 and then give
    # the value to inc
    inc = inc / 1.3

    # I don't know what to write as a comment here
    return 1 if inc < 1 else int(inc)
 
def CombSort(array):
 
    inc = len(array)
    swap = True
 
    while not inc == 1 or swap == True:
 
        inc = RecalibrateInc(inc)
        swap = False
 
        for i in range(0, len(array) - inc):
            if array[i] > array[i + inc]:
                array[i], array[i + inc] = array[i + inc], array[i]
                swap = True
 
# The array on which you will operate
array = [ 8, 4, 1, 3, -44 ]

# Start Combing
CombSort(array)

# Print the array
print(array)