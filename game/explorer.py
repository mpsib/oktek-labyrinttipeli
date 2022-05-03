import pygame
import os

class Explorer:
    def __init__(this, startingX, startingY, screen) -> None:
        this.x = startingX
        this.y = startingY
        this.image = pygame.image.load(os.path.join('assets', 'stickman.png'))
        this.screen = screen

    
    def draw(this):
        drawX = this.x * this.image.get_width()
        drawY = this.y * this.image.get_height()
        this.screen.blit(this.image, (drawX, drawY))

    def move(this, x, y):
        this.x += x
        this.y += y
