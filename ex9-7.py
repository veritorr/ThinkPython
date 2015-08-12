__author__ = "Thomas D'Alleva"
# NOTE:
# find a word with 3 consecutive double letters.
# from Car Talk puzzle www.cartalk.com/content/puzzler/transcrips/200725


def consecDouble(word):
    pair = 0
    length = len(word)
    if length < 6:
        return False
    for x in range(0, (length - 1)):

        if (word[x] == word[x+1] and
        word[x+2] == word[x+3] and
        word[x+4] == word[x+5]):
            return True
        if x + 6 >= length:
            break

    return False



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

dcounter = 0

for line in fin:
    word = line.strip()
    if consecDouble(word):
        print "This word: %s, has 3 consecutive double letters!!!" % word
        dcounter += 1


print "End of search! We found %r words with 3 consecutive double letters." % dcounter