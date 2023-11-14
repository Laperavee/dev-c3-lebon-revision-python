def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def substract(a,b):
    return a-b
def divide(a,b):
    return a/b

chain = input("Saisissez une opération")
list = chain.replace("+"," + ").replace("-"," - ").replace("/"," / ").replace("*"," * ")
sum = 0
for i in range(0,len(list)):
    result = 0
    if list[i] == "*":
        result = multiply(int(list[i-1]),int(list[i+1]))
    if list[i] == "/":
        result = divide(int(list[i - 1]),int(list[i + 1]))
    if list[i] == "*":
        result = add(int(list[i - 1]), int(list[i + 1]))
    if list[i] == "*":
        result = substract(int(list[i-1]),int(list[i+1]))
    list[i] =""
    list[i+1] = ""
    list[i-1].replace(list[i-1],result)
    sum+=result
    print(list)
