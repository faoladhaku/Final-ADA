class Nodo():
    def __init__(self, id,posicion,error):
        self.id = id
        self.posicion= posicion
        self.error = error

    def findCercanos(self, topologia ):
        print "fc" ,self.posicion
        nodo_cercano = topologia.nodos[0]
        cercano=(((self.posicion[0]-topologia.nodos[0].posicion[0])**(2))+((self.posicion[1]-topologia.nodos[0].posicion[1])**(2)))**(1/2.0)
        cercanos=[]
        for i in topologia.nodos:
            norma2=(((self.posicion[0]-i.posicion[0])**(2))+((self.posicion[1]-i.posicion[1])**(2)))**(1/2.0)
            print norma2
            if cercano>norma2:
                cercano=norma2
                nodo_cercano=i
                #print "asd",cercano
        print "primero",nodo_cercano.posicion
        cercanos.append(nodo_cercano)
        aux=[i for i in topologia.nodos if i!=nodo_cercano]
        nodo_cercano=aux[0]
        cercano=(((self.posicion[0]-aux[0].posicion[0])**(2))+((self.posicion[1]-aux[0].posicion[1])**(2)))**(1/2.0)
        print cercano
        for i in aux:
            norma2=(((self.posicion[0]-i.posicion[0])**(2))+((self.posicion[1]-i.posicion[1])**(2)))**(1/2.0)
            print norma2
            if cercano>norma2:
                cercano=norma2
                nodo_cercano=i
                #print "asd1",cercano
        print "segundo",nodo_cercano.posicion
        cercanos.append(nodo_cercano)
        return cercanos


    def getSenal(self, topologia):
        print "senal"
        return self.findCercanos(topologia)
