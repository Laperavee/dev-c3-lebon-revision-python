chain = input("Saisissez une opération")
list = chain.replace("+"," + ").replace("-"," - ").replace("/"," / ").replace("*"," * ")

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b