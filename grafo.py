from nodo import nodo
from aristas import aristas

class grafo():
    def __init__(self):
        self.nodos = []
        self.aristas = []
    def addnodo(self, nodo):
        self.nodos.append(nodo)
        print(nodo.id)
    def addarista(self, arista):
        self.aristas.append(arista)
        print(arista.edad)
    def findnodo(self, nodo):
        for x in self.nodos:
            if(x.id == nodo.id):
                print(nodo.id)
    def deletenodo(self, nodos):
        pass
    