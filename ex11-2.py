__author__ = "Thomas D'Alleva"
# moves words in words.txt to keys in a dictionary
# allows checks to see if if a word exists in the dictionary.

# builds a histogram of a word entered by the user.

def historgram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return (d)
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def print_hist(h):

    for c in h:
        print c, h[c]


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
# print "The dictionary  has the following word: %s" % inword in wordDict
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
print "=============="
r = invert_dict(d)
print (r)

