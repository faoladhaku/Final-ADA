# -*- encoding: utf-8 -*-
from grafo import *
import operator


class gng():
    def __init__(self,topologia,tam):
        self.topologia = topologia
        self.grafo = Grafo(tam)
        self.senal = []
        nodo1=self.grafo.addNodo1(1,[random.randint(1,600),random.randint(1,600)],0)
        nodo2=self.grafo.addNodo1(1,[random.randint(1,600),random.randint(1,600)],0)
        print("Crear nodos iniciales: ")
        print('\t',nodo1.posicion,nodo2.posicion)
        self.grafo.addConexion(nodo1,nodo2)
        self.edadMax=100
        self.iteracion=0
        self.alpha=0.05  #Factor de aumento de error en nuevos nodos
        self.betha=0.0005  #Factor de decrecimiento de errores
        self.maxNodos=1000
        self.ew=0.1    #Movimiento de nodo principal
        self.en=0.07   #Movimiento de vecinos
        self.lamb=100  #Iteracion # para insertar nuevo nodo
        self.tam=tam
        self.ageStep=5
        
	



    def start(self):
        tam=self.grafo.tree.tam
        pantalla=pg.display.set_mode(tam)
        #reloj=pg.time.Clock()
        pg.font.init()
        cerrar=False

        while not cerrar:
            for evento in pg.event.get():
                if evento.type==pg.QUIT:
                    cerrar= True


            #Generar la senal (un elemento random de la topologia)
            signal= random.choice(self.topologia)
            
            #Encontramos los 2 mas cercanos a la senal
            nodo1,nodo2,dist=self.grafo.findCercanos(signal)
            #print(signal)

            #Aumentar el error del nodo mas cercano
            nodo1.error+=dist

            #Movemos al nodo mas cercano hacia la senal
            #e=0.3  #Factor de movimiento (algo asi como la velocidad)
            self.grafo.tree.update1(nodo1)
            nodo1.mover(self.ew,signal)
            nodo1.visitado=1
            self.grafo.tree.update2(nodo1)

            #Movemos a todos los vecinos hacia la senal
            for vecino in nodo1.vecinos:
                self.grafo.tree.update1(vecino[0])
                vecino[0].mover(self.en,signal)
                vecino[1].edad+=self.ageStep
                self.grafo.tree.update2(vecino[0])
            
            #Revisamos si los dos nodos del principio tienen conexion
            arista=nodo1.tieneVecino(nodo2)
            if arista: #Si la tienen se reinicia su edad
                arista.edad=0
            else:     #Si no se crea una nueva conexion
                self.grafo.addConexion(nodo1,nodo2)
            

            #Se revisan todas las aristas para ver si hay una muy vieja 
            ar=self.grafo.aristas[:]
            for arista in ar:
                if arista.edad>=self.edadMax:   #Si encontramos una borramos sus conexiones
                    self.grafo.deleteConexionA(arista)
            ar=[]

            #Agregar nodo si no se excedio el limite
            if self.iteracion%self.lamb==0 and self.grafo.id<=self.maxNodos:
                #Encontrar el nodo con error maximo
                nodoU=self.grafo.getNodeErrorMax()
                #Encontrar el nodo vecino de nodoU con el error maximo
                nodoV , conexion=self.grafo.getNodeErrorMaxByNodo(nodoU)

                #Encontrar la posicion media
                posMedia=nodoU.posMedia(nodoV)
                #Crear un nodo entre los dos
                nodoR=self.grafo.addNodo1(1,posMedia,0)
                #self.grafo.tree.raiz.Insertar(nodoR)
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

                #Dibujar
                pantalla.fill(pg.color.Color('black'))                
                for punto in self.topologia:
                    pg.draw.circle(pantalla,pg.color.Color('white'),punto,3)

                for arista in self.grafo.aristas:
                    pg.draw.line(pantalla,pg.color.Color('red'),arista.nodos[0].posicion,arista.nodos[1].posicion,4)

                for nodo in self.grafo.nodos:
                    pg.draw.circle(pantalla,pg.color.Color('blue'), map(int,nodo.posicion),3)
                
                self.grafo.tree.raiz.Update(pantalla)
                text_to_screen(pantalla,"nodos: "+str(self.grafo.id),[5,5])

                pg.display.flip()
                #print("nodos: "+str(self.grafo.id))
            
            #Si excedio el limite GG
            if len(self.grafo.nodos)==self.maxNodos:

                print("Termino\n")
                print("Numero de nodos",len(self.grafo.nodos))
                input("Presione una tecla para cerrar")
                # for nodo in self.grafo.nodos:
                #     print(nodo.id,  [i[0].id for i in nodo.vecinos])
                cerrar=True
                #return

                #text_to_screen(pantalla,nodo.id,nodo.posicion)

            self.iteracion+=1



#            reloj.tick(100)
            


        print("Termino\n")
        print("Numero de nodos",len(self.grafo.nodos))

        cerrar=False
        pantalla=pg.display.set_mode(tam)
        while not cerrar:
            for evento in pg.event.get():
                if evento.type==pg.QUIT:
                    cerrar= True

            pantalla.fill(pg.color.Color('black'))
            for arista in self.grafo.aristas:
                pg.draw.line(pantalla,pg.color.Color('red'),arista.nodos[0].posicion,arista.nodos[1].posicion,3)
            # for nodo in self.grafo.nodos:
            #     pg.draw.circle(pantalla,pg.color.Color('blue'), list(map(int,nodo.posicion)),3)
            pg.display.flip()
            #reloj.tick(20)


        #print("Cercanos:",nodo1.posicion,nodo2.posicion,dist)
