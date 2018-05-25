import ast
import random
import json

def insertPunto(punto1,punto2,archivo2):
	archivo1 = open(archivo2)	

def gng(archivo1,archivo2):
	archivo1 = open(archivo1,'r')
	archivo2 = open(archivo2,'w')
	stringP = archivo1.read()
	archivo1.close()
	rX1 = random.randint(0,700)
	rY1 = random.randint(0,700)
	rX2 = random.randint(0,700)
	rY2 = random.randint(0,700)
	
	puntos1 = ast.literal_eval(stringP)
	print(json.dumps(puntos1,indent=4))


'''[(id viene),(x,y), (Id va) ]'''

gng('diccionario','puntos')
