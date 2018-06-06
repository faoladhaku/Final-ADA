from nodo import Nodo
from arista import Arista


def distancia(pos1,pos2):
    return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2.0)


class Grafo():
    def __init__(self):
        self.nodos = []
        self.aristas = []
    def addNodo(self, nodo):
        self.nodos.append(nodo)
        #print "AN",nodo.posicion
    def addNodo1(self,id,posicion,error):
        self.nodos.append(Nodo(id,posicion,error))
    def addArista(self, arista):
        self.aristas.append(arista)
#        print "AA",arista.edad
    def addConexion(self,nodo1,nodo2,distancia=0,edad=0):
        self.aristas.append(Arista(nodo1,nodo2,edad,distancia))
    def findNodo(self, nodo):
        for x in self.nodos:
            if(x.id == nodo.id):
                print "FN",nodo.id
    def findConexion(self,nodo1,nodo2):
        for arista in self.aristas:
            if nodo1 in arista.nodos and nodo2 in arista.nodos:
                return True
        return False
    def deleteNodo(self, nodos):
        pass


    def getSenal(self,topologia):
        minDis=float('inf')
        cercanos=[]
        nodoCercano=0

        for nodo in self.nodos:
            distanciaTotal=0
            for punto in topologia.nodos:
                distancia1=distancia(nodo.posicion,punto.posicion)
                distanciaTotal+=distancia1
            if distanciaTotal<minDis:
                minDis=distanciaTotal
                nodoCercano=nodo
        cercanos.append(nodoCercano)

        aux=[i for i in self.nodos if i!=nodoCercano]
        minDis=float('inf')
        nodoCercano=0
        for nodo in aux:
            distanciaTotal=0
            for punto in topologia.nodos:
                distanciaTotal+=distancia(nodo.posicion,punto.posicion)
            if distanciaTotal<minDis:
                minDis=distanciaTotal
                nodoCercano=nodo
        cercanos.append(nodoCercano)

        distanciaMin=float('inf')
        for nodo in self.nodos:
            distancia1=distancia(nodo.posicion,cercanos[0].posicion)
            if distancia1<distanciaMin:
                distanciaMin=distancia1
                print "este es cercano", nodo.posicion
        return cercanos,distanciaMin
