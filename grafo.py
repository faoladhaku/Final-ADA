import pygame as pg

from arista import Arista
from nodo import Nodo
import random


def distancia(pos1,pos2):
    return ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**(1/2.0)


class Grafo():
    def __init__(self):
        self.nodos = []
        self.aristas = []
        self.id=0
    def addNodo(self, nodo):
        self.nodos.append(nodo)
        self.id+=1
        #print "AN",nodo.posicion
    def addNodo1(self,id,posicion,error):
        nuevo=Nodo(self.id,posicion,error)
        self.nodos.append(nuevo)
        print("Añadido nodo",self.id,"en",posicion)
        self.id+=1
        return nuevo

    def addArista(self, arista):
        self.aristas.append(arista)
#        print "AA",arista.edad
    def addConexion(self,nodo1,nodo2,distancia=0,edad=0):
        if nodo1 in [i[0] for i in nodo2.vecinos] or nodo1==nodo2:
            print ("Denegado: ",nodo1.id,nodo2.id)
            return 
        arista=Arista(nodo1,nodo2,edad,distancia)
        nodo1.vecinos.append((nodo2,arista))
        nodo2.vecinos.append((nodo1,arista))
        self.aristas.append(arista)
        #print("vecinos de",nodo1.id,[i[0].id for i in nodo1.vecinos])
    def addConexiones(self,nodos):
        try:
            for n1,n2 in zip(nodos,nodos[1:]):
                print(n1,n2)
                self.addConexion(self.nodos[n1],self.nodos[n2])


        except StopIteration:
            pass

    def findNodo(self, nodo):
        for x in self.nodos:
            if(x.id == nodo.id):
                print ("FN",nodo.id)

    
    def findConexion(self,nodo1,nodo2):
        for arista in self.aristas:
            if nodo1 in arista.nodos and nodo2 in arista.nodos:
                return True
        return False
    
    def deleteConexionA(self,arista):
        self.aristas.remove(arista)
        nodo1=arista.nodos[0]
        nodo2=arista.nodos[1]
        nodo1.vecinos.remove((nodo2,arista))
        nodo2.vecinos.remove((nodo1,arista))
        print("Arista eliminada entre",nodo1.id,nodo2.id,hex(id(arista)))
    
    def deleteConexionN(self,nodo1,nodo2):
        n1=self.nodos[nodo1]
        n2=self.nodos[nodo2]
        arista=n1.tieneVecino(n2)
        if arista:
            self.deleteConexionA(arista)
        else:
            print("No tienen Conexion")

    def deleteNodo(self, nodos):
        pass

    def findCercanos(self,signal):
        n1=0
        n2=0
        dMin=float('inf')
        for nodo in self.nodos:
            d=distancia(nodo.posicion,signal)
            if dMin>=d:
                n1=nodo
                dMin=d
        dmin=dMin
        dMin=float('inf')
        for nodo in [i for i in self.nodos if i!=n1]:
            d=distancia(nodo.posicion,signal)
            if dMin>=d:
                n2=nodo
                dMin=d
        print(n1,n2)
        return n1,n2,dmin

    def getNodeErrorMax(self):
        n=self.nodos[0]
        for nodo in self.nodos:
            if n.error < nodo.error:
                n=nodo
        return n

    def getNodeErrorMaxByNodo(self,nodo):
        n=nodo.vecinos[0]
        for vecino in nodo.vecinos:
            if n[0].error < vecino[0].error:
                n=vecino
        return n


    def createHalfNodo(self,nodoU,nodoV):
        nodoU=self.nodos[nodoU]
        nodoV=self.nodos[nodoV]

        conexion=nodoU.tieneVecino(nodoV)

        #Nodo vecino de U con el error maximo
        posMedia=nodoU.posMedia(nodoV)
        nodoR=self.addNodo1(1,posMedia,0)

        self.addConexion(nodoU,nodoR)
        self.addConexion(nodoR,nodoV)
        self.deleteConexionA(conexion)






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
                #print "este es cercano", nodo.posicion
        return cercanos,distanciaMin




def text_to_screen(screen, text, pos, size = 25):
    try:

        text = str(text)
        font = pg.font.Font(None, size)
        text = font.render(text, True, pg.color.Color('white'))
        screen.blit(text, pos)

    except Exception as e:
        print ('Font Error, saw it coming')
        raise e


# grafo=Grafo()
# tam=[600,600]
# pg.font.init()
# for i in range(7):
#     grafo.addNodo1(1,[random.randint(1,600),random.randint(1,600)],0)

# for nodo1 in grafo.nodos:
#     h=random.randint(0,grafo.id-1)
#     n=[grafo.nodos[random.randint(0,grafo.id-1)] for i in range(h)]
#     for nodo2 in n:
#         grafo.addConexion(nodo1,nodo2)

# for nodo in grafo.nodos:
#     print ("Vecinos de ",nodo.id)
#     print ("\t-",[(i[0].id,i[1]) for i in nodo.vecinos])

# for arista in grafo.aristas:
#     print ("Arista:",[nodo.id for nodo in arista.nodos],arista)

# pantalla=pg.display.set_mode(tam)
# reloj=pg.time.Clock()
# cerrar=False
# while not cerrar:
#     for evento in pg.event.get():
#         if evento.type==pg.QUIT:
#             cerrar= True
#         if evento.type==pg.MOUSEBUTTONUP:
#             pos=pg.mouse.get_pos()
#             grafo.addNodo1(1,pos,0)
#             #objetos.append(pos)
#         if evento.type==pg.KEYUP:
#             if evento.key==pg.K_s:
#                 b=list(map(int,input("Ingrese Nodos: ").split()))
#                 grafo.addConexiones(b)
#                 for nodo in grafo.nodos:
#                     print ("Vecinos de ",nodo.id,[i[0].id for i in nodo.vecinos])
#             elif evento.key==pg.K_r:
#                 b=list(map(int,input("Ingrese Nodos: ").split()))
#                 grafo.deleteConexionN(b[0],b[1])

#             elif evento.key==pg.K_t:
#                 ar=grafo.aristas[:]
#                 for arista in ar:
#                     grafo.deleteConexionA(arista)
#                 ar.clear()
        
            
#     pantalla.fill(pg.color.Color('black'))
#     #pg.draw.rect(pantalla,pg.color.Color('blue'),[300,300,600,600],1)
#     for arista in grafo.aristas:
#         pg.draw.line(pantalla,pg.color.Color('red'),arista.nodos[0].posicion,arista.nodos[1].posicion,1)

#     for nodo in grafo.nodos:
#         pg.draw.circle(pantalla,pg.color.Color('blue'),nodo.posicion,6)
#         text_to_screen(pantalla,nodo.id,nodo.posicion)


#     pg.display.flip()
#     reloj.tick(20)

# print("Grafo terminado")
# for nodo in grafo.nodos:
#     print ("Vecinos de ",nodo.id,[i[0].id for i in nodo.vecinos])

# for arista in grafo.aristas:
#     print("Arista",arista.nodos)

# print([i.posicion for i in grafo.nodos]) 
