def factorielle(x):
    if x != 0:
        return x * factorielle(x-1)
    else:
        return 1

number = int(input("Saisissez un nombre : "))
print("Voici la factorielle de ce nombre =",factorielle(number))