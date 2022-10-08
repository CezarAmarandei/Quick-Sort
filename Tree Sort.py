class nod:
    def __init__(self, val):
        self.val = val  # valoarea nodului
        self.left = None     # nodul din stanga
        self.right = None   # nodul din dreapta

    def insert(self, val):   # functia de inserare
        if self.val:     # daca nodul are valoare
            if val < self.val:   # daca valoarea este mai mica decat valoarea nodului
                if self.left is None:    # daca nodul din stanga este gol
                    self.left = nod(val)    # inseram valoarea in nodul din stanga
                else:       # daca nodul din stanga nu este gol
                    self.left.insert(val)        # inseram valoarea in nodul din stanga
            elif val > self.val:         # daca valoarea este mai mare sau egala cu valoarea nodului
                if self.right is None: #        daca nodul din dreapta este gol
                    self.right = nod(val)        # inseram valoarea in nodul din dreapta
                else:        # daca nodul din dreapta nu este gol
                    self.right.insert(val)      # inseram valoarea in nodul din dreapta
        else:       # daca nodul nu are valoare
            self.val = val       # inseram valoarea in nod

def inorder(root, res):         # functia de parcurgere in ordine
    if root:        # daca nodul are valoare
        inorder(root.left, res)      # parcurgem nodul din stanga
        res.append(root.val)         # adaugam valoarea nodului in lista
        inorder(root.right, res)        # parcurgem nodul din dreapta

def tree_sort(arr):         # functia de sortare
    if len(arr) == 0:        # daca lungimea listei este 0
        return arr       # returnam lista
    root = nod(arr[0])       # cream un nod cu valoarea primului element din lista
    for i in range(1, len(arr)):       # pentru fiecare element din lista
        root.insert(arr[i])        # inseram elementul in nod
    res = []      # cream o lista noua
    inorder(root, res)    # parcurgem nodul
    return res    # returnam lista

if __name__ == "__main__":  # daca fisierul este rulat direct
    print(tree_sort([10, 1, 3, 2, 9, 14, 13]))  # afisam lista sortata
