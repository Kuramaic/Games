import pygame
pygame.init()

class Wall():
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.rect= self.image.get_rect(center=(x,y))
