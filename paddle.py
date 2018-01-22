import pygame
class Paddle(pygame.sprite.Sprite):
    # creates the paddle
    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    # moves the paddle
    def move(self):
        self.rect.x = pygame.mouse.get_pos()[0]

