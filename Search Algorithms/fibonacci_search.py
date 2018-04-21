# return the fibonacci number at the index of n
def FibonacciGenerator(n):
    if n < 1: return 0
    elif n == 1: return 1
    else: return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

# return the index at which x exists inside arr
# return -1 otherwise
def FibonacciSearch(arr, x):

    # find the smallest Fibonacci number greater than or equal 
    # to the length of arr
    m = 0
    while FibonacciGenerator(m) < len(arr):
        m = m + 1

    # m now contains the index of the the smallest Fibonacci
    # number greater than or equal to the length of tha array
    # for example
    # if the length of arr is 10, FibonacciGenerator(m) should be 13
    
    # this is the length of that array from the 
    # start that has been eliminated
    offset = -1
 
    # make sure you fibonacci index is valid
    while (FibonacciGenerator(m) > 1):
         
        # 1. you are generating a number greater the length
        # of the array the first time you run it
        # 2. you're adding it with the offset
        # 3. you're comparing it with the length of the array
        # 4. after running for the first time, you will always
        # get returned the first parameter of min()
        i = min(offset + FibonacciGenerator(m - 2), len(arr) - 1)
 
        # if the value you are searching for is greater than the 
        # current arr[i], then it clearly means that you need to 
        # shift your focus to the elements that are beyond arr[i]
        # move the three fibonacci variables one fibonacci down. 
        # Reset offset to index. Together these indicate elimination
        # of approximately front one-third of the remaining array.
        if (x > arr[i]):

            m = m - 1
            offset = i
 
        # if the value you are searching for is less than the 
        # current arr[i], then it clearly means that you need to 
        # shift your focus to the elements that are before arr[i]
        # move the three fibonacci variables two fibonacci down, 
        # indicating elimination of approximately rear two-third 
        # of the remaining array
        elif (x < arr[i]):

            m = m - 2
 
        # naturally if both the values are the same, then you
        # have reached your answer and you can then return the
        # the index of the array
        else :

            return i
 
    # this will run if there is one last element left
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
 
    # return -1 if the element doesn't exist in the array
    return -1


# the search array
arr = [ 10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130 ]
x = 10
print(FibonacciSearch(arr, x))
