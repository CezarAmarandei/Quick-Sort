def partition(array, Primul, Ultimul):
  pivot = array[Ultimul] # Alegem pivotul ca ultim element
  i = Primul - 1 # pointerul
  for j in range(Primul, Ultimul): #parcurgem toata lista comparand-o cu pivotul
    if array[j] <= pivot: # daca elementul este mai mic sau egal cu pivotul, il mutam in stanga
      i = i + 1
      (array[i], array[j]) = (array[j], array[i]) # interschimbam elementele
  (array[i + 1], array[Ultimul]) = (array[Ultimul], array[i + 1]) # interschimbam pivotul cu elementul din dreapta
  return i + 1 # returnam pozitia pivotului

def quickSort(array, Primul, Ultimul): # Functia ce efectueaza QuickSort
  if Primul < Ultimul:
    pi = partition(array, Primul, Ultimul)
    quickSort(array, Primul, pi - 1) # apelam functia pentru partea stanga
    quickSort(array, pi + 1, Ultimul) # apelam functia pentru partea dreapta

Lista = [8, 7, 2, 1, 0, 9, 6, 5, 4, 3, 12, 99, 1, 5]
print("Lista nesortata: ", Lista)
quickSort(Lista, 0, len(Lista) - 1)
print('Lista sortata in ordine crescatoare: ', Lista)
