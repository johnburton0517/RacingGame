# Importing the pygame module
import pygame
from pygame.locals import *

# Import randint method random module
from random import randint


pygame.init()

window = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

radius = 25


red_x = 100
red_y = 100
blue_x = 400
blue_y = 400
green_x = 50
green_y = 50

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 204, 0)

redHitRight = False
redHitBottom = False
greenHitRight = False
greenHitBottom = False
blueHitRight = False
blueHitBottom = False


while True:

    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    ###### Red ######

    # move red right
    if redHitRight == False:
        red_x += 4
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_x >= 600-radius:
            redHitRight = True

    # move red left
    if redHitRight == True:
        red_x -= 4
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_x <= 25:
            redHitRight = False

    # move red down
    if redHitBottom == False:
        red_y += 5
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_y >= 600-radius:
            redHitBottom = True

    # move red up
    if redHitBottom == True:
        red_y -= 3
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_y <= 25:
            redHitBottom = False


    #################


    ##### Green #####

    # move green right
    if greenHitRight == False:
        green_x += 3
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_x >= 600-radius:
            greenHitRight = True

    # move green left
    if greenHitRight == True:
        green_x -= 3
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_x <= 25:
            greenHitRight = False

    # move green down
    if greenHitBottom == False:
        green_y += 4
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_y >= 600-radius:
            greenHitBottom = True

    # move green up
    if greenHitBottom == True:
        green_y -= 4
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_y <= 25:
            greenHitBottom = False

    #################


    ##### Blue ######

    # move blue right
    if blueHitRight == False:
        blue_x += 3
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_x >= 600-radius:
            blueHitRight = True

    # move blue left
    if blueHitRight == True:
        blue_x -= 5
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_x <= 25:
            blueHitRight = False

    # move blue down
    if blueHitBottom == False:
        blue_y += 4
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_y >= 600-radius:
            blueHitBottom = True

    # move blue up
    if blueHitBottom == True:
        blue_y -= 2.5
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_y <= 25:
            blueHitBottom = False

    #################


    pygame.display.update()
    window.fill((255, 255, 255))
