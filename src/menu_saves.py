import sys
from pygame.constants import *
import game
import utils
import saves_manager


# Saves_listing : Create the user saves (unfinished games only) list window
def saves_listing(pygame, font, screen, screen_rect, userName):
    print("User saves list incoming")
    savedGames = saves_manager.getUserUnfinishedGames(userName)

    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        utils.init_game_background(pygame, screen)                                          # Start the init_game_background function
        utils.draw_text('Unfinished games', font, (255, 255, 255), screen, 300, 50, True)   # Draw the text menu

        if len(savedGames) == 0:
            button_1 = pygame.Rect(250, 200, 600, 100)
            button_1.centerx = screen_rect.centerx
            pygame.draw.rect(screen, (255, 255, 255), button_1)  # Draw the menubutton_1
            utils.draw_text("Time to start a new game !", font, (0, 0, 0), screen, 300, 227, True)
        else:
            startY = 200
            buttons = []
            for savedGame in savedGames:
                button = pygame.Rect(250, startY, 600, 100)
                button.centerx = screen_rect.centerx
                pygame.draw.rect(screen, (255, 255, 255), button)
                utils.draw_text(savedGame[1][:10] + " -> " + savedGame[2], font, (0, 0, 0), screen, 300, startY + 27, True)
                buttons.append(button)
                startY += 200


        # Event loop that will check if any input event occurs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape has been pushed -> Return to main_menu")
                    return False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if len(savedGames) > 0 and buttons[0].collidepoint((mx, my)):
            if click:
                print("First save resumed")
                print("Game launch should occur now")
                return True
        if len(savedGames) > 0 and buttons[1].collidepoint((mx, my)):
            if click:
                print("Second save resumed")
                print("Game launch should occur now")
                return True
        if len(savedGames) > 0 and buttons[2].collidepoint((mx, my)):
            if click:
                print("Third save resumed")
                print("Game launch should occur now")
                return True

        pygame.display.flip()  # Refresh screen