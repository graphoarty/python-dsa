'''

The BitonicSort function does the job of recursively splitting the array into smaller and smaller pieces and then calling the BitonicMerge function on the splits along with passing the direction that the values need to be sorted into. The arguments which are put into the BitonicSort are the direction and the array. If the direction is True, then the array is supposed to be sorted in the increasing order of value and if the direction is false, then the array is supposed to be sorted in the decreasing order of values. Every recursive function contains a base case and this is the base case of the BitonicSort function.

'''

def BitonicSort(direction, arr):

    '''
    
    The obvious condition that we have over here is that is the length of the array is less than or equal to 1, then it makes no sense to call the BitonicMerge function on the array as it contains only one element.
    
    '''

    if len(arr) <= 1:

        return arr

    else: 

        '''

        When you split the array to form a Bitonic Sequence, you want the first half to be in an increasing order and the second half to be in a decreasing order. The booleans True and False respresent increasing and decreasing order of values respectively and this will become more obvious in the BitonicCompare functions. 

        '''

        first = BitonicSort(True, arr[:len(arr) // 2])
        second = BitonicSort(False, arr[len(arr) // 2:])

        '''

        This is the only line that might be a little confusing and the reason for this is very simple. When we looked at the example, we executed the increasing and decreasing sorting of the array to form Bitonic Sequences simultaneously. As it turns out, we are not following the same procedures here. In fact, these operations are being done at very different times in the execution of the array but don't let that confuse you. This is the part in the process where you move to the next stage and increase the size of the Bitonic Sequence in the array.

        '''

        return BitonicMerge(direction, first + second)


'''

The BitonicMerge function deals with driving the comparisons and recursively executes the passes of the current stage. 

'''

def BitonicMerge(direction, arr): 

    '''

    You cannot merge a single element and hence, we return the array that contains that element.

    '''

    if len(arr) == 1:
        return arr
    else:

        BitonicCompare(direction, arr)
        first = BitonicMerge(direction, arr[:len(arr) // 2])
        second = BitonicMerge(direction, arr[len(arr) // 2:])
        return first + second


'''

The BitonicCompare function takes in the direction along with the array and compares elements at a distance of half the length of array. The elements are swapped if they are not in the correct direction. There is no need to return the array as, in Python, data structurs are passed by reference and not by value. Arrays are data structures.

'''

def BitonicCompare(direction, arr):

    '''

    The comparison distance is half the length of the array.

    '''

    dist = len(arr) // 2
    
    for i in range(dist):  

        '''

        If the direction is True then the elements compared should be arranged in an increasing order. The condition below checks if the element arr[i] is greater then the element arr[i + dist]. The value of dist is always poritive which means that arr[i + dist] comes after arr[i]. So, if the direction is True and this condition is met, then it means that we need to swap as the arr[i] cannot be greater than array[i + dist] when increasing order values are in play. The exact opposite is executed when the direction is False.

        '''

        if (arr[i] > arr[i + dist]) == direction:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]


'''

The program starts execution from the definition of the array. The array contains the same values that we had taken as an example when discussing the workings of the algorithm. On the next line we have a function call which takes in two arguments. The first one is a boolean and the second one is the array itself. The return value of this function call is an array which we over-write into the array variable. The returned array, as most of you might have figured out, is the sorted array which we then proceed to print. These three lines are the drivers to starting the process of the Bitonic Sort. Let's see what the BitonicSort function actually does with the parameters that we have passed into it.

'''

array = [ 3, 7, 4, 8, 6, 2, 1, 5 ]
array = BitonicSort(True, array)
print(array)