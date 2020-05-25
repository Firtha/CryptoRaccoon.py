import sys

from pygame.constants import *
import game
import utils
import data_collector
import saves_manager



# Stats_listing : Create the best scores list window
def stats_listing(pygame, font, screen, screen_rect, userName):
    print("Stats list incoming")
    color = (255, 255, 255)
    active = False
    done = False

    savedGames = saves_manager.getBestScores()

### init every needed icons for the stats windows 
    cup = pygame.image.load("../img/medals/prize.png").convert_alpha()
    cup_s = pygame.transform.scale(cup, (100, 100))

    #winner trophy
    trophy_first = pygame.image.load("../img/medals/trophy_1.png").convert_alpha()
    trophy_first_s = pygame.transform.scale(trophy_first, (60, 60))
    
    #second trophy
    trophy_second = pygame.image.load("../img/medals/trophy_2.png").convert_alpha()
    trophy_second_s = pygame.transform.scale(trophy_second, (60, 60))
    
    #third trophy
    trophy_third = pygame.image.load("../img/medals/trophy_3.png").convert_alpha()
    trophy_third_s = pygame.transform.scale(trophy_third, (60, 60))

    #medal trophy
    medal = pygame.image.load("../img/medals/medal.png").convert_alpha()
    medal_s = pygame.transform.scale(medal, (60, 60))
### end

    ### list of position on the screen
    list_line_pos = [290, 380, 470, 560, 650]
 
    while not done:
        mx, my = pygame.mouse.get_pos() 
        utils.init_game_background(pygame, screen)              # Start the init_game_background function
        utils.draw_text('Score', font, (255, 255, 255), screen, 215, 200, False)                  # Draw the text menu
        utils.draw_text('board', font, (255, 255, 255), screen, 480, 200, False)                  # Draw the text menu

        top_rectangle = 290
        top_text_pos = 310

        #draw the medals cards
        for i in list_line_pos:
            pygame.draw.rect(screen, color, pygame.Rect(63, i, 80, 80), 1)
            top_rectangle += 90
        
        # draw the user_name cards
        for i in list_line_pos:
            pygame.draw.rect(screen, color, pygame.Rect(145, i, 400, 80), 1)
            top_rectangle += 90

        # draw the user_score cards
        for i in list_line_pos:
            pygame.draw.rect(screen, color, pygame.Rect(545, i, 250, 80), 1)
            top_rectangle += 90

        screen.blit(cup_s, (369, 140))        
        screen.blit(trophy_first_s, (73, 300))
        screen.blit(trophy_second_s, (73, 390))
        screen.blit(trophy_third_s, (73, 480))
        screen.blit(medal_s, (73, 570))
        screen.blit(medal_s, (73, 660))


        # Max 5 lines displayed
        currIndex = 0
        for savedGame in savedGames:
            if currIndex < 5:
                utils.draw_text(savedGame[0], font, (255, 255, 255), screen, 155, top_text_pos, False)
                utils.draw_text(savedGame[1], font, (255, 255, 255), screen, 555, top_text_pos, False)
                top_text_pos += 90
            currIndex += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print("enter")
                if event.key == K_ESCAPE:
                    print("Escape has been pushed")
                    done = True

        pygame.display.flip()
