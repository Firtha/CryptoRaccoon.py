import sys
from pygame.constants import *
import game

# Draw text : A function to draw some text on the screen, take multiple parameter
def draw_text(text, font, color, surface, x, y, center):
    textobj = font.render(text, 1, color)  # Create a textobject based on the text received as input
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.topleft = (x, y)  # Define the rectangle x,y position
    if center == True:
        surface_rect = surface.get_rect()  # Get the screen rect x and y data
        textrect.centerx = surface_rect.centerx  # Synchronize the rect x center of the text are to the screen
    surface.blit(textobj, textrect)


# Main_menu : create the menu window
def main_menu(pygame, font, screen, screen_rect):
    click = False
    running = True
    while running:
        # Define mouse click to false
        mx, my = pygame.mouse.get_pos()  # Init mouse cursor position for the menu
        init_game_background(pygame, screen)  # Start the init_game_background function
        draw_text('MENU', font, (255, 255, 255),
                  screen, 300, 50, True)  # Draw the text menu
        button_1 = pygame.Rect(250, 200, 400,
                               100)  # Init button_1 rectangleparameters -> Rect(left, top, width, height)
        button_1.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value
        button_2 = pygame.Rect(250, 400, 400,
                               100)  # Init button_2 rectangleparameters -> Rect(left, top, width, height)
        button_2.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value

        if button_1.collidepoint((mx, my)):
            if click:
                click = False
                print("Start button clicked")
                game.game(pygame, screen)
        if button_2.collidepoint((mx, my)):
            if click:
                click = False
                print("Stats button clicked")
                running = False
                main_menu(pygame, font, screen, screen_rect)

        pygame.draw.rect(screen, (255, 255, 255), button_1)  # Draw the menubutton_1
        pygame.draw.rect(screen, (255, 255, 255), button_2)  # Draw the menubutton_2

        draw_text('START', font, (0, 0, 0), screen, 300, 227, True)
        draw_text('STATS', font, (0, 0, 0), screen, 300, 427, True)

        # Event loop that will check if any input event occurs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape has been pushed")
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()  # Refresh screen


# Initialisation du background
def init_game_background(pygame, screen):
    fond = pygame.image.load("img/background.jpg").convert()
    screen.blit(fond, (0, 0))

