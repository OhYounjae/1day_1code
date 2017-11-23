def findminIdx (nbrs, start):
    minval = nbrs[start]
    minidx = start
    for i in range(start + 1, len(nbrs)):
        if (minval > nbrs[i]):
            minval = nbrs[i]
            minidx = i
    return minidx


a = [4, 1, 3, 5, 2]

for curPos in range(len(a)):
    result = findminIdx(a, curPos)
    # temp = a[curPos]
    # a[curPos] = a[result]
    # a[result] = temp
    a[curPos], a[result] = a[result], a[curPos]
    print(a)


