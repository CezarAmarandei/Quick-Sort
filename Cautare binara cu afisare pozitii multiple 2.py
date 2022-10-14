list=[]
numar_elemente=int(input("Introduceti numarul de elemente: "))
for i in range(0,numar_elemente):
    element=int(input("Introduceti elementul: "))
    list.append(element)
print(list)

list.sort()
print("Lista sortata: ", list)

cautare_numar=int(input("Introduceti numarul pe care doriti sa il cautati: "))

low=0
high=numar_elemente-1
def cautare_binara(list, cautare_numar, low, high):
    while low <= high:
        mid=(low+high)//2
        if list[mid]==cautare_numar:
            for i in range(low, high+1):
                if list[i]==cautare_numar:
                    print("Numarul a fost gasit pe pozitia ", i+1)
            return mid
        elif list[mid]<cautare_numar:
            low=mid+1
        else:
            high=mid-1
    return -1

cautare_binara(list, cautare_numar, low, high)
repetare = input("Doriti sa cautati alt numar? (y/n): ")
while (repetare=="y"):
    cautare_numar = int(input("Introduceti numarul pe care doriti sa il cautati: "))
    if cautare_binara(list, cautare_numar, low, high) == -1:
        print("Numarul nu a fost gasit")
    repetare = input("Doriti sa cautati alt numar? (y/n): ")
