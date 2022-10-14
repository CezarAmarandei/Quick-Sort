def forsearch(array, size, search, rezultat):
    gasit = 0
    for i in range(size):
        if array[i] == search:
            rezultat.append(i)
            gasit=1
    if gasit == 0:
        print("Valoarea ", serch, " nu a fost gasita.")
    return -1

data = [1 , 2 , 2, 3, 4, 5, 2]
size = len(data)
value = 2
rezultat=[]
forsearch(data, size, value, rezultat) 
delim = ","
temp = list(map(str, rezultat))
res = delim.join(temp)
print(str(res))