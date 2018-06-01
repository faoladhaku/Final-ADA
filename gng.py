from grafo import *
from topologia  import topologia
class gng():
    def __init__(self,topologia,Grafo):
        self.topologia = topologia
        self.grafo = Grafo
        self.senal = []
        self.nodo1 = Nodo(1,[1,2],2)
        self.nodo2 = Nodo(2,[3,4],4)
        self.arista = Arista(self.nodo1,self.nodo2,2,2)
        self.grafo.addNodo(self.nodo1)
        self.grafo.addNodo(self.nodo2)
        self.grafo.addArista(self.arista)
        for nodo in self.grafo.nodos:
            nodo.getSenal(self.topologia)
    def begin(self):
        pass
