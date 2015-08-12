__author__ = "Thomas D'Alleva"
# moves words in words.txt to keys in a dictionary
# allows checks to see if if a word exists in the dictionary.

# build a histogram

def historgram(str):
    d = dict()
    for chara in str:
        if chara not in d:
            d[chara] = 1
        else:
            d[chara] += 1

    return (d)





fin = open('words.txt')
loopcounter = 0

wordDict = dict()

for line in fin:
    word = line.strip() # removes white space

    wordDict[line] = word.strip("\n")

    if loopcounter > 10 and loopcounter < 20:
        print word
    loopcounter += 1
    if loopcounter > 30:
        break

inword = raw_input("Enter word to check")
print "Checking %s" % inword

print "The dictionary has the following word: %s" % inword in wordDict

if inword + "\n" in wordDict:
    print "Word exists in dictionary!!!"
else:
    print "Word does not exist in dictionary!"

print wordDict
