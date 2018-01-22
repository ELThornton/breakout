import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    # Constants that will be used in the program
    pygame.init()
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =(APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # this set the frames per second
    fps = 60
    fps_clock = pygame.time.Clock()


    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH,APPLICATION_HEIGHT),0,32)
    # this set the paddle in to breakout.
    paddle_group = pygame.sprite.Group()
    new_paddle = paddle.Paddle(WHITE)
    new_paddle.rect.x = 200
    new_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(new_paddle.image, new_paddle.rect)
    paddle_group.add(new_paddle)

    block_group = pygame.sprite.Group()
    # this set the ball in to breakout.
    new_ball = ball.Ball(WHITE,APPLICATION_WIDTH,APPLICATION_HEIGHT)
    new_ball.rect.x = 200
    new_ball.rect.y = 200
    # these rows from 48 to 143 set the brick into breakout.
    originalx = 0
    originaly = BRICK_Y_OFFSET
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, RED)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx

    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, RED)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx


    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, ORANGE)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx
    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, ORANGE)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx

    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, YELLOW)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx
    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, YELLOW)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx

    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, GREEN)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx
    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, GREEN)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx

    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, CYAN)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx
    originaly = originaly + 8 + BRICK_SEP
    originalx = 0
    for x in range(BRICKS_PER_ROW):
        new_brick = brick.Brick(BRICK_WIDTH, CYAN)
        new_brick.rect.x = originalx
        new_brick.rect.y = originaly
        mainSurface.blit(new_brick.image, new_brick.rect)
        block_group.add(new_brick)
        originalx = BRICK_WIDTH + BRICK_SEP + originalx

    while True:
        # quites pygame smoothly
        for even in pygame.event.get():
            if even.type == QUIT:
                pygame.quit()
                sys.exit()

        mainSurface.fill(BLACK)
        for bricks in block_group:
            mainSurface.blit(bricks.image,bricks.rect)
        new_paddle.move()
        mainSurface.blit(new_paddle.image, new_paddle.rect)
        new_ball.move()
        # gets a new turn to start
        if new_ball.rect.y > APPLICATION_HEIGHT:
            NUM_TURNS = NUM_TURNS - 1
            new_ball.rect.y = 300
            new_ball.rect.x = 200
            mainSurface.blit(new_ball.image, new_ball.rect)
        # ends game
        if NUM_TURNS == 0:
            mainSurface.fill(BLACK)
            my_font = pygame.font.SysFont("Arial", 94)
            my_label = my_font.render ("Game Over", 1, WHITE)
            mainSurface.blit(my_label,(0,150))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        # sets the collisions into pygame
        new_ball.collide_paddle(paddle_group)
        new_ball.collide_brick(block_group)
        mainSurface.blit(new_ball.image, new_ball.rect)

        pygame.display.update()
        fps_clock.tick(fps)
main()