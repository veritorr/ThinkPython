__author__ = "Thomas D'Alleva"
# NOTE:
# adds a function that checks to see of the letters
# in a word are in alphabetical order.

def check_no_e(word):
    for char in word:
        if char == 'e' or char == 'E':
            return False
    return True

def is_abecedarian(word):
    for x in range(0, (len(word) - 1)):
        if word[x] > word[x+1]:
            return False
    return True

    

fin = open('words.txt')
loopcounter = 0
acounter = 0
ncounter = 0
total = 0.0
percent = 0.0
epercent = 0.0
for line in fin:
    word = line.strip()
    loopcounter += 1
    if is_abecedarian(word):
        print "The word %s is an abcedarian word!!!" % word
        acounter += 1
    else:
        ncounter += 1
        print "This word is not in alphabetical order: %s" % word

    if loopcounter >= 20:
        break
    else:
        continue


print "There are %r words in alphabetical order " % int(acounter)
print "There are %r words not in alphabetical order " % int(ncounter)
"""
total = counter + ecounter
percent = counter / total
epercent = ecounter / total
print "the percentage of words without 'e' is: {0:1.2%}".format(percent)
#print "%"
print "the percentage of words with 'e' is: {0:1.2%}".format(epercent)
# print "%"
"""

