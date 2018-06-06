from grafo import *
from topologia  import topologia
class gng():
    def __init__(self,topologia,Grafo):
        self.topologia = topologia
        self.grafo = Grafo
        self.senal = []
        self.nodo1 = Nodo(1,(369, 428),0)
        self.nodo2 = Nodo(2,[3,4],0)
        self.arista = Arista(self.nodo1,self.nodo2,0,2)
        self.grafo.addNodo(self.nodo1)
        self.grafo.addNodo(self.nodo2)
        self.grafo.addArista(self.arista)

    def begin(self):
        self.grafo.nodos[0].getSenal(self.topologia)
