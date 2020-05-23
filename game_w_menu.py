import pygame, sys
from pygame.locals import *

pygame.init()

# Init some basic parameters for the game (Screen size, font, icon, name)
pygame.display.set_caption('Crypto Raccoon')                #Define the window name
icon = pygame.image.load('img/icon.png')                    #Define the icon var
pygame.display.set_icon(icon)                               #Define the window icon
screen = pygame.display.set_mode((859, 1002))               #Define screen size
screen_rect = screen.get_rect()                             #Get screen size as a rectangle, allow us to center other rectangle elements based on the screen size
font = pygame.font.SysFont(None, 72)                        #Define the game font

#Draw text : A function to draw some text on the screen, take multiple parameter
def draw_text(text, font, color, surface, x, y, center):
    textobj = font.render(text, 1, color)                   #Create a textobject based on the text received as input
    textrect = textobj.get_rect()                           #Create a rectangle for the text
    textrect.topleft = (x, y)                               #Define the rectangle x,y position 
    if center == True :
        surface_rect = surface.get_rect()                   #Get the screen rect x and y data
        textrect.centerx = surface_rect.centerx             #Synchronize the rect x center of the text are to the screen
    surface.blit(textobj, textrect)                 

#Main_menu : create the menu window
def main_menu():
    click = False 
    running = True
    while running:
        #Define mouse click to false
        mx, my = pygame.mouse.get_pos()                     #Init mouse cursor position for the menu
        init_game_background()                              #Start the init_game_background function
        draw_text('MENU', font, (255, 255, 255),
         screen, 300, 50, True)                             #Draw the text menu
        button_1 = pygame.Rect(250, 200, 400, 100)          #Init button_1 rectangleparameters -> Rect(left, top, width, height)
        button_1.centerx = screen_rect.centerx              #The button x-center value is set to be equal to the screen x-center value
        button_2 = pygame.Rect(250, 400, 400, 100)          #Init button_2 rectangleparameters -> Rect(left, top, width, height)
        button_2.centerx = screen_rect.centerx              #The button x-center value is set to be equal to the screen x-center value
        
        if button_1.collidepoint((mx, my)):
            if click:
                click = False
                print("Start button clicked")
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                click = False
                print("Stats button clicked")
                running = False
                main_menu()

        pygame.draw.rect(screen, (255, 255, 255), button_1) #Draw the menubutton_1
        pygame.draw.rect(screen, (255, 255, 255), button_2)     #Draw the menubutton_2
        
        draw_text('START', font, (0, 0, 0), screen, 300, 227, True) 
        draw_text('STATS', font, (0, 0, 0), screen, 300, 427, True) 

        #Event loop that will check if any input event occurs
        for event in pygame.event.get():            
            if event.type == QUIT:
                running = False
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("escape has been pushed")
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()                               #Refresh screen   

        

#Initialisation du background
def init_game_background() :
    fond = pygame.image.load("img/background.jpg").convert()
    screen.blit(fond, (0,0))

# define the player persona position
def raccoon_player(x, y) :
    raccoon = pygame.image.load("img/raccoon.png").convert_alpha()
    screen.blit(raccoon, (x, y))

def game():
    #init player position in the screen and the image
    raccoon_Xpos = 0
    raccoon_Ypos = 880
    raccoon_new_Xpos = 0
    raccoon_new_Ypos = 0

    pygame.display.flip()
    #BOUCLE INFINIE
    running = True
    while running:
        for event in pygame.event.get():
            
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_DOWN :
                    raccoon_new_Ypos = 80
                    raccoon_Ypos += raccoon_new_Ypos
                if event.key == K_UP :
                    raccoon_new_Ypos = -80
                    raccoon_Ypos += raccoon_new_Ypos
                if event.key == K_RIGHT :
                    raccoon_new_Xpos = +75
                    raccoon_Xpos += raccoon_new_Xpos
                if event.key == K_LEFT :
                    raccoon_new_Xpos = -75
                    raccoon_Xpos += raccoon_new_Xpos
                if event.key == K_m :
                    running = False
                    main_menu()

            #if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            #    print("Zone dangereuse")

        #put your game code below :
        init_game_background()

        #check raccon's position on the screen
        if raccoon_Xpos <= 0 :
            raccoon_Xpos = 0
        elif raccoon_Xpos >= 660 : 
            raccoon_Xpos = 660
        
        if raccoon_Ypos <= 720 :
            raccoon_Ypos = 720
        elif raccoon_Ypos >= 880 : 
            raccoon_Ypos = 880
        

        raccoon_player(raccoon_Xpos, raccoon_Ypos)
        pygame.display.flip()

def game_menu():
    

main_menu()
    
