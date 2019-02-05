
'''
{
    This is the recursive function that you call to process
    the numbers continuously. For simplicity, the numbers in this case
    are called a and b. You can call them whatever you want, obviously.
}
'''
def EuclideanGCD(a, b):

    '''
    {
        We take the absolutes of a and b, and pop them back
        into a and b. We do this because we want to deal with
        non-negative numbers.
    }
    '''
    a = abs(a)
    b = abs(b)

    '''
    {
        The three conditions below are the recursive base conditions,
        which are put to end the recursive loop and return the correct
        answer. 

        When a and b are both 0, it basically means that the two numbers,
        don't really have a GCD, which might happen.
    }
    '''
    if a == 0 and b == 0:
        return None
        
    '''
    {
        When a is zero, it means that the GCD is stored in b,
        as we saw in the example.
    }
    '''
    if a == 0 and not b == 0:
        return b

    '''
    {
        Vice versa, when b is zero, the GCD is stored in a.
    }
    '''
    if not a == 0 and b == 0:
        return a

    '''
    {
        The algorithm is applied FROM the larger number 
        TO the smaller number. Always subtract the smaller
        from the larger number. So, to check which number
        is larger, we use this little condition.
    }
    '''
    if a > b:

        '''
        {
            So, I know we said subtraction, but repeated subtraction
            without extra conditions can cause computational issue.
            Using the modulus operator makes our life much simpler.
            The modulus operator gets us the remainder 
            of the first number divided with the second number, which 
            essentially means subtracting the second number from the 
            first number until you cannot subtract further. Hence, your
            remainder.

            Once you get the remainder, you just pass it into the function.
        }
        '''
        return EuclideanGCD(a % b, b)
    
    else:

        '''
        {
            If the second number is bigger or equal to the first, this is what gets called.
        }
        '''
        return EuclideanGCD(b % a, a)


# Example Function Call
print(EuclideanGCD(49, 21))


# 49 , 21 => GCD is 7
# 28 , 21 => GCD is 7
# 7 , 21 => GCD is 7
# 7 , 14 => GCD is 7
# 7 , 7 => GCD is 7




