__author__ = "Thomas D'Alleva"
# NOTE:
# Spent more time trying to figure out how to format a percentage correctly
# then writing the logic of the program.
# I'm sure there is a way better way but for now this will due.
# The better way might mean switching to Python 3.x

def check_no_e(word):
    for char in word:
        if char == 'e' or char == 'E':
            return False
    return True

def is_abecedarian(word):
    for x in range(0, len(word)):
        if word[x] > word[x+1]:
            return False
    return True



fin = open('words.txt')
counter = 0.0
ecounter = 0.0
total = 0.0
percent = 0.0
epercent = 0.0
for line in fin:
    word = line.strip()
    if check_no_e(word):
      #  print "There are no e's in %s" % word
        counter += 1
    else:
        ecounter += 1
       # print "There are words with 'e': %s" % word
print "There are %r words with no letter 'E' " % int(counter)
print "There are %r words with letter 'E' " % int(ecounter)
total = counter + ecounter
percent = counter / total
epercent = ecounter / total
print "the percentage of words without 'e' is: {0:1.2%}".format(percent)
#print "%"
print "the percentage of words with 'e' is: {0:1.2%}".format(epercent)
# print "%"


