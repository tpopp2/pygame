#Tyler and Joe's first game
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("The Game") # Change later?
clock = pygame.time.Clock()

x = 100
y = 200

pygame.draw.rect(DISPLAYSURF, (0,200,200), (x,y,20,20))

pygame.key.set_repeat(50,50)

while True:

    for event in pygame.event.get():

        pygame.draw.rect(DISPLAYSURF, (0,0,0), (x,y,20,20))
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5
                
        pygame.draw.rect(DISPLAYSURF, (0,200,200), (x,y,20,20))
        

    pygame.display.update()
    clock.tick(50)

