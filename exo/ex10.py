def InsertionSorting(tab):
    for i in range(1,len(tab)):
        index = tab[i]
        j = i-1
        while j>=0 and tab[j] > index:
            tab[j+1] = tab[j]
            j = j-1
        tab[j+1] = index

a = [1,6,8,4,8,5,4,7,6,9]
InsertionSorting(a)
print(a)