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
a = 0
b = 10
localmin = b
localmax = a
for i in range(0,10):
    list.append(random.randint(a,b))
