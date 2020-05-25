import sys

from pygame.constants import *
import game
import utils
import menu_stats
import menu_authenticate
import data_collector
import saves_manager
import menu_saves

# Main_menu : create the menu window
def main_menu(pygame, font, screen, screen_rect, userName):
    savesCount = saves_manager.countUserUnfinishedGames(userName)
    startDisplayed = True
    savedDisplayed = True

    click = False
    running = True
    while running:
        if savesCount >= 3:
            startDisplayed = False
        else:
            startDisplayed = True

        if savesCount == 0:
            savedDisplayed = False
        else:
            savedDisplayed = True

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

        if startDisplayed:
            utils.draw_text('START', font, (0, 0, 0), screen, 300, 227, True)
        else:
            utils.draw_text('CONTINUE', font, (0, 0, 0), screen, 300, 227, True)

        utils.draw_text('STATS', font, (0, 0, 0), screen, 300, 427, True)

        if savedDisplayed:
            button_3 = pygame.Rect(250, 600, 400, 100)
            button_3.centerx = screen_rect.centerx
            pygame.draw.rect(screen, (255, 255, 255), button_3)
            utils.draw_text(str(savesCount) + ' SAVED GAMES', font, (0, 0, 0), screen, 300, 627, True)

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
                if startDisplayed:
                    game.game(pygame, font, screen, screen_rect, userName, -1, [])
                    savesCount = saves_manager.countUserUnfinishedGames(userName)
                else:
                    gameSaved = saves_manager.getLastSave(userName)
                    game.game(pygame, font, screen, screen_rect, userName, gameSaved[0], gameSaved)
        if button_2.collidepoint((mx, my)):
            if click:
                click = False
                print("Stats button clicked")
                menu_stats.stats_listing(pygame, font, screen, screen_rect, userName)
        if savedDisplayed:
            if button_3.collidepoint((mx, my)):
                if click:
                    click = False
                    print("Saved Games button clicked")
                    menu_saves.saves_listing(pygame, font, screen, screen_rect, userName)
                    savesCount = saves_manager.countUserUnfinishedGames(userName)

        pygame.display.flip()  # Refresh screen

