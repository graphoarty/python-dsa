def cycleSort(array):

    writes = 0

    # [  26, 68, 79, 42, 48  ]

    for cycleStart in range(0, len(array) - 1):

        # [  26, 42, 48, 68, 79  ]
        # cycleStart = 3
        # item = 79
        # pos = 0

        item = array[cycleStart]

        pos = cycleStart # pos = 2 + 2 = 4
        for i in range(cycleStart + 1, len(array)): # i = 4 -> 5
            if array[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        # duplicates
        while item == array[pos]:
            pos += 1

        # swapping
        array[pos], item = item, array[pos]
        writes += 1

        # [  26, 42, 48, 68, 79  ]
        # cycleStart = 2
        # item = 79
        # pos = 2

        while pos != cycleStart:

            pos = cycleStart 
            for i in range(cycleStart + 1, len(array)): # i = 3 -> 5
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]
            writes += 1

    return array, writes

print(cycleSort( [  26, 68,	79,	42,	48  ] ) [0])
