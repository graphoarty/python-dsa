

def EuclideanGCD(a, b):

    a = abs(a);
    b = abs(b);

    if a == 0 and b == 0:
        return None
        
    if a == 0 and not b == 0:
        return b

    if not a == 0 and b == 0:
        return a

    # Normally we need to do subtraction (a - b) but to prevent
    # recursion occurs to often we may shorten subtraction to (a % b).
    # Since (a % b) is normally means that we've subtracted b from a
    # many times until the difference became less then a.

    if a > b:
        return EuclideanGCD(a % b, b)
    
    return EuclideanGCD(b % a, a)

print(EuclideanGCD(252, 105))