from nodo import Nodo
class topologia():
    def __init__(self):
        self.nodos=[]
    def add2Nodo(self, nodo):
        self.nodos.append(nodo)
        #print nodo.id
    def addNodo(self,id,posicion,error):
        self.nodos.append(Nodo(id,posicion,error))
