
def Factorial(x):

    if x < 2:
        return 1
    else:
        return x * Factorial(x - 1)
