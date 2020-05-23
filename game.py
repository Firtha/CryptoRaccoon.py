import sys

from pygame.constants import *

# Initialisation du background
def init_game_background(pygame, screen):
    fond = pygame.image.load("img/background.jpg").convert()
    screen.blit(fond, (0, 0))


# define the player persona position
def raccoon_player(x, y, pygame, screen):
    raccoon = pygame.image.load("img/raccoon.png").convert_alpha()
    screen.blit(raccoon, (x, y))


def game(pygame, screen):
    # init player position in the screen and the image
    raccoon_Xpos = 0
    raccoon_Ypos = 880
    raccoon_new_Xpos = 0
    raccoon_new_Ypos = 0

    pygame.display.flip()
    # BOUCLE INFINIE
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_DOWN:
                    raccoon_new_Ypos = 80
                    raccoon_Ypos += raccoon_new_Ypos
                if event.key == K_UP:
                    raccoon_new_Ypos = -80
                    raccoon_Ypos += raccoon_new_Ypos
                if event.key == K_RIGHT:
                    raccoon_new_Xpos = +75
                    raccoon_Xpos += raccoon_new_Xpos
                if event.key == K_LEFT:
                    raccoon_new_Xpos = -75
                    raccoon_Xpos += raccoon_new_Xpos
                if event.key == K_m:
                    running = False
                    main_menu(pygame, font, screen, screen_rect)

            # if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            #    print("Zone dangereuse")

        # put your game code below :
        init_game_background(pygame, screen)

        # check raccon's position on the screen
        if raccoon_Xpos <= 0:
            raccoon_Xpos = 0
        elif raccoon_Xpos >= 660:
            raccoon_Xpos = 660

        if raccoon_Ypos <= 720:
            raccoon_Ypos = 720
        elif raccoon_Ypos >= 880:
            raccoon_Ypos = 880

        raccoon_player(raccoon_Xpos, raccoon_Ypos, pygame, screen)
        pygame.display.flip()
