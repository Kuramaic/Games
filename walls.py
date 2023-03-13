import pygame
pygame.init()

class Wall():
    def __init__(self, x, y, filename, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.rect= self.image.get_rect(center=(x,y))
        self.image= pygame.transform.scale(self.image, (self.image.get_rect().width * w, self.image.get_rect().height * h))