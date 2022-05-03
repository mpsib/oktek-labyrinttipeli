import random
import pygame
import os
from game.explorer import Explorer
from game.stage import stage, stageSC, randomizedStage
from game.Astar import AStar

imageSize = 50

class Game:
    def __init__(this, screen, level) -> None:
        this.screen = screen
        this.wall = pygame.image.load(os.path.join('assets', 'walltop.png'))
        this.floor = pygame.image.load(os.path.join('assets', 'floor.png'))
        this.start = pygame.image.load(os.path.join('assets', 'start.png'))
        this.exit = pygame.image.load(os.path.join('assets', 'exit.png'))
        this.visited = pygame.image.load(os.path.join('assets', 'visit.png'))
        this.path = pygame.image.load(os.path.join('assets', 'path.png'))
        if level == 1:
            s = randomizedStage()
            this.stage = s
        elif level == 2:
            this.stage = stageSC
        elif level == 3:
            this.stage = stage
        this.stageHeight = len(this.stage)
        this.stageWidth = len(this.stage[0])
        this.controller = 'player'
        this.startX = random.randint(0, 14)
        this.startY = random.randint(0, 9)
        this.explorer = Explorer(this.startX, this.startY, this.screen)
        this.exitX = random.randint(0, 14)
        this.exitY = random.randint(0, 9)
        while this.startX == this.exitX and this.startY == this.exitY:
            print('Start and exit overlap; retrying exit placement')
            this.exitX = random.randint(0, 14)
            this.exitY = random.randint(0, 9)
        this.astar = AStar(screen, this.stage, this.exitX, this.exitY)
    
    def handleEvent(this, event):
        # arrow buttons
        if this.controller == 'player' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if this.explorer.x > 0:
                    if 'r' in this.stage[this.explorer.y][this.explorer.x-1]:
                        this.explorer.move(-1,0)

            if event.key == pygame.K_RIGHT:
                if this.explorer.x < this.stageWidth:
                    if 'r' in this.stage[this.explorer.y][this.explorer.x]:
                        this.explorer.move(1,0)

            if event.key == pygame.K_UP:
                if this.explorer.y > 0:
                    if 'd' in this.stage[this.explorer.y-1][this.explorer.x]:
                        this.explorer.move(0,-1)

            if event.key == pygame.K_DOWN:
                if this.explorer.y < this.stageHeight:
                    if 'd' in this.stage[this.explorer.y][this.explorer.x]:
                        this.explorer.move(0,1)
        # TODO button(s) to activate algorithm
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                this.astar.start(this.explorer.x, this.explorer.y)
            if event.key == pygame.K_o:
                this.astar.visited = []
                this.astar.path = []
        # TODO button(s) to reset exit, reset player location

    def draw(this):
        for y in range(this.stageHeight):
            for x in range(this.stageWidth):
                # draw floor
                this.screen.blit(this.floor, (x*imageSize,y*imageSize))
                # draw walls
                #top
                if y == 0:
                    this.screen.blit(this.wall, (x*imageSize,y*imageSize))
                elif 'd' not in this.stage[y-1][x]:
                    this.screen.blit(this.wall, (x*imageSize,y*imageSize))
                #left
                wallLeft = pygame.transform.rotate(this.wall, 90)
                if x == 0:
                    this.screen.blit(wallLeft, (x*imageSize,y*imageSize))
                elif 'r' not in this.stage[y][x-1]:
                    this.screen.blit(wallLeft, (x*imageSize,y*imageSize))
                #bottom
                wallBottom = pygame.transform.rotate(this.wall, 180)
                if y == this.stageHeight-1:
                    this.screen.blit(wallBottom, (x*imageSize,y*imageSize))
                elif 'd' not in this.stage[y][x]:
                    this.screen.blit(wallBottom, (x*imageSize,y*imageSize))
                #right
                wallRight = pygame.transform.rotate(this.wall, 270)
                if x == this.stageWidth-1:
                    this.screen.blit(wallRight, (x*imageSize,y*imageSize))
                elif 'r' not in this.stage[y][x]:
                    this.screen.blit(wallRight, (x*imageSize,y*imageSize))

        # Visited nodes 
        for n in this.astar.visited:
            this.screen.blit(this.visited, (n.x*imageSize, n.y*imageSize))
        # Path nodes
        for n in this.astar.path:
            this.screen.blit(this.path, (n.x*imageSize, n.y*imageSize))

        this.screen.blit(this.exit, (this.exitX*imageSize, this.exitY*imageSize))
        this.screen.blit(this.start, (this.startX*imageSize, this.startY*imageSize))

        # draw explorer
        this.explorer.draw()