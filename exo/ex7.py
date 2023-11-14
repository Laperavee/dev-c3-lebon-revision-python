with open("addresses.csv","r") as file:
    number = len(file.read().replace("\n",",").split(","))
with open("result.txt","w") as file:
    file.write(str(number))