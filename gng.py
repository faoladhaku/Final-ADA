from grafo import *
from topologia  import topologia
import operator


class gng():
    def __init__(self,topologia):
        self.topologia = topologia
        self.grafo = Grafo()
        self.senal = []
        nodo1=self.grafo.addNodo1(1,[random.randint(1,600),random.randint(1,600)],0)
        nodo2=self.grafo.addNodo1(1,[random.randint(1,600),random.randint(1,600)],0)
        print("Crear nodos iniciales: ")
        print('\t',nodo1.posicion,nodo2.posicion)
        self.grafo.addConexion(nodo1,nodo2)
        self.edadMax=10
	



    def start(self):
        #signal=self.topologia[random.randint(0,len(self.topologia)-1)]

        #Generar la señal (un elemento random de la topologia)
        signal= random.choice(self.topologia)
        
        #Encontramos los 2 más cercanos a la señal
        nodo1,nodo2,dist=self.grafo.findCercanos(signal)
        print(signal)

        #Aumentar el error del nodo más cercano
        nodo1.error+=dist

        #Movemos al nodo mas cercano hacia la señal
        e=0.1  #Factor de movimiento (algo asi como la velocidad)
        nodo1.mover(e,signal)

        #Movemos a todos los vecinos hacia la señal
        for vecino in nodo1.vecinos:
            vecino[0].mover(e,signal)
            vecino[1].edad+=1
        
        #Revisamos si los dos nodos del principio tienen conexion
        arista=nodo1.tieneVecino(nodo2)
        if arista: #Si la tienen se reinicia su edad
            arista.edad=0
        else:     #Si no se crea una nueva conexion
            self.grafo.addConexion(nodo1,nodo2)
        

        #Se revisan todas las aristas para ver si hay una muy vieja 
        ar=grafo.aristas[:]
        for arista in ar:
            if arista.edad>self.edadMax:   #Si encontramos una borramos sus conexiones
                grafo.deleteConexionA(arista)
        ar.clear()


        
        print("Cercanos:",nodo1.posicion,nodo2.posicion,dist)
