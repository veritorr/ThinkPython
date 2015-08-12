__author__ = 'Thomas'

'''
Takes a string and a nummber and does a simple encryption
'''


def rotate_word(s, num):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for c in s:

        index = alpha.find(c) + num
        if index > 25:
            index = 0 + num
        if index < 0:
            index = 26 + index

        letter = alpha[index]

        print letter,

# word = "melon"
# num = -10
# rotate_word(word, num)
# # answer = c u b e d


word = raw_input("enter a word: ")
num = raw_input("enter a number:")
rotate_word(word, int(num))









