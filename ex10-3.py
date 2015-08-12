__author__ = "Thomas D'Alleva"

# accumulating numbers from a list

def accum(numList):
    total = 0
    totalList = []
    for i in numList:
        total += i
        totalList.append(total)
    return totalList

numList = [1, 2, 3, 4, 5, 4, 3, 2, 1]

Total = accum(numList)
print "The original number list is %s " % numList
print "The new accumulated total list is %s" % Total[:]


