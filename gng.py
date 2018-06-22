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
        self.edadMax=5
        self.iteracion=0
        self.alpha=0.5
        self.betha=0.6
	



    def start(self):

        while True:

            #signal=self.topologia[random.randint(0,len(self.topologia)-1)]

            #Generar la señal (un elemento random de la topologia)
            signal= random.choice(self.topologia)
            
            #Encontramos los 2 más cercanos a la señal
            nodo1,nodo2,dist=self.grafo.findCercanos(signal)
            print(signal)

            #Aumentar el error del nodo más cercano
            nodo1.error+=dist

            #Movemos al nodo mas cercano hacia la señal
            e=0.3  #Factor de movimiento (algo asi como la velocidad)
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
            ar=self.grafo.aristas[:]
            for arista in ar:
                if arista.edad>self.edadMax:   #Si encontramos una borramos sus conexiones
                    self.grafo.deleteConexionA(arista)
            ar=[]

            #Agregar nodo si no se excedio el limite
            if self.iteracion%10==0 and len(self.grafo.nodos)<=800:
                #Encontrar el nodo con error maximo
                nodoU=self.grafo.getNodeErrorMax()
                #Encontrar el nodo vecino de nodoU con el error maximo
                nodoV , conexion=self.grafo.getNodeErrorMaxByNodo(nodoU)

                #Encontrar la posicion media
                posMedia=nodoU.posMedia(nodoV)
                #Crear un nodo entre los dos
                nodoR=self.grafo.addNodo1(1,posMedia,0)

                #Conectar nodoR a nodoU y nodoV y borrar la conexion entre nodoU y nodoV
                self.grafo.addConexion(nodoU,nodoR)
                self.grafo.addConexion(nodoR,nodoV)
                self.grafo.deleteConexionA(conexion)

                #Modificar los errores de U, V y R
                nodoU.error*=self.alpha
                nodoV.error*=self.alpha
                nodoR.error=nodoU.error

                #Reducir los errores de todos los nodos del grafo
                for nodo in self.grafo.nodos:
                    nodo.error-=self.betha*nodo.error
            
            #Si excedio el limite GG
            if len(self.grafo.nodos)==500:
                print("Termino")
                # for nodo in self.grafo.nodos:
                #     print(nodo.id,  [i[0].id for i in nodo.vecinos])
                return
            


            



        
        print("Cercanos:",nodo1.posicion,nodo2.posicion,dist)
