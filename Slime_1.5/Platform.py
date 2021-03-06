from pygame.sprite import Sprite
from pygame.image import load


class Platform(Sprite):
    def __init__(self, x, y, file):
        Sprite.__init__(self)
        self.image = load(file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
