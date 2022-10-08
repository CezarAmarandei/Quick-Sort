def bubbleSort(array):          # functia bubbleSort
  for i in range(len(array)):           # parcurgem vectorul de la 0 la lungimea vectorului
    for j in range(0, len(array) - i - 1):   # parcurgem vectorul de la 0 la lungimea vectorului - i - 1
      if array[j] > array[j + 1]:    # daca elementul curent este mai mare decat urmatorul, interschimbam elementele
        temp = array[j]        # salvam elementul curent intr-o variabila temporara
        array[j] = array[j+1]
        array[j+1] = temp

data = [-2, 45, 0, 11, -9]      # vectorul-ul de sortat
bubbleSort(data)        # apelam functia bubbleSort
print('Vectorul sortat in ordine crescatoare: ', data)       # afisam vectorul sortat
