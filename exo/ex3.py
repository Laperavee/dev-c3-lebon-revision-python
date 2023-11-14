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


