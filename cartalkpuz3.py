__author__ = "Thomas D'Alleva"
# NOTE:
# looks for palindrones between the ages of a parent and child.
# program is seeded with the ages in the puzzle parent 73  and child 37

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
 #       print i, j
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def is_palindrome(age1, age2):
    """

    """
    first = str(age1)
    second = str(age2)
    if first[::-1] == second: # check the string reversed with the odometer string for palindrome
        # print "Palindrone is %s" % od
        return True
    else:
        return False


def mainRoutine(diff):

    count = diff
    age1 = diff
    age2 = 0

    while count < 100:
        if is_palindrome(age1, age2):
            print age1, age2
        age1 += 1
        age2 += 1
        count += 1


print "Checking age palindrones"
mainRoutine(73-37)
print " End of check"