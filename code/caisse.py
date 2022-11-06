import pygame

class Caisse(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.image.load('../graphics/decor/caisse/caisse.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)

	def update(self,x_shift, y_shift):
		self.rect.x += x_shift
		self.rect.y += y_shift