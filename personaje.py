import pygame,sys
import threading
from time import sleep 
ruta = 'media/Imagenes/Sprites/'

class personaje:
	
	

	def __init__(self, arriba, abajo, izquierda , derecha, ancho, largo,limite ,posicionInicial, skin):
		self.imagen = pygame.image.load(ruta+skin)
		self.posicionInicial = posicionInicial
		self.derecha = derecha
		self.izquierda = izquierda
		self.abajo = abajo
		self.limite = limite
		self.arriba = arriba 
		self.identacion =0
		self.ancho=ancho 
		self.largo=largo
		self.velocidad = 5
		self.Rectangulo = pygame.Rect(posicionInicial[0],posicionInicial[1],46,64)
		
		
		
		
	def getSpawn(self , Mapa): 
		Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]] = (self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	

	def movimiento(self , Mapa):
		if pygame.key.get_pressed()[276] == 1 :
			
			#screen.fill((255,255,255))
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]]=0
			self.identacion = self.identacion +1
			self.posicionInicial[0] -=self.velocidad
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]] = (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.izquierda*self.largo,self.ancho,self.largo)
			Mapa.limpiar(self.posicionInicial)
			#sleep(0.05)
			
		if pygame.key.get_pressed()[274] == 1 :
			
			#screen.fill((255,255,255))
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]] = 0
			self.identacion = self.identacion +1
			self.posicionInicial[1] +=self.velocidad
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]] = (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.abajo*self.largo,self.ancho,self.largo)
			Mapa.limpiar(self.posicionInicial)
			#sleep(0.05)					
				
		if pygame.key.get_pressed()[275] == 1 :
			
			#screen.fill((255,255,255))
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]]=0
			self.identacion = self.identacion +1
			self.posicionInicial[0] +=self.velocidad
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]]=(self.imagen,self.posicionInicial,self.identacion*self.ancho,self.derecha*self.largo,self.ancho,self.largo)
			Mapa.limpiar(self.posicionInicial)
			#sleep(0.05)
			
		if pygame.key.get_pressed()[273] == 1 :
			
			#screen.fill((255,255,255))
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]]=0
			self.identacion = self.identacion +1
			self.posicionInicial[1] -=self.velocidad
			Mapa.MatrizLogica[self.posicionInicial[0]][self.posicionInicial[1]]=(self.imagen,(self.posicionInicial),self.identacion*self.ancho,self.arriba*self.largo,self.ancho,self.largo)
			Mapa.limpiar(self.posicionInicial)
			#sleep(0.05)	
				
		if self.identacion >= self.limite:
			self.identacion = 0	
		
		
		self.Rectangulo.left,self.Rectangulo.top = self.posicionInicial[0],self.posicionInicial[1]		

class Orda:
	def __init__(self, personajes):
		self.personajes = personajes 
		
	
	def movimiento(self, Matriz):	    
		test = Matriz
		for i in self.personajes:   
	    
		    i.movimiento(test)
	
	def setPersonaje(self, personaje ):
		self.personajes.append(personaje)		 	





class Mouse:
	def __init__(self):
		self.estado = False
		self.Rectangulo= (0,0,0,0)
		self.a=(0,0)
	
	def seleccion(self,screen, personajes):
		
		
		if pygame.mouse.get_pressed()[0]==1 and self.estado ==False :
				self.a = pygame.mouse.get_pos()
				print (self.a)
				self.estado=True
		if pygame.mouse.get_pressed()[0]==0 and self.estado==True:
					b=pygame.mouse.get_pos()
					print (b)
					self.estado = False
					if (self.a[0]<b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],self.a[1],(b[0]-self.a[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(b[0],self.a[1],(self.a[0]-b[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]<b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],b[1],(b[0]-self.a[0]),(self.a[1]-b[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(b[0],b[1],(self.a[0]-b[0]),(self.a[1]-b[1]))
					for i in personajes:
                       
						if self.Rectangulo.contains(i.Rectangulo)==1:
							print("True")
							screen.blit(pygame.image.load('media/Imagenes/seleccion.png'),i.posicionInicial)

							
						    							    
							    
		
		 			 			 
					 
				
				
