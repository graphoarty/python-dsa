'''
{
 
    According to Number Theory and Combinatorics, a partition of a positive integer is a way of writing the number as a sum of multiple positive integers. For example, if we take a positive integer number like 4. We can express 4 as 
    
    4 (we count the value of the integer itself also as a seperate combination)
    3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
    
    Hence, the number of integer partitions for 4 are 5.

    If you observe, 2 + 1 + 1 can also be represented as 1 + 1 + 2, 1 + 2 + 1. But in this algorithm we will not consider the order in which the numbers occur but the values of the numbers themselves. So basically, order is not important.

    Another way of thinking about this is that we will consider combinations and not permutations.

    The Integer Partition Algorithm helps you calculate the number of combinations that are available for a particular number. For example if you pass 4 into the algorithm you'll get 5 as the answer as 5 combinations are available for 4.

    Let's take a closer look at how this algorithm actually generates the combinations for the partition of an integer. We do it by creating a 2D Array or another name for it could be a Matrix.

    For example, if we create a partition matrix for the number 5. It will look something like this.
        
      Y   0  1  2  3  4  5
    X       
    0   [ 0, 0, 0, 0, 0, 0 ]
    1   [ 0, 0, 0, 0, 0, 0 ]
    2   [ 0, 0, 0, 0, 0, 0 ]
    3   [ 0, 0, 0, 0, 0, 0 ]
    4   [ 0, 0, 0, 0, 0, 0 ]
    5   [ 0, 0, 0, 0, 0, 0 ]

    In this matrix, the horizontal or Y indexes denote the sum that we have to create and the vertical indexes or X denote the summands which help us generate the sum (if you don't know what a summand is... summands are the actual numbers that you add to get the sum. For example, if you add 1 + 3 = 4. 1 and 3 are the summands and 4 is the sum). So basically, we are going to use the vertical summands to generate the horizontal sums. The algorithm that we use here is based on Dymanic Programming. The paradigm by which Dynamic Programming operates is by breaking the bigger problem into smaller problems, then solving those problems and then storing the results obtained. The results can then be fetched to later help solve the bigger problem. That is exactly what we are gonna do in this case.

    Now, as the first index of Y is 0, so we need to create a sum of 0 from the first summand in X which is also 0. The number of combinations in which we can achieve 0 from 0 is 1 because 0 has no value and cannot be broken down any futher.
    
      Y   0  1  2  3  4  5
    X       
    0   [ 1, 0, 0, 0, 0, 0 ]
    1   [ 0, 0, 0, 0, 0, 0 ]
    2   [ 0, 0, 0, 0, 0, 0 ]
    3   [ 0, 0, 0, 0, 0, 0 ]
    4   [ 0, 0, 0, 0, 0, 0 ]
    5   [ 0, 0, 0, 0, 0, 0 ]

    The next sum that we need to create from 0 is 1. Now, if you think about it, that is kind of impossible because 0 literally has no value. This means that there are no combinations that will lead us to create 1 from 0. Similary, if we consider the next sums to create from 0 i.e., 2, 3, 4, 5. They will also suffer the same fate because you cannot create either of them from 0. Hence, the number of combinations there will also be 0.

    Hence, our first row is solved.

    The way we solve the next row is interesting because now, we not only have 1 but actually 2 numbers to choose from which are {0, 1} to create our sum. For the first number we have to create a sum of 0 from {0, 1}. The tricky part here is that there is no way you can create a sum of 0 from 1. So the only way to do this is with 0 which give us only 1 combination. 

    Next, we create 1 from {0, 1}. We cannot create 1 from 0 but we can create 1 from 1. Hence, that is our single combination.

    Similarly, we can create 2 from {0, 1} in only one way which 1 + 1 because the only other number available to us is 0. The reason we are using 2 1s in this case is because we assume, in this algorithm, that we have an unlimited supply of the summands which in this particular case was using multiple 1s for creating our combinations. Same goes for 3 which is 1 + 1 + 1, 4 which is 1 + 1 + 1 + 1 and 5 which is 1 + 1 + 1 + 1 + 1 respectively. If you observe, the entire row is filled with 1s. Let's move on to the next row.

      Y   0  1  2  3  4  5
    X       
    0   [ 1, 0, 0, 0, 0, 0 ]
    1   [ 1, 1, 1, 1, 1, 1 ]
    2   [ 0, 0, 0, 0, 0, 0 ]
    3   [ 0, 0, 0, 0, 0, 0 ]
    4   [ 0, 0, 0, 0, 0, 0 ]
    5   [ 0, 0, 0, 0, 0, 0 ]

    In the next row, we have access to the summands {0, 1, 2}. So, to create the first number we will need to generate 0 from {0, 1, 2}. Now, we know for a fact that we will not be able to use 2 or 1 in this case to create the sum. This is simply because 2 and 1 are bigger than 0. So, there is only 1 combination as seen previously. But, we can actually use a shortcut in this case and not have to logically assess this every single time as we have the answers to the pervious test cases stored in the partition matrix. So, the shortcut basically is, 

    SC1: If the sum is less than the summand considered, just fill the empty field considered by the value directly above it.

    Hence we fill, [2, 0] with 1 and we fill [2, 1] with 1 considering the fact that the summands are greater than the sum.

      Y   0  1  2  3  4  5
    X       
    0   [ 1, 0, 0, 0, 0, 0 ]
    1   [ 1, 1, 1, 1, 1, 1 ]
    2   [ 1, 1, 0, 0, 0, 0 ]
    3   [ 0, 0, 0, 0, 0, 0 ]
    4   [ 0, 0, 0, 0, 0, 0 ]
    5   [ 0, 0, 0, 0, 0, 0 ]

    So, now we are at a point where we need to create 2 from {0, 1, 2}. So, the algorithm states, to tackle this sort of a field.

    1. Find the combinations excluding the current summand.
    2. Find the combinations including the current summand.
    3. The total combinations will be the sum of the both above.

    So, first we need to find the combintions excluding the current summand which in this case is 2. So we need to find the combinations to create 2 from {0, 1} (here is where we excluded 2). The fact that we are using Dynamic Programming helps us immensely in this case because if you are paying attention, we already have the answer to this sitting in the field [1, 2] which is 1.

    Now, if we were to include 2 in the set, we would need to generate 2 from {0, 1, 2}. Now we can generate an equation like 2 + 0 = 2 which means that we only need to find the number of ways in which we can generate 0 from {0,, 1, 2}. This combination has already been solved and is ready at the field [2, 0] which is 1. 

    By adding the excluded and included values for generating 2 from {0, 1, 2} we get the answer, 1 + 1 which is 2. So, we fill in the field [2, 2] with 2. Similarly, we now have to generate 3 from {0, 1, 2}. Hence, we use the same priciples of exclusion and inclusion. 
    
    Now, there is another shortcut that we can use in this case, and that is the fact that during step of exclusion of the current summand which in this case is generating 3 from {0, 1}. If you observe closely, notice that the number that we always end up copying is always above the current field considered. Hence, the algorithm states that,

    SC2: The combinations of excluding the current summand are present above the current field.

    So, in this field that we are currently considering, the excluded combinations are 1. 

    For the included combinations, we need to create 3 from {0, 1, 2}. One of the ways in which we can do this is 2 + 1 = 3. Remember that we have an unlimited supply of summands always. So, the number of combinations needed are generating 1 from {0, 1, 2}. So, the number of combinations for that is already calculated at the field [2, 1] which is 1. 

    So, the total combinations become 1 + 1 which is 2. Hence, the field [2, 3]in the partition matrix is filled with 2. 

      Y   0  1  2  3  4  5
    X       
    0   [ 1, 0, 0, 0, 0, 0 ]
    1   [ 1, 1, 1, 1, 1, 1 ]
    2   [ 1, 1, 2, 2, 3, 0 ]
    3   [ 0, 0, 0, 0, 0, 0 ]
    4   [ 0, 0, 0, 0, 0, 0 ]
    5   [ 0, 0, 0, 0, 0, 0 ]

    The next field [2, 4] need to be filled with the combinations of generating 4 from {0, 1, 2}. Using the excluding shortcut, we know the first addition value is 1. In order to generete the including addition value, we can, as usual take 2 + 2 = 4 and try to find the combinations for generating 2 from {0, 1, 2} or we can use another shortcut. This shortcut generates the second addition value. 
    
    SC3: The combinations of including the current summand can be calculated by subtracting the current sum from the current summand, which would give you an integer which we will denote by x. The number of combinations is the value at the field [current summand, x] of the partition matrix.

    In this case, the x value will be 4 - 2 which is 2. So, the field [2, 2] is 2. Hence, we get the values 1 + 2 which is 3. So the field [2, 4] is populated by 3. 

    The reason we use these 3 shortcuts is to enable to write the code for generating the partition matrix for this algorithm. Similarly, we can compute all of the other fields by using these shortcuts. Let's take a look at the code. 

}
'''

