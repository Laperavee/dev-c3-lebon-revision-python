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
sum = 0
for i in range(0,10):
    list.append(random.randint(a,b))
for item in list:
    localmin = inf(localmin,item)
    localmax = sup(localmax,item)
    sum+=item
print("Local min =" ,localmin)
print("Local max =" ,localmax)
print("Average =", sum / len(list))
