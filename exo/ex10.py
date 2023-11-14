def InsertionSorting(tab):
    x = len(tab)
    for i in range(1,x):
        index = tab(i)
        j = i-1
        while j>=0 and tab(j) > index:
            tab[j+1] = tab(j)
            j = j-1
        tab[j+1] = index

