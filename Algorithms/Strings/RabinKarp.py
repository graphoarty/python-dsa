# T = 'aacabababaabc'
# P = 'abc'

# Returns index of first instance string patten P in string T
# Returns -1 if not found
def RabinKarpSearch(P, T):

    # d is the multiplier and q is the mod
    d = 265
    q = 101

    # p is the hash for the pattern
    p = 0

    # t is the rolling hash for the substring
    t = 0

    # h is multiplier to assist removing higher order number
    h = 1

    # len(P) - 1 as we only need d^m-1 where m is length of pattern (refer theory)
    for i in range(0, len(P) - 1):

        h = ( d * h ) % q

    # loop to find first hash before we start rolling t
    for i in range(0, len(P)):

        p = ( d * p + ord(P[i]) ) % q
        t = ( d * t + ord(T[i]) ) % q

    # start calculating rolling hash
    for s in range(0, len(T) - len(P) + 1):

        # if hashes are equal we found a hit
        if t == p:

            for x in range(0, len(P)):

                # check if all characters are same (double tap)
                if T[s + x] == P[x]:

                    if x == len(P) - 1:

                        return s

                else:

                    break


        if s < len(T) - len(P):

            # roll, roll, roll the hash (refer theory)
            t = (d * (t - ord(T[s]) * h) + ord(T[s + len(P)])) % q

            # if t is negative, attempt revival
            if t < 0:
                t += q

    return -1