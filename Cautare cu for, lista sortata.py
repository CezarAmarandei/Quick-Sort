list=[]
numar_elemente=int(input("Introduceti numarul de elemente: "))
for i in range(0,numar_elemente):
    element=int(input("Introduceti elementul: "))
    list.append(element)
print(list)

cautare_numar=int(input("Introduceti numarul pe care doriti sa il cautati: "))
list.sort()

print("Lista sortata: ", list)
ok=0

def find_array(list, numar_elemente):
    global ok
    ok=0
    for i in range(0,numar_elemente):
        if (cautare_numar==list[i]):
            print("Numarul cautat se afla in lista sortata pe pozitia ", i+1)
            ok=1
    if (ok==0):
        print("Numarul cautat nu se afla in lista sortata")


find_array(list, numar_elemente)

repetare = input("Doriti sa cautati alt numar? (y/n): ")

while (repetare=="y"):
    cautare_numar = int(input("Introduceti numarul pe care doriti sa il cautati: "))
    find_array(list, numar_elemente)
    repetare = input("Doriti sa cautati alt numar? (y/n): ")
