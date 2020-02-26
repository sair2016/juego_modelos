import pygame,sys
ruta = 'media/Imagenes/Sprites'

class personaje:
	def self(self, arriba, abajo, derecha , izquierda, cantidad, posicionInicial):
		self.sheet = pygame.load.image(ruta+'link.png')
		self.sheet.set_clip(pygame.Rect(0,0))
	 	
		
		
