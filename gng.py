from grafo import *
from topologia  import topologia
import random


class gng():
    def __init__(self,topologia,Grafo):
        self.topologia = topologia
        self.grafo = Grafo
        self.senal = []
        self.nodo1 = Nodo(1,[random.randint(1,599),random.randint(1,599)],0)
        self.nodo2 = Nodo(2,[random.randint(1,599),random.randint(1,599)],0)
        #self.arista = Arista(self.nodo1,self.nodo2,0,2)
        self.grafo.addNodo(self.nodo1)
        self.grafo.addNodo(self.nodo2)

    def begin(self):
        print "antes",self.nodo1.posicion, self.nodo2.posicion
        cercanos,distncia=self.grafo.getSenal(self.topologia)
        print "despues",cercanos[0].posicion,cercanos[1].posicion
        if not self.grafo.findConexion(cercanos[0],cercanos[1]):
            self.grafo.addConexion(cercanos[0],cercanos[1])
        else:
            cercanos[0].error+=distancia
