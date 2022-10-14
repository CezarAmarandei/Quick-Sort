list=[]
numar_elemente=int(input("Introduceti numarul de elemente: "))
for i in range(0,numar_elemente):
    element=int(input("Introduceti elementul: "))
    list.append(element)
print(list)

cautare_numar=int(input("Introduceti numarul pe care doriti sa il cautati: "))
list.sort()

print("Lista sortata: ", list)


def cautare_binara(list, cautare_numar, numar_elemente):
    low=0
    high=numar_elemente-1
    while low <= high:
        mid=(low+high)//2
        if list[mid]==cautare_numar:
            return mid
        elif list[mid]<cautare_numar:
            low=mid+1
        else:
            high=mid-1
    return -1

#cautare_binara(list, cautare_numar, numar_elemente)

if cautare_binara(list, cautare_numar, numar_elemente) == -1:
    print("Numarul nu a fost gasit")
else:
    print("Numarul a fost gasit pe pozitia ", cautare_binara(list, cautare_numar, numar_elemente)+1)

repetare = input("Doriti sa cautati alt numar? (y/n): ")
while (repetare=="y"):
    cautare_numar = int(input("Introduceti numarul pe care doriti sa il cautati: "))
    if cautare_binara(list, cautare_numar, numar_elemente) == -1:
        print("Numarul nu a fost gasit")
    else:
        print("Numarul a fost gasit pe pozitia ", cautare_binara(list, cautare_numar, numar_elemente)+1)
    repetare = input("Doriti sa cautati alt numar? (y/n): ")
