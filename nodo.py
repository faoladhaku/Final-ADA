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

    def posMedia(self,nodo1):
        #print("posicion",self.posicion)
        posicion=[0]*len(self.posicion)
        for i in range(len(self.posicion)):
            posicion[i]=(self.posicion[i]+nodo1.posicion[i])/2
        return posicion


