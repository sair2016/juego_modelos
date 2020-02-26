import pygame,sys


def main():
	pygame.init()
	screen = pygame.display.set_mode((500,500))
	pygame.display.get_caption()
	while(True):
		for evento in pygame.event.get():
			if evento.type == 12:
				sys.exit(0)
				
	return 0 

main()
