__author__ = "Thomas D'Alleva"
# NOTE:
# palindromic odometer puzzle
# from Car Talk puzzle www.cartalk.com/content/puzzler/transcripts/20083
# 6 digit odometer e.g. 300000
# 1st:  last four digits are palindromatic eg. 315445
# 2nd:  one mile later the last 5 digits were palindromatic eg. 365456
# 3rd: one mile later the middle for numbers were palindromatic.
# 4th: one mile later all 6 numbers were palindromatic.

# What was the on the initial odometer reading?


# compare two words and return True if one word is reverse of the other

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

def is_palindrome(num, start, length):
    """
    :param num: feed in 6 digit odometer numbers
    :param start: parse where to start palindrone check
    :param length: parse where to end palindrone check
    :return: True == palindrone, False == not a palindrone
    """
    od = str(num)[start:start+length] # slice from and including start index to one short of length index
    if od[::-1] == od: # check the string reversed with the odometer string for palindrome
        # print "Palindrone is %s" % od
        return True
    else:
        return False


def parseRules(od):
    if (is_palindrome(od, 2, 4) and  # check last 4 digits
    is_palindrome(od+1, 1, 5) and  # add a mile, check last 5 digits
    is_palindrome(od+2, 1, 4) and  # add a mile, and check middle 4 digits
    is_palindrome(od+3, 0, 6)):  # add another mile and the whole odometer becomes a palindrone!
         print "Here's one that worked!"
         return True
    else:
        return False



def mainRoutine():
    od = 100000
    while od <= 999999:
        if parseRules(od):
            print od
        od += 1


print "Odometer settings that satisfy rules"
mainRoutine()
print " End of check"