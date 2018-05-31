from nodo import Nodo
from arista import Arista

class Grafo():
    def __init__(self):
        self.nodos = []
        self.aristas = []
    def addNodo(self, nodo):
        self.nodos.append(nodo)
        print "AN",nodo.id
    def addArista(self, arista):
        self.aristas.append(arista)
        print "AA",arista.edad
    def findNodo(self, nodo):
        for x in self.nodos:
            if(x.id == nodo.id):
                print "FN",nodo.id
    def deleteNodo(self, nodos):
        pass
    