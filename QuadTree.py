import pygame as pg

tam=(700,500)
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)

pantalla=pg.display.set_mode(tam)

reloj=pg.time.Clock()

cerrar=False
while not cerrar:
    for evento in pg.event.get():
        if evento.type==pg.QUIT:
            cerrar= True
    

    pg.draw.line(pantalla,ROJO,[0,0],tam,1)
    pg.display.flip()
    reloj.tick(20)
    
pg.quit()