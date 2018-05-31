
def integerPartition(number):

    number = number + 1

    '''
    {
        Create a partition matrix for solving this task using Dynamic Programming.
        The line mentioned below creates a partition matrix that is number x number in
        width and height.
    }
    '''
    partitionMatrix = [ [0] * number for x in xrange(number) ]

    for summandIndex in range(0, number):
        partitionMatrix[summandIndex][0] = 1

    for summandIndex in range(1, number):
        for numberIndex in range(1, number):
            
            if summandIndex > numberIndex:
                
                partitionMatrix[summandIndex][numberIndex] = partitionMatrix[summandIndex - 1][numberIndex]

            else:
                
                combosWithoutSummand = partitionMatrix[summandIndex - 1][numberIndex];
                combosWithSummand = partitionMatrix[summandIndex][numberIndex - summandIndex];

                partitionMatrix[summandIndex][numberIndex] = combosWithoutSummand + combosWithSummand;

    
    return partitionMatrix

partitionMatrix = integerPartition(5)

for x in range(0, len(partitionMatrix)):
    print(partitionMatrix[x])

