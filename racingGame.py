# Written by John Burton
from pydoc import ModuleScanner
import pygame
import random
import winIncrease
import time

 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

clock = pygame.time.Clock()

X = 600
Y = 600
window = pygame.display.set_mode((X, Y))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 204, 0)
 
# Fill the scree with white color
window.fill(WHITE)

# Text
# font = pygame.font.Font('freesansbold.ttf', 32)
# print(pygame.font.get_fonts())
font = pygame.font.SysFont("arialrounded", 32)
text = font.render('Red: Lap 1', True, RED, WHITE)
text2 = font.render('Green: Lap 1', True, GREEN, WHITE)
text3 = font.render('Blue: Lap 1', True, BLUE, WHITE)
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3= text3.get_rect()
textRect.center = (X / 2, (Y / 2) - 80)
textRect2.center = (X / 2, (Y / 2) - 40)
textRect3.center = (X / 2, Y / 2)
restartText = font.render('Restart' , True , WHITE)
startText = font.render('Start' , True , WHITE)
threeText = font.render('3!' , True , WHITE)
twoText = font.render('2!' , True , WHITE)
oneText = font.render('1!' , True , WHITE)

radius = 25

# object current co-ordinates 
red_x = random.randrange(25, 575)
red_y = random.randrange(25, 575)
blue_x = random.randrange(25, 575)
blue_y = random.randrange(25, 575)
green_x = random.randrange(25, 575)
green_y = random.randrange(25, 575)

# velocity / speed of movement
red_vel = 1
blue_vel = 1
green_vel = 1

# location variables
redAllRight = False
redAllDown = False
redAllLeft = True
redAllUp = True

blueAllRight = False
blueAllDown = False
blueAllLeft = True
blueAllUp = True

greenAllRight = False
greenAllDown = False
greenAllLeft = True
greenAllUp = True

redHitRight = False
redHitBottom = False
greenHitRight = False
greenHitBottom = False
blueHitRight = False
blueHitBottom = False

# laps
redLaps = 1
blueLaps = 1
greenLaps = 1
endLapsNumber = 6
endLaps = False
winner = ''

isRunning = True
startGame = False

pygame.display.set_caption('Circle Racing Game')

####### Start Screen ########
# Before start is pressed
while startGame == False:
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pygame.draw.rect(window,BLACK,[228,50,140,40])
        window.blit(startText , (260,55))
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 228 <= mouse[0] <= 228+140 and 50 <= mouse[1] <= 50+40:
                red_x = radius + 25
                red_y = radius + 25
                blue_x = radius + 25
                blue_y = radius + 25
                green_x = radius + 25
                green_y = radius + 25
                startGame = True

                pygame.draw.rect(window,BLACK,[228,50,140,40])
                window.blit(threeText , (285,55))
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(window,BLACK,[228,50,140,40])
                window.blit(twoText , (285,55))
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(window,BLACK,[228,50,140,40])
                window.blit(oneText , (285,55))
                pygame.display.update()
                time.sleep(1)

    
    ###### Red ######

    # move red right
    if redHitRight == False:
        red_x += 4 * .04
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_x >= 600-radius:
            redHitRight = True

    # move red left
    if redHitRight == True:
        red_x -= 4 * .04
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_x <= 25:
            redHitRight = False

    # move red down
    if redHitBottom == False:
        red_y += 5* .04
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_y >= 600-radius:
            redHitBottom = True

    # move red up
    if redHitBottom == True:
        red_y -= 3* .04
        pygame.draw.circle(window, RED, [red_x, red_y], 25, 0)

        if red_y <= 25:
            redHitBottom = False


    #################


    ##### Green #####

    # move green right
    if greenHitRight == False:
        green_x += 3 * .04
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_x >= 600-radius:
            greenHitRight = True

    # move green left
    if greenHitRight == True:
        green_x -= 3 * .04
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_x <= 25:
            greenHitRight = False

    # move green down
    if greenHitBottom == False:
        green_y += 4 * .04
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_y >= 600-radius:
            greenHitBottom = True

    # move green up
    if greenHitBottom == True:
        green_y -= 4 * .04
        pygame.draw.circle(window, GREEN, [green_x, green_y], 25, 0)

        if green_y <= 25:
            greenHitBottom = False

    #################


    ##### Blue ######

    # move blue right
    if blueHitRight == False:
        blue_x += 3 * .04
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_x >= 600-radius:
            blueHitRight = True

    # move blue left
    if blueHitRight == True:
        blue_x -= 5 * .04
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_x <= 25:
            blueHitRight = False

    # move blue down
    if blueHitBottom == False:
        blue_y += 4 * .04
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_y >= 600-radius:
            blueHitBottom = True

    # move blue up
    if blueHitBottom == True:
        blue_y -= 2.5 * .04
        pygame.draw.circle(window, BLUE, [blue_x, blue_y], 25, 0)

        if blue_y <= 25:
            blueHitBottom = False

    #################
    
    pygame.draw.rect(window,BLACK,[228,50,140,40])
    window.blit(startText , (257,55))
    pygame.display.update()
    # Comment me out if you want more colors
    window.fill((255, 255, 255))

