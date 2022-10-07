def mergeSort(array): # functia de sortare
    if len(array) > 1: # daca lungimea array-ului este mai mare decat 1, adica inca nu am impartit lista in cate un element
        r = len(array)//2 #  r este mijlocul listei
        L = array[:r] # L este lista din stanga
        M = array[r:] #M este lista din dreapta
        mergeSort(L) #sortam lista din stanga
        mergeSort(M) #sortam lista din dreapta
        i = j = k = 0 # i,j,k sunt indexii ce pornesc de la zero
        while i < len(L) and j < len(M): # cat timp i si j sunt mai mici decat lungimile listelor
            if L[i] < M[j]: # daca elementul din lista din stanga este mai mic decat cel din dreapta
                array[k] = L[i] # daca da, atunci elementul din lista din stanga va fi pus in array
                i += 1 # se incrementeaza i
            else:
                array[k] = M[j] # daca nu, atunci elementul din lista din dreapta va fi pus in array
                j += 1 # se incrementeaza j
            k += 1 # 
        while i < len(L): #daca ramanem fara elemente in lista din stanga
            array[k] = L[i] # atunci elementele din lista din stanga vor fi puse in array
            i += 1
            k += 1

        while j < len(M): #daca ramanem fara elemente in lista din dreapta
            array[k] = M[j] # atunci elementele din lista din dreapta vor fi puse in array
            j += 1
            k += 1

def printList(array): # functia de printare
    for i in range(len(array)): # pentru fiecare element din array
        print(array[i], end=" ") # printam elementul urmat de un spatiu
    print() # printam un rand nou

if __name__ == '__main__': # daca fisierul este rulat direct
    array = [6, 5, 12, 10, 9, 1]
    mergeSort(array) # sortam array-ul
    print("Sorted array is: ") 
    printList(array) # printam array-ul sortat
