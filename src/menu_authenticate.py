import sys

from pygame.constants import *
import game
import utils
import menu_stats
import menu_authenticate
import data_collector
import saves_manager


# Authenticate_user : Ask for an username and returns it to Main.py
def authenticate_user(pygame, font, screen, screen_rect):
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    click = False
    text = ''
    done = False
    font_s = pygame.font.SysFont(None, 48)                        #Define the game font


    while not done:
        mx, my = pygame.mouse.get_pos() 
        utils.init_game_background(pygame, screen)              # Start the init_game_background function
        utils.draw_text('WHO ARE YOU ?', font, (255, 255, 255),
                        screen, 300, 350, True)                  # Draw the text menu
        input_box = pygame.Rect(250, 410, 400, 80)             # Init button_1 rectangleparameters -> Rect(left, top, width, height)
        input_box.centerx = screen_rect.centerx                 # The button x-center value is set to be equal to the screen x-center value

        validate_button = pygame.Rect(250, 510, 200, 40)
        validate_button.centerx = screen_rect.centerx          

        pygame.draw.rect(screen, color, input_box)    # Draw the menubutton_1
        pygame.draw.rect(screen, (255, 255, 255), validate_button)    # Draw the menubutton_1
        utils.draw_text('validate', font_s, (0, 0, 0), screen, 300, 515, True)  
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
                if validate_button.collidepoint((mx, my)):
                    print("button validate clicked")
                    done = True

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
        


        txt_surface = font.render(text, True, (0, 0, 0))
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 20))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text