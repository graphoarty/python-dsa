import os
from shutil import copy

def main():

    path = []

    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR001/A0011683")
    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR002/A0021683")
    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR003/A0031683")
    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR004/A0041683")
    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR005/A0051683")
    path.append("/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/100AR006/A0061683")

    processedPath  = "/Users/apple/Desktop/Ashiana Town Day 2 Batch 3/Processed"

    if not os.path.exists(processedPath):
        os.makedirs(processedPath)

    if not os.path.exists(processedPath):
        print("Folder Could Not Be Created")

    numberOfFiles = 31

    i = 0
    while i < numberOfFiles:

        if not os.path.exists(processedPath + "/" + str(i)):
            os.makedirs(processedPath + "/" + str(i))

        try:
            for x in range(6):
                print("Copy From " + path[x] + ".jpg" + " - " + processedPath + "/" + str(i))
                copy(path[x] + ".jpg", processedPath + "/" + str(i))
            i = i + 1
        except:
            print("Could Not Do Much")

        for x in range(6):
            path[x] = incrementPath(path[x])

def incrementPath(stringNum):
    strList = list(stringNum)
    pre = stringNum[0:-4]
    number = int((strList[len(strList) - 1] + strList[len(strList) - 2] + strList[len(strList) - 3] + strList[len(strList) - 4])[::-1])
    number = number + 1
    strNum = str(number)
    while(len(strNum) != 4):
        strNum = "0" + strNum
    return pre + strNum

if __name__ == "__main__":
    main()