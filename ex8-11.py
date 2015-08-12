__author__ = "Thomas D'Alleva"

def any_lowercase1(s):
    # returns a bool if a the first letter of string "s" is lower case
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # local variable c is never used
    # instead the literal character 'c' is used
    # and always returns the string 'True'
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # returns boolean True if the first character in string s is lower case
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s):
    # Tries  to iterate through s string and returns True or False depending on the last char of the string being lowercase
    # fails due to c.islower() is not correct bad indent level
    flag = False
    for c in s:
        # flag = flag or c.islower() intentionally commented out to avoid compiler error
     return flag

def any_lowercase5(s):
    # Returns False is s string has any upper case letters, else it returns True
    for c in s:
        if not c.islower():
            return False

    return True

print (any_lowercase5("string"))