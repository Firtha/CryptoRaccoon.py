import sys
from pygame.constants import *
import utils
import saves_manager


# define the player persona position
def raccoon_player(x, y, pygame, screen):
    raccoon = pygame.image.load("../img/raccoon.png").convert_alpha()
    screen.blit(raccoon, (x, y))


def game(pygame, font, screen, screen_rect, userName, saveId, gameData):
    # init player position in the screen and the image
    raccoon_Xpos = 0
    raccoon_Ypos = 880
    raccoon_new_Xpos = 0
    raccoon_new_Ypos = 0

    # Fixed value for gravity
    gravity = 250

    # Fly time counting var
    flyTime = 0

    # Character state management vars
    allowMoves = True
    flyUp = False

    movingLeft = False
    movingRight = False
    moveTime = 0

    # If saveId = -1 then it means it's a new game
    if saveId == -1:
        saveId = saves_manager.getNextId(userName)
        userScore = 0.0
    else:
        userScore = float(gameData[2])


    print("Game ID is ", saveId)
    print("Starting score is ", userScore)

    fontScore = pygame.font.SysFont(None, 24)

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
                    targetOptions = game_menu(pygame, font, screen, screen_rect, userName)
                    if targetOptions == 1:
                        saves_manager.putSavedGame(userName, userScore, saveId)
                    if targetOptions == 1 or targetOptions == -1:
                        running = False

                # Jumping will block any other action and will trigger animation
                if event.key == K_UP and allowMoves:
                    allowMoves = False
                    flyUp = True
                    flyTime = 0
                    movingLeft = False
                    movingRight = False
                if event.key == K_RIGHT and allowMoves and not movingLeft and not movingRight:
                    movingRight = True
                    moveTime = 0
                if event.key == K_LEFT and allowMoves and not movingLeft and not movingRight:
                    movingLeft = True
                    moveTime = 0

            # if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            #    print("Zone dangereuse")

        # Gradual moves handling
        if movingLeft:
            raccoon_Xpos += -5
            moveTime += 1
            if moveTime >= 10:
                moveTime = 0
                movingLeft = False

        if movingRight:
            raccoon_Xpos += 5
            moveTime += 1
            if moveTime >= 10:
                moveTime = 0
                movingRight = False

        # Jump handling (quick at first then decelerate)
        if flyUp:
            raccoon_Ypos -= gravity * (40 - flyTime) / 500
            flyTime += 1
            if flyTime >= 40:
                flyUp = False
                flyTime = 0

        # Gravity handling (slow at first then accelerate)
        if not allowMoves and not flyUp:
            if (raccoon_Ypos + gravity * flyTime / 500) > 880:
                raccoon_Ypos = 880
                allowMoves = True
            else:
                raccoon_Ypos += gravity * flyTime / 500
            flyTime += 1

        # put your game code below :
        utils.init_game_background(pygame, screen)

        utils.draw_text('User : ' + userName, fontScore, (0, 0, 0),
                        screen, 15, 10, False)  # Draw the user name

        utils.draw_text('Score (BTC) :', fontScore, (0, 0, 0),
                        screen, 15, 30, False)  # Draw the score declaration

        utils.draw_text('%.4f' % userScore, fontScore, (0, 0, 0),
                        screen, 30, 45, False)  # Draw the score

        userScore += 0.00001

        # check raccon's position on the screen
        if raccoon_Xpos <= 0:
            raccoon_Xpos = 0
        elif raccoon_Xpos >= 660:
            raccoon_Xpos = 660

        raccoon_player(raccoon_Xpos, raccoon_Ypos, pygame, screen)
        pygame.display.flip()


# Returns value are used to define the next action to take (-1 quit without saving, 0 resume game and 1 quit&save)
def game_menu(pygame, font, screen, screen_rect, userName):
    click = False
    running = True
    while running:
        # Define mouse click to false
        mx, my = pygame.mouse.get_pos()  # Init mouse cursor position for the menu
        utils.init_game_background(pygame, screen)  # Start the init_game_background function
        utils.draw_text('PAUSE', font, (255, 255, 255),
                        screen, 300, 50, True)  # Draw the text menu
        button_1 = pygame.Rect(250, 200, 400,
                               100)  # Init button_1 rectangleparameters -> Rect(left, top, width, height)
        button_1.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value
        button_2 = pygame.Rect(250, 400, 400,
                               100)  # Init button_2 rectangleparameters -> Rect(left, top, width, height)
        button_2.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value
        button_3 = pygame.Rect(250, 600, 400,
                               100)  # Init button_3 rectangleparameters -> Rect(left, top, width, height)
        button_3.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value

        pygame.draw.rect(screen, (255, 255, 255), button_1)  # Draw the menubutton_1
        pygame.draw.rect(screen, (255, 255, 255), button_2)  # Draw the menubutton_2
        pygame.draw.rect(screen, (255, 255, 255), button_3)  # Draw the menubutton_3

        utils.draw_text('RESUME', font, (0, 0, 0), screen, 300, 227, True)
        utils.draw_text('SAVE AND QUIT', font, (0, 0, 0), screen, 300, 427, True)
        utils.draw_text('QUIT', font, (0, 0, 0), screen, 300, 627, True)

        # Event loop that will check if any input event occurs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape has been pushed -> RESUME")
                    return 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                print("RESUME button clicked")
                return 0
        if button_2.collidepoint((mx, my)):
            if click:
                print("SAVE&QUIT button clicked")
                return 1
        if button_3.collidepoint((mx, my)):
            if click:
                print("QUIT button clicked")
                return -1

        pygame.display.flip()  # Refresh screen
