def printTable(inList):
    maxLen = 0
    for L1 in range(0, len(inList)):
        for L2 in range(0, len(inList[L1])):
            if maxLen < len(inList[L1][L2]):
                maxLen = len(inList[L1][L2])

    # print(maxLen)
    inLen = len(inList[0])

    for L2 in range(0, inLen):
        for L1 in range(0, len(inList)):
            print(inList[L1][L2].rjust(maxLen+1), end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