#########################




while isRunning:

    window.fill(WHITE)

    window.blit(text, textRect)
    window.blit(text2, textRect2)
    window.blit(text3, textRect3)

    pygame.time.delay(100)

    events = pygame.event.get()

    # exit the game
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            print(mouse)

            # Game restarts if clicked
            if 450 <= mouse[0] <= 450+140 and 50 <= mouse[1] <= 50+40:
                red_x = radius + 25
                red_y = radius + 25
                blue_x = radius + 25
                blue_y = radius + 25
                green_x = radius + 25
                green_y = radius + 25

                redAllRight = False
                redAllDown = False
                redAllLeft = True
                redAllUp = True

                blueAllRight = False
                blueAllDown = False
                blueAllLeft = True
                blueAllUp = True

                greenAllRight = False
                greenAllDown = False
                greenAllLeft = True
                greenAllUp = True

                redLaps = 1
                blueLaps = 1
                greenLaps = 1
                endLapsNumber = 6
                endLaps = False
                winner = ''
                
        
    mouse = pygame.mouse.get_pos()

    while endLaps == False:

        pygame.time.delay(10)
        window.fill(WHITE)

        pygame.draw.rect(window, BLACK, pygame.Rect(100, 100, 375, 370), 3)

        text = font.render(('Red: Lap '+ str(redLaps)), True, RED, WHITE)
        text2 = font.render(('Green: Lap '+ str(greenLaps)), True, GREEN, WHITE)
        text3 = font.render(('Blue: Lap '+ str(blueLaps)), True, BLUE, WHITE)

        window.blit(text, textRect)
        window.blit(text2, textRect2)
        window.blit(text3, textRect3)

        ##### red circle #####
        # move right
        if red_x < 550 - radius and redAllLeft == True and redAllUp == True:
            red_x += random.randrange(8)
            pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
        elif red_x >= 550-radius and redAllRight == False:
            redAllRight = True
            redAllLeft = False

        # move down
        if red_y < 550-radius and redAllRight == True and redAllUp == True:
            red_y += random.randrange(8)
            pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
        elif red_y >= 500-radius and redAllDown == False:
            redAllDown = True
            redAllUp = False

        # move left
        if red_x > radius + radius and redAllRight == True and redAllDown == True:
            red_x -= random.randrange(8)
            pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
        elif red_x <= radius + radius and redAllLeft == False:
            redAllLeft = True
            redAllRight = False
        
        # move up
        if red_y > radius + radius and redAllDown == True and redAllLeft == True:
            red_y -= random.randrange(8)
            pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
        elif red_y <= radius + radius and redAllUp == False:
            redAllUp = True
            redAllDown = False
            redLaps += 1
            pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
            if redLaps == endLapsNumber:
                pygame.draw.circle(window, RED, [red_x, red_y], radius, 0)
                winner = 'Red'
                endLaps = True
        ##################
        

        ##### blue circle #####
        # move right
        if blue_x < 550 - radius and blueAllLeft == True and blueAllUp == True:
            blue_x += random.randrange(8)
            pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
        elif blue_x >= 550-radius and blueAllRight == False:
            blueAllRight = True
            blueAllLeft = False

        # move down
        if blue_y < 550 - radius and blueAllRight == True and blueAllUp == True:
            blue_y += random.randrange(8)
            pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
        elif blue_y >= 550-radius and blueAllDown == False:
            blueAllDown = True
            blueAllUp = False

        # move left
        if blue_x > radius + radius and blueAllRight == True and blueAllDown == True:
            blue_x -= random.randrange(8)
            pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
        elif blue_x <= radius + radius and blueAllLeft == False:
            blueAllLeft = True
            blueAllRight = False

        # move up
        if blue_y > radius + radius and blueAllDown == True and blueAllLeft == True:
            blue_y -= random.randrange(8)
            pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
        elif blue_y <= radius + radius and blueAllUp == False:
            blueAllUp = True
            blueAllDown = False
            blueLaps += 1
            pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
            if blueLaps == endLapsNumber:
                pygame.draw.circle(window, BLUE, [blue_x, blue_y], radius, 0)
                winner = 'Blue'
                endLaps = True
        ##################


        ##### green circle #####
        # move right
        if green_x < 550 - radius and greenAllLeft == True and greenAllUp == True:
            green_x += random.randrange(8)
            pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
        elif green_x >= 550-radius and greenAllRight == False:
            greenAllRight = True
            greenAllLeft = False

        # move down
        if green_y < 550 - radius and greenAllRight == True and greenAllUp == True:
            green_y += random.randrange(8)
            pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
        elif green_y >= 550-radius and greenAllDown == False:
            greenAllDown = True
            greenAllUp = False

        # move left
        if green_x > radius + radius and greenAllRight == True and greenAllDown == True:
            green_x -= random.randrange(8)
            pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
        elif green_x <= radius + radius and greenAllLeft == False:
            greenAllLeft = True
            greenAllRight = False

        # move up
        if green_y > radius + radius and greenAllDown == True and greenAllLeft == True:
            green_y -= random.randrange(8)
            pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
        elif green_y <= radius + radius and greenAllUp == False:
            greenAllUp = True
            greenAllDown = False
            greenLaps += 1
            pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
            if greenLaps == endLapsNumber:
                pygame.draw.circle(window, GREEN, [green_x, green_y], radius, 0)
                winner = 'Green'
                endLaps = True
        ##################

        # Winner
        if endLaps == True:
            if winner == 'Red':
                window.fill(RED)
                time.sleep(2)
                textWinner = font.render(winner + ' WINS!', True, RED, WHITE)
                window.blit(textWinner, textRect)
                winIncrease.redWinIncrease()
                pygame.display.update()

            if winner == 'Green':
                window.fill(GREEN)
                time.sleep(2)
                textWinner = font.render(winner + ' WINS!', True, GREEN, WHITE)
                window.blit(textWinner, textRect)
                winIncrease.greenIncrease()
                pygame.display.update()

            if winner == 'Blue':
                window.fill(BLUE)
                time.sleep(2)
                textWinner = font.render(winner + ' WINS!', True, BLUE, WHITE)
                window.blit(textWinner, textRect)
                winIncrease.blueIncrease()
                pygame.display.update()

            time.sleep(2)
            redTotalText = font.render("Red Wins: " + str(winIncrease.getRedWins()), True, RED, WHITE)
            blueTotalText = font.render("Blue Wins: " + str(winIncrease.getBlueWins()), True, BLUE, WHITE)
            greenTotalText = font.render("Green Wins: " + str(winIncrease.getGreenWins()), True, GREEN, WHITE)
            window.blit(redTotalText, textRect3)
            window.blit(blueTotalText, textRect2)
            window.blit(greenTotalText, textRect)

            mouse = pygame.mouse.get_pos()

            # Draws rectangle for button
            pygame.draw.rect(window,BLACK,[450,50,140,40])

            # superimposing the text onto our button
            window.blit(restartText , (465,55))
        
            # updates the frames of the game
            pygame.display.update()
            

        pygame.display.update()

        # exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

# closes the pygame window 
pygame.quit()