from gng import gng
import pygame as pg
from figura import topologia


#Ready to go: Linux and Windows
#Msg to fork
def text_to_screen(screen, text, pos, size = 25):
    try:

        text = str(text)
        font = pg.font.Font(None, size)
        text = font.render(text, True, pg.color.Color('white'))
        screen.blit(text, pos)

    except Exception as e:
        print ('Font Error, saw it coming')
        raise e

#topologia=[[482, 232], [257, 404], [119, 321], [268, 229], [123, 155], [186, 40], [110, 273]]



 
print("1.- Usar topologia por default")
print("2.- Propia topologia")
op=input("opcion: ")
tam=[1280,720]
if op=='1' or op==1:
    cerrar=True
else:
    topologia=[]    
    pantalla=pg.display.set_mode(tam)
    reloj=pg.time.Clock()
    cerrar=False

while not cerrar:
    for evento in pg.event.get():
        if evento.type==pg.QUIT:
            cerrar= True
        if evento.type==pg.MOUSEMOTION:
            if pg.mouse.get_pressed()[0]:
                pos=pg.mouse.get_pos()
                topologia.append(pos)

    pantalla.fill(pg.color.Color('black'))

    for punto in topologia:
        pg.draw.circle(pantalla,pg.color.Color('white'),punto,3)



    pg.display.flip()
    reloj.tick(60)

#print(topologia[0])

mygng = gng(topologia,tam)


mygng.start()


# tam=[600,600]
# pantalla=pg.display.set_mode(tam)
# reloj=pg.time.Clock()
# pg.font.init()
# cerrar=False
# pos=[0,0]
# while not cerrar:
#     for evento in pg.event.get():
#         if evento.type==pg.QUIT:
#             cerrar= True

#     pantalla.fill(pg.color.Color('black'))

#     for arista in mygng.grafo.aristas:
#             pg.draw.line(pantalla,pg.color.Color('red'),arista.nodos[0].posicion,arista.nodos[1].posicion,1)

#     for nodo in mygng.grafo.nodos:
#         pg.draw.circle(pantalla,pg.color.Color('blue'), list(map(int,nodo.posicion)),3)
#         #text_to_screen(pantalla,nodo.id,nodo.posicion)

#     for punto in topologia:
#         pg.draw.circle(pantalla,pg.color.Color('white'),punto,6)



#     pg.display.flip()
#     reloj.tick(5)
