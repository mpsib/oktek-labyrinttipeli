from turtle import width
import pygame

from game.explorer import Explorer
from game.game import Game

pygame.init()
imageSize = 50
# for now support only 10x15 stages
stageH = 10
stageW = 15
screen = pygame.display.set_mode((stageW * imageSize,stageH * imageSize))
pygame.display.set_caption("Labyrinth")

clock = pygame.time.Clock()

game = Game(screen, 1)

while True:
    for event in pygame.event.get():
        game.handleEvent(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                game = Game(screen, 3)
            if event.key == pygame.K_k:
                game = Game(screen, 2)
            if event.key == pygame.K_j:
                game = Game(screen, 1)
        if event.type == pygame.QUIT:
            exit()

    ##  screen drawing functions
    screen.fill((0,0,0))
    game.draw()
    #update screen
    pygame.display.flip()
    
    ##  advance time (by framerate)
    clock.tick(60)