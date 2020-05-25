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

        # Different interface according to the number of saved games (max is 3 unfinished games)
        if len(savedGames) == 0:
            button_1 = pygame.Rect(250, 200, 600, 100)
            button_1.centerx = screen_rect.centerx
            pygame.draw.rect(screen, (255, 255, 255), button_1)  # Draw the menubutton_1
            utils.draw_text("Time to start a new game !", font, (0, 0, 0), screen, 300, 227, True)
        else:
            delBtn = pygame.image.load("../img/delete-btn.png").convert_alpha()
            delBtn = pygame.transform.scale(delBtn, (60, 60))

            startY = 200
            buttons = []
            delCrosses = []
            currIndex = 0
            # Creates an array of buttons (build object + graphic display)
            # It simplifies the defining activity part, right after events listening
            for savedGame in savedGames:
                if currIndex < 3:
                    button = pygame.Rect(250, startY, 600, 100)
                    button.centerx = screen_rect.centerx
                    pygame.draw.rect(screen, (255, 255, 255), button)
                    utils.draw_text(savedGame[1][:10] + " -> " + savedGame[2], font, (0, 0, 0), screen, 300, startY + 27, True)
                    buttons.append(button)

                    screen.blit(delBtn, (750, startY + 27))
                    delCross = pygame.Rect(750, startY + 27, 50, 50)
                    delCrosses.append(delCross)

                    startY += 200
                currIndex += 1


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

        # We make the buttons effective only if we need them
        # Buttons    : Take back a saved game
        # DelCrosses : Delete the saved game on the current line
        if len(savedGames) > 0 and click:
            if buttons[0].collidepoint((mx, my)):
                print("First save resumed with id ", savedGames[0][0])
                game.game(pygame, font, screen, screen_rect, userName, savedGames[0][0], savedGames[0])
                return True
            if delCrosses[0].collidepoint((mx, my)):
                print("First save deleted with id ", savedGames[0][0])
                saves_manager.deleteSavedGame(userName, savedGames[0][0])
                savedGames = saves_manager.getUserUnfinishedGames(userName)
                click = False
        if len(savedGames) > 1 and click:
            if buttons[1].collidepoint((mx, my)):
                print("Second save resumed with id ", savedGames[1][0])
                game.game(pygame, font, screen, screen_rect, userName, savedGames[1][0], savedGames[1])
                return True
            if delCrosses[1].collidepoint((mx, my)):
                print("First save deleted with id ", savedGames[1][0])
                saves_manager.deleteSavedGame(userName, savedGames[1][0])
                savedGames = saves_manager.getUserUnfinishedGames(userName)
                click = False
        if len(savedGames) > 2 and click:
            if buttons[2].collidepoint((mx, my)):
                print("Third save resumed with id ", savedGames[2][0])
                game.game(pygame, font, screen, screen_rect, userName, savedGames[2][0], savedGames[2])
                return True
            if delCrosses[2].collidepoint((mx, my)):
                print("First save deleted with id ", savedGames[2][0])
                saves_manager.deleteSavedGame(userName, savedGames[2][0])
                savedGames = saves_manager.getUserUnfinishedGames(userName)
                click = False

        pygame.display.flip()  # Refresh screen