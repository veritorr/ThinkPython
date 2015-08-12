__author__ = "Thomas D'Alleva"



def middle(List):
    return List[1:-1]

def chop(List):
    del List[0]
    del List[-1]
    print List
    return None

oList = [1, 2, 3, 4, 5, 6]
print middle(oList)
chop(oList)