'''
{
    The function integerPartition takes a number and returns the total number if integer partition combinations generated for that number.
}
'''
def integerPartition(number):

    '''
    {
        Increment number by one so as to be able to use the original number as an index in the matrix. For example, if the original value of the number passed was 4. We would only consider 0, 1, 2, 3 in the range function. So, instead of adding + 1 to every range function, we can just add + 1 here and decrement later. 
    }
    '''
    number = number + 1

    '''
    {
        Create a partition matrix for solving this task using Dynamic Programming. The line mentioned below creates a partition matrix that is number by number in width and height. For example, if the value of number is 5 after incrementing, you will create a matrix of width by height of 5 by 5. So, this line is basically a short-cut
        for creating a 2D or bi-dimensional Array.

        Once more thing to realize is that, we have initialized all of the fields in the partitionMatrix to zero.

          Y   0  1  2  3  4  5
        X       
        0   [ 0, 0, 0, 0, 0, 0 ]
        1   [ 0, 0, 0, 0, 0, 0 ]
        2   [ 0, 0, 0, 0, 0, 0 ]
        3   [ 0, 0, 0, 0, 0, 0 ]
        4   [ 0, 0, 0, 0, 0, 0 ]
        5   [ 0, 0, 0, 0, 0, 0 ]...
        
    }
    '''
    partitionMatrix = [ [0] * number for x in xrange(number) ]

    '''
    {
        Now the we have solved an example, you would have realized that the first column of the partition matrix is always 1. Hence, this is what we are setting up here. The summandIndex is the value in the forloop which goes from the range 0 to number (excluding the number ofcourse). The first index is always row selection and second value is column selection in a 2D Array. 
    }
    '''
    for summandIndex in range(0, number):
        partitionMatrix[summandIndex][0] = 1

    '''
    {
        In these nested forloops we will apply the algorithms that we discussed in the examples. The summandIndex indicates the vertical index of the partition matrix and the numberIndex indicates the horizontal index of the partition matrix. We start the loop from 1, simply because we have already set the values for the first row and the first column in the previous steps.
    }
    '''
    for summandIndex in range(1, number):
        for numberIndex in range(1, number):
            
            if summandIndex > numberIndex:

                '''
                {
                    If the summand is greater than the sum, we just copy the value in the field above. The co-ordinates for the values in the field above are [summandIndex - 1][numberIndex]
                }
                '''
                partitionMatrix[summandIndex][numberIndex] = partitionMatrix[summandIndex - 1][numberIndex]

            else:

                '''
                {
                    If the summand is not greater than the sum, we find the combinations that include the current summand and exclude the current summand. We have the shortcuts available for finding them with the algorithms. 

                    For excluding the current summand, we just copy the value above it as usual.
                }
                '''
                combosWithoutSummand = partitionMatrix[summandIndex - 1][numberIndex]

                '''
                {
                    And for including the summand, we subtract the current sum which in this case is the number index from the summandIndex and that becomes our column indicator. Using the summandIndex as our row indicator we get our field value as [summandIndex][numberIndex - summandIndex]
                }
                '''
                combosWithSummand = partitionMatrix[summandIndex][numberIndex - summandIndex]

                '''
                {
                    Hence, we fill the value at partitionMatrix[summandIndex][numberIndex] by adding the combosWithoutSummand and combosWithSummand to get our answer.
                }
                '''
                partitionMatrix[summandIndex][numberIndex] = combosWithoutSummand + combosWithSummand

    '''
    {
        Decrement the number as mentioned above.
    }
    '''
    number = number - 1

    '''
    {
        Return the total number of combinations of integer partitions.
    }
    '''
    return partitionMatrix[number][number]


print(integerPartition(5))


