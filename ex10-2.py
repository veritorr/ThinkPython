__author__ = "Thomas D'Alleva"

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(nestedT):
    result = []

    for s in nestedT:
        result.append(capitalize_all(s))

    return result

newString = []

nestString = [['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h'],['i', 'j', 'k', 'l']]

newString = capitalize_nested(nestString)
print nestString[:]
print newString[:]
