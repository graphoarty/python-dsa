# T = 'ababcabcabababd'
# PString = 'ababd'

def KnuthMorrisPrattSearch(PString, T):
    
    # Create Map
    PMap = []

    # Append Empty 0th Element (see theory)
    PMap.append(0)

    # Enter Empty 1st Element
    PMap.append(0)

    # Create List P (PString mirror) with Empty 0th Element
    P = []
    P.append(0)
    P.append(PString[0])

    # Create Map
    j = 0
    for i in range(1, len(PString)):
        if PString[i] == PString[j]:
            PMap.append(j + 1)
            j += 1
        else:
            PMap.append(0)
            j = 0
        P.append(PString[i])

    # Start Matching
    j = 0
    i = 0
    while i < len(T):

        # If equal, move both i and j forward
        if T[i] == P[j + 1]:

            i += 1
            j += 1

            if j == len(PString):
                return (i - len(P) + 1)
                break

        else:

            # If j is not zero, pick from Map
            # Else if j is zero, move i forward
            if j != 0:
                j = PMap[j]
            else:
                i += 1

    return -1