from gng import gng
import pygame as pg

'''nodo1 = Nodo(1,[1,2],2)
nodo2 = Nodo(2,[1,2],4)

arista = Arista(nodo1,nodo2,2,2)

grafo = Grafo()
grafo.addNodo(nodo1)

grafo.addNodo(nodo2)

grafo.addArista(arista)

grafo.findNodo(nodo1)'''

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
topologia=[[178, 95], [161, 112], [150, 145], [150, 172], [161, 195], [186, 218], [210, 232], [233, 239], [255, 250], [279, 267], [289, 291], [291, 316], [283, 332], [272, 346], [258, 361], [238, 381], [216,
396], [198, 412], [178, 435], [168, 448], [189, 476], [222, 488], [247, 498], [279, 509], [306, 513], [329, 514], [354, 519], [377, 510], [399, 502], [410, 477], [415, 457], [421, 428], [428, 406],
[448, 391], [471, 377], [487, 356], [497, 314], [476, 286], [461, 302], [439, 326], [431, 330], [424, 312], [427, 292], [435, 267], [448, 242], [444, 209], [439, 193], [429, 173], [410, 151], [387,
140], [360, 145], [340, 127], [344, 107], [357, 86], [351, 73], [325, 69], [311, 80], [300, 107], [282, 99], [274, 77], [261, 61], [246, 57], [230, 77], [231, 102], [220, 131]]


tam=[600,600]
pantalla=pg.display.set_mode(tam)
reloj=pg.time.Clock()
cerrar=False
 
print("1.- Usar topologia por default")
print("2.- Propia topologia")
op=input("opcion: ")
if op=='1' or op==1:
    cerrar=True
else:
    topologia=[]

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
    reloj.tick(30)

mygng = gng(topologia)


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
