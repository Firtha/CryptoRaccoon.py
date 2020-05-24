import sys

from pygame.constants import *
import game
import utils


def authenticate(pygame, font, screen, screen_rect):

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        utils.init_game_background(pygame, screen)  # Start the init_game_background function
        utils.draw_text('WHO ARE YOU', font, (255, 255, 255),
                        screen, 300, 50, True)  # Draw the text menu
        input_box = pygame.Rect(250, 200, 400,
                                100)  # Init button_1 rectangleparameters -> Rect(left, top, width, height)
        input_box.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value

        pygame.draw.rect(screen, (255, 255, 255), input_box)  # Draw the menubutton_1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text

# Authenticate_user : Ask for an username
def authenticate_user():
    print("Ask for an username")


# Main_menu : create the menu window
def main_menu(pygame, font, screen, screen_rect):
    click = False
    running = True
    while running:
        # Define mouse click to false
        mx, my = pygame.mouse.get_pos()  # Init mouse cursor position for the menu
        utils.init_game_background(pygame, screen)  # Start the init_game_background function
        utils.draw_text('MENU', font, (255, 255, 255),
                  screen, 300, 50, True)  # Draw the text menu
        button_1 = pygame.Rect(250, 200, 400,
                               100)  # Init button_1 rectangleparameters -> Rect(left, top, width, height)
        button_1.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value
        button_2 = pygame.Rect(250, 400, 400,
                               100)  # Init button_2 rectangleparameters -> Rect(left, top, width, height)
        button_2.centerx = screen_rect.centerx  # The button x-center value is set to be equal to the screen x-center value

        pygame.draw.rect(screen, (255, 255, 255), button_1)  # Draw the menubutton_1
        pygame.draw.rect(screen, (255, 255, 255), button_2)  # Draw the menubutton_2

        utils.draw_text('START', font, (0, 0, 0), screen, 300, 227, True)
        utils.draw_text('STATS', font, (0, 0, 0), screen, 300, 427, True)

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

        if button_1.collidepoint((mx, my)):
            if click:
                click = False
                print("Start button clicked")
                game.game(pygame, font, screen, screen_rect)
        if button_2.collidepoint((mx, my)):
            if click:
                click = False
                print("Stats button clicked")
                running = False
                main_menu(pygame, font, screen, screen_rect)

        pygame.display.flip()  # Refresh screen


# Stats_listing : Create the best scores list window
def stats_listing():
    print("Stats list incoming")


# Saves_listing : Create the user saves (unfinished games only) list window
def saves_listing():
    print("User saves list incoming")