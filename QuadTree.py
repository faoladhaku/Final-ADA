from QNodo import QNodo
import pygame as pg
class QuadTree:
    def __init__(self,tam):
        self.tam=tam
        self.pantalla=pg.display.set_mode(self.tam)
        self.reloj=pg.time.Clock()
        self.raiz=QNodo([0,0],self.tam)
        self.actualizar=self.raiz
    def update1(self,objeto):
        cuadrante = self.raiz.Encontrar(objeto)
        try:
            cuadrante.objetos.remove(objeto)
        except:
            print("mal addnode")
            pass
        self.actualizar = cuadrante
    def update2(self,objeto):
        actualizando = self.actualizar
        actualizando.objetos.append(objeto)
