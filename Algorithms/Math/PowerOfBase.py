'''
{
    Okay, so hey guys, it's Quinston and today we are going talk about how to check if a number is a power of a particular base. What is a power and what is a base is the most obvious next question. A base could be a regular number. It could be 2, 3, 44, 89. Whatever. A power is obtained when you multiply the base with itself n number of times, where n could range from upwards of 2.

    For example, if 2 is your base. The power could be 4, because 2 times 2 is 4. It could also be 8, because 2 times 2 times 2 is 8.

    Also, just to be clear, the power is a set of numbers, and not just one number.

    So, this program basically checks if the power that you passed in is composed of the base that you passed in.                                    
    There are multiple ways to do this, and this is just one of them. Let's take a look at the code.

    Let's take an example.

    Assume you have the power 8 and the base 2. The way the algorithm works is that you test if the power divides perfectly with the base. This means that you need to divide 8 by 2 and check if the remainder is 0. If the remainder is zero, it obviously means that the power is completely divisible by the base. But, that does not mean that the power is a multiple of the base. They could just be numbers that are divisible by one another. So, you need to get the quotient from power divided by base and test again until you have completely reduced the power to 1.

    We use the modulus operator in this case. 

    8 mod 2 gives us 0 - hence 2 is completely divisible by 8
    next power = 8 / 2 = 4
    4 % 2 gives us 0 - hence 2 is completely divisible by 4
    next power = 4 / 2 = 2
    2 % 2 gives us 0 - hence 2 is completely divisible by 2
    next power = 2 / 2 = 1

    If you get 1, it means that the power is a multiple of the base. If you do not get the remainder as 0 at any of the conditions, it means that the power is not a multiple of the base.

    Let's take a look at the code.

}
'''


'''
{
    Here is the main function that runs, it's called isPowerOfBase. Nothing fancy. Now, it takes in two parameters. The first one is power, which is basically the power and the second one is base. 
}
'''
def isPowerOfBase(power, base):

    '''
    {
        If the power is 1 then you return False as 1 is not a power of anything. 1 times 1 is 1. So, you can't really achieve anything here. Also, the same argument goes for zero. On top of that, we are not dealing with negative numbers, which are also covered in this condition. Any number that is one and below one is disqualified.
    }
    '''
    if power <= 1:
        return False

    '''
    {
        Next, we basically check and run a loop while power is not equal to one. We use the value of power as our condition.
    }
    '''
    while not power == 1:

        '''
        {
            Now, here, we are basically checking if the power divides perfectly with the base. The reason we need to check this, is that, if it does not divide perfectly then the power is clearly not a multiple of the base. Hence, you return False. We use the modulus operator in this case, simply because the modulus operator gives us the remainder, and if the remainder is zero, it means that the divisor divides perfectly with the divient.
        }
        '''
        if not power % base == 0:
            return False

        '''
        {
            Now, to move to the next loop, we need to change the power. We divide the power with the base and store the value in the variable power. Imagine this as the base being chipped away from the power until nothing remains. The power is a multiple of the base. And this is a good way to test it at every step.
        }
        '''
        power = power / base

    return True

print(isPowerOfBase(1, 2))

