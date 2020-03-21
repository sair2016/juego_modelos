import time
import pygame,sys,random
from personaje import *
from aura import *
import threading






class IEstrategiaAnimaciones:
	def evaluar (self, numero):
		pass
	
	def limpiar(self, posicion):
		pass
		
	def imprimir(self):
		pass
		
	def animarEspecifico(self, a):
		pass
		
				



		


class MapaEstandar(IEstrategiaAnimaciones):
	
	def __init__(self, screen):
		self.dimension=500
		self.MatrizLogica=[[0 for x in range(self.dimension)] for y in range(self.dimension)]
		for i in range (0,self.dimension):
		   for j in range (0,self.dimension):
			   self.MatrizLogica[i][j]= random.randint(0,2)
			   
		self.screen = screen

	def evaluar(self,numero):
		hierba= pygame.image.load('media/Imagenes/hierba.jpg')
		arbol= pygame.image.load('media/Imagenes/arbol.png')
		roca= pygame.image.load('media/Imagenes/roca.png')
		if numero == 0:
			return hierba
			
		elif numero == 1:
			return arbol
			
		elif numero == 2:
			return roca
		else:
			return int
			
		
			
	def limpiar(self, posicion):
		hierba= pygame.image.load('media/Imagenes/hierba.jpg')
		arbol= pygame.image.load('media/Imagenes/arbol.png')
		roca= pygame.image.load('media/Imagenes/roca.png')
		for i in range (round(posicion[1]/64)-2,round(posicion[1]/64)+2):
			for j in range (round(posicion[0]/46)-2,round(posicion[0]/46)+2):
				self.screen.blit(hierba,(j*46,i*64))
				if  self.MatrizLogica[i][j] == 1:
					self.screen.blit(arbol,(j*46,i*64))
				elif  self.MatrizLogica[i][j] == 2:
					self.screen.blit(roca,(j*46,i*64))
 
			
	def setMatriz(self,Matriz):
		self.MatrizLogica = Matriz
				   
	     	
	     	
		
	def imprimirMapa(self, screen):
	 self.MatrizLogica[0][0] = 3
	 self.MatrizLogica[1][2] = 3	 
	 hierba= pygame.image.load('media/Imagenes/hierba.jpg')
	 arbol= pygame.image.load('media/Imagenes/arbol.png')
	 roca= pygame.image.load('media/Imagenes/roca.png')
	 roca2= pygame.image.load('media/Imagenes/text.jpg')
	 for i in range (0,self.dimension):
		 for j in range (0,self.dimension):
			 screen.blit(hierba,(j*46,i*64))
				
			 if  self.MatrizLogica[i][j] == 1:
				 screen.blit(arbol,(j*46,i*64))
				
			 elif  self.MatrizLogica[i][j] == 2:
				 screen.blit(roca,(j*46,i*64))
				 
			 elif 	self.MatrizLogica[i][j] ==3:
				  screen.blit(roca2,(j*46,i*64))	
					

class MapaEventos(IEstrategiaAnimaciones):
	def __init__(self):
		d=500
		self.MatrizEventos=[[0 for x in range(d)] for y in range(d)]
		for i in range (0,d):
		   for j in range (0,d):
			   self.MatrizEventos[i][j]=0
		




def main():
	inicio = time.time()
	posX=50
	posY=50
	pygame.init()
	screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
	pygame.display.get_caption()
	principal_personaje = personaje(3,0,1,2,45.25,64,3,[posX,posY],'pain.png')
	mapa1 = MapaEstandar(screen)
	a = decorador(screen, principal_personaje, 5, 'polvo.png')
	Rect = pygame.Rect(0,0,10,10)
	principal_personaje.getSpawn(mapa1)
	personajes = [] 
	Orda1 = Orda(personajes)
	
	personajes.append(personaje(3,0,1,2,45.25,64,3,[0,0],'pain.png'))
	personajes.append(personaje(3,0,1,2,45.25,64,3,[46,0],'pain.png'))
	personajes.append(personaje(3,0,1,2,45.25,64,3,[46,64],'pain.png'))
	personajes.append(personaje(3,0,1,2,45.25,64,3,[92,64],'pain.png'))
	personajes.append(personaje(3,0,1,2,45.25,64,3,[92,128],'pain.png'))
	m = Mouse()
	Rect.left,Rect.top = pygame.mouse.get_pos()  
	
	mapa1.imprimirMapa(screen)
	#mapa1.limpiar(principal_personaje.posicionInicial,screen)		
	while(True):
		print (Rect.colliderect(principal_personaje.Rectangulo))
		#mapa1.imprimirMapa(screen)	
		#mapa1.limpiar(principal_personaje.posicionInicial,screen)
		tiempoEjecucion =round( time.time() - inicio)
		if pygame.key.get_pressed()[306] == 1:
			Orda1.movimiento(mapa1)
			
		else:
			principal_personaje.movimiento(mapa1)
			
		    
		#print(MatrizLogica)
		for evento in pygame.event.get():
			
			
			if evento.type == 12:
				sys.exit(0)
				
		
		for row in mapa1.MatrizLogica:
			for elem in row:
				if elem != 0 and elem != 1 and elem != 2 and elem != 3:
					screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
			
		m.seleccion(screen, personajes)												
		pygame.display.flip()
		pygame.display.update()		
	return 0 

main()









 
