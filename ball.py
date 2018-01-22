import pygame
class Ball(pygame.sprite.Sprite):
    # makes ball
    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.Surface((self.RADIUS, self.RADIUS))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = 5

    # moves ball
    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.speedx = -self.speedx

    # tells the ball what to do when it collides with the paddle
    def collide_paddle(self,paddle_sprite):
        if pygame.sprite.spritecollide(self,paddle_sprite, False):
            self.speedy = -self.speedy

    # tells the ball what to do when it collides with the bricks
    def collide_brick(self, brick_spirit):
        if pygame.sprite.spritecollide(self, brick_spirit, True):
            self.speedy = -self.speedy

