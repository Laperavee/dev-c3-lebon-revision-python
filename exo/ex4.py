import random
def sup(a,b):
    if a>b:
        return a
    else:
        return b
def inf(a,b):
    if a<b:
        return a
    else:
        return b

list = []
for i in range(0,10):
    list.append(random.randint(0,10))
