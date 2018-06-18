import pygame as pg

class QNodo:
    def __init__(self, p1, p2):
        self.p1=p1
        self.p2=p2
        self.objetos=[]
        self.hijos=[None]*4
        self.ancho=abs(p2[0]-p1[0])
        self.altura=abs(p2[1]-p1[1])
        self.rectangulo=p1+[self.ancho,self.altura]
        print(p1,p2,"   ",self.rectangulo)


    def tieneHijos(self):
        if self.hijos[0]:
            return True
        return False

    def Update(self,pantalla):
        if not self.tieneHijos():
            pg.draw.rect(pantalla,pg.color.Color('red'),self.rectangulo,1)
            for objeto in self.objetos:
                pg.draw.circle(pantalla,pg.color.Color('blue'),objeto,5,0)
        else:
            for i in self.hijos:
                i.Update(pantalla)

    def Encontrar(self,objeto):
        if not self.tieneHijos():
            if objeto[0] > self.p1[0] and objeto[0] < self.p2[0] and objeto[1] > self.p1[1] and objeto[1] < self.p2[1]:
                return self
            return 0
        else:
            for i in self.hijos:
                res=i.Encontrar(objeto)
                if res:
                    return res

    def Dividir(self):
        if self.tieneHijos():
            return
        centro    = [self.p1[0]+self.ancho/2 , self.p1[1]+self.altura/2]
        derecha   = [self.p2[0]              , self.p1[1]+self.altura/2]
        izquierda = [self.p1[0]              , self.p1[1]+self.altura/2]
        abajo     = [self.p1[0]+self.ancho/2 , self.p2[1]]
        arriba    = [self.p1[0]+self.ancho/2 , self.p1[1]]
        self.hijos[0]=QNodo(self.p1,centro)
        self.hijos[1]=QNodo(arriba,derecha)
        self.hijos[2]=QNodo(izquierda,abajo)
        self.hijos[3]=QNodo(centro,self.p2)
        print()
        for i in self.objetos:
            self.Insertar(i)
    
    def Insertar(self,objeto):
        cuadrante = self.Encontrar(objeto)
        if cuadrante:
            cuadrante.objetos.append(objeto)
            if len(cuadrante.objetos)==4:
                cuadrante.Dividir()
                
        else:
            print ("que fue?")
