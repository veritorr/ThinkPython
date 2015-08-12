__author__ = "Thomas D'Alleva"
# moves words in words.txt to keys in a dictionary
# allows checks to see if if a word exists in the dictionary.

# build a histogram

def historgram(s):
    d = dict()
    newd = dict()
    for c in s:
        newd[c] = s[c]
        d[c] = 1 + d.get(c, 0)
    return (d)

def print_hist(h):

    for c in h:
        print c, h[c]

    print "Keys = %s" % h.keys()


fin = open('words.txt')
loopcounter = 0

wordDict = dict()

# for line in fin:
#     word = line.strip() # removes white space
#
#     wordDict[line] = word.strip("\n")
#
#     loopcounter += 1
#     if loopcounter > 20:
#         break

inword = raw_input("Enter word to check")
#
# print "Checking %s" % inword
#
# print "The dictionary has the following word: %s" % inword in wordDict
#
# if inword + "\n" in wordDict:
#     print "Word exists in dictionary!!!"
# else:
#     print "Word does not exist in dictionary!"
#
# print "the histogram for string %s is as follows: " % inword
# print "++++++++++++++++++"
d = historgram(inword)
print "=============="
print_hist(d)


