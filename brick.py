import pygame
class Brick(pygame.sprite.Sprite):

    # creates the bricks
    def __init__(self, width, color):
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.image = pygame.Surface((width,self.BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

