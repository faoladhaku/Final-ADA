import operator

class Nodo():
    def __init__(self, id,posicion,error):
        self.id = id
        self.posicion= list(posicion)
        self.error = error
        self.vecinos=[]
        self.visitado=0
    

    def mover(self,e,signal):
        vector=list(map(operator.sub,signal,self.posicion))
        for i in range(len(vector)):
            self.posicion[i]+=e*vector[i]
    
    def tieneVecino(self,nodo):
        for vecino in self.vecinos:
            if vecino[0]==nodo:
                return vecino[1]
        return False

    def findCercanos(self, topologia ):
        print ("fc" ,self.posicion)
        nodo_cercano = topologia.nodos[0]
        cercano=(((self.posicion[0]-topologia.nodos[0].posicion[0])**(2))+((self.posicion[1]-topologia.nodos[0].posicion[1])**(2)))**(1/2.0)
        cercanos=[]
        for i in topologia.nodos:
            norma2=(((self.posicion[0]-i.posicion[0])**(2))+((self.posicion[1]-i.posicion[1])**(2)))**(1/2.0)
            #print norma2
            if cercano>norma2:
                cercano=norma2
                nodo_cercano=i
                #print "asd",cercano
        #print "primero",nodo_cercano.posicion
        cercanos.append(nodo_cercano)
        aux=[i for i in topologia.nodos if i!=nodo_cercano]
        nodo_cercano=aux[0]
        cercano=(((self.posicion[0]-aux[0].posicion[0])**(2))+((self.posicion[1]-aux[0].posicion[1])**(2)))**(1/2.0)
        #print cercano
        for i in aux:
            norma2=(((self.posicion[0]-i.posicion[0])**(2))+((self.posicion[1]-i.posicion[1])**(2)))**(1/2.0)
            #print norma2
            if cercano>norma2:
                cercano=norma2
                nodo_cercano=i
                #print "asd1",cercano
        #print "segundo",nodo_cercano.posicion
        cercanos.append(nodo_cercano)
        return cercanos

    def posMedia(self,nodo1):
        #print("posicion",self.posicion)
        posicion=[0]*len(self.posicion)
        for i in range(len(self.posicion)):
            posicion[i]=(self.posicion[i]+nodo1.posicion[i])/2
        return posicion


    def getSenal(self, topologia):
        #print "senal"
        return self.findCercanos(topologia)
