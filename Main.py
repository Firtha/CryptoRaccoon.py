import pygame
import sys
import main_menu


pygame.init()

# Init some basic parameters for the game (Screen size, font, icon, name)
pygame.display.set_caption('Crypto Raccoon')                #Define the window name
icon = pygame.image.load('img/icon.png')                    #Define the icon var
pygame.display.set_icon(icon)                               #Define the window icon
screen = pygame.display.set_mode((859, 1002))               #Define screen size
screen_rect = screen.get_rect()                             #Get screen size as a rectangle, allow us to center other rectangle elements based on the screen size
font = pygame.font.SysFont(None, 72)                        #Define the game font

userName = main_menu.authenticate_user(pygame, font, screen, screen_rect)
print(userName)
main_menu.main_menu(pygame, font, screen, screen_rect, userName)
pygame.quit()
sys.exit()