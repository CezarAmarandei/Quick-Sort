def bubbleSort(array):          # functia bubbleSort
  for i in range(len(array)):           # parcurgem array-ul
    for j in range(0, len(array) - i - 1):   # parcurgem array-ul   
      if array[j] > array[j + 1]:    # daca elementul curent este mai mare decat urmatorul  
        temp = array[j]     # interschimbam elementelea
        array[j] = array[j+1]       # interschimbam elementelea
        array[j+1] = temp       # interschimbam elementeleaa
data = [-2, 45, 0, 11, -9]      # vectorul-ul

bubbleSort(data)        # apelam functia bubbleSort
print('Vectorul sortat in ordine crescatoare: ', data)       # afisam vectorul sortat
