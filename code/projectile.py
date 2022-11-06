import pygame

class Bullet(object):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (100, 100))

    def update(self):
        self.rect.x += 5

    # def draw(self,win):
    #     pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)