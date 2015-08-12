__author__ = "Thomas D'Alleva"

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

def is_palindrome(word1, word2):
    print word1[::1]
    print word2[::-1]
    return ('True' if word1[::1] == word2[::-1] else 'False')


ans = is_reverse('abcdef', 'fedcba')
print ans

ansb = is_palindrome('hannah', 'hannah')
print ansb