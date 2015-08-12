__author__ = "Thomas D'Alleva"

def nested_sum(L):
    total = 0
    for x in L:
        total += add_nest(x)
    return total


def add_nest(sublist):
    total = 0
    for x in sublist:
        total += x
    return total
def check_ans(x):
    ans = 0
    for i in range(x):
        ans += (1 + i)

    return ans


subList = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15]]
total = nested_sum(subList)

print "the total for %s is %s " % (subList[:],  str(total))
print "the right answer should be %s" % str(check_ans(15))