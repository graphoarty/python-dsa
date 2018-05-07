# [0, 1, 1, 2, 3, 5, 8, 13...]

# return the fibonacci number at the index of n
def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

# return the index at which x exists inside arr
# return -1 otherwise

def FibonacciSearch(arr, x):

    # find the smallest Fibonacci number greater than or equal
    # to the length of arr
    m = 0 
    while FibonacciGenerator(m) < len(arr): # 
        m = m + 1 

    # [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130] 
    # m = 7

    # m now contains the index of the the smallest Fibonacci
    # number greater than or equal to the length of the array
    # for example
    # if the length of arr is 11, FibonacciGenerator(m) should be 13

    # this is the length of that array from the
    # start that has been eliminated
    offset = -1

    # [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130] 
    # m = 7
    # offset = -1

    # make sure you fibonacci index is valid
    while (FibonacciGenerator(m) > 1):

        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)

        # [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130] 
        # m = 3
        # offset = 5
        # i = 6
        # x = 60

        if (x > arr[i]):

            m = m - 1
            offset = i

        elif (x < arr[i]):

            m = m - 2

        else:

            return i

    # this will run if there is one last element left
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1

    # return -1 if the element doesn't exist in the array
    return -1


# the search array
arr = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130] 
x = 60
print(FibonacciSearch(arr, x))
