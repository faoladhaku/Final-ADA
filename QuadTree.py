from QNodo import QNodo
import pygame as pg
class QuadTree:
    def __init__(self):
        self.tam=[600,600]

        self.pantalla=pg.display.set_mode(self.tam)
        self.reloj=pg.time.Clock()
        self.raiz=QNodo([0,0],self.tam)
    def update(self):
        cerrar=False
        objetos=[]
        while not cerrar:
            for evento in pg.event.get():
                if evento.type==pg.QUIT:
                    cerrar= True
                if evento.type==pg.MOUSEBUTTONDOWN:
                    pos=pg.mouse.get_pos()
                    #print(pos)
                    #objetos.append(pos)
                    self.raiz.Insertar(pos)
            self.pantalla.fill(pg.color.Color('black'))
            #pg.draw.rect(self.pantalla,pg.color.Color('blue'),[300,300,600,600],1)
            self.raiz.Update(self.pantalla)
            pg.display.flip()
            self.reloj.tick(20)
            

qt=QuadTree()
qt.update()
pg.quit()            