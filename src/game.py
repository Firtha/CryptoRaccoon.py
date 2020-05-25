import sys
import pygame
import utils
import saves_manager

from truck import Truck

# class qui représente le jeu
class Game:
    def __init__(self):
        self.player = Player()
        self.all_trucks = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_truck()
        
    
    def spawn_truck(self):
        truck = Truck()
        self.all_trucks.add(truck)

# class du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 20
        self.image = pygame.image.load("../img/raccoon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 880
        self.max_y = 720
    
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def jump(self):
        self.rect.y -= self.velocity


def game(pygame, font, screen, screen_rect, userName, saveId, gameData):

    game = Game()

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

        for truck in game.all_trucks:
            truck.drive()

        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :
            game.player.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()
        if game.pressed.get(pygame.K_UP) and game.player.rect.y > 500 :
            game.player.jump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_ESCAPE:
                    targetOptions = game_menu(pygame, font, screen, screen_rect, userName)
                    if targetOptions == 1:
                        saves_manager.putSavedGame(userName, userScore, saveId)
                    if targetOptions == 1 or targetOptions == -1:
                        running = False

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                if event.key == pygame.K_UP:
                    game.player.rect.y = 880

        # draw the background
        utils.init_game_background(pygame, screen)

        # draw the player 
        screen.blit(game.player.image, game.player.rect)

        # draw players stats
        utils.draw_text('User : ' + userName, fontScore, (0, 0, 0), screen, 15, 10, False)  # Draw the user name
        utils.draw_text('Score (BTC) :', fontScore, (0, 0, 0), screen, 15, 30, False)  # Draw the score declaration
        utils.draw_text('%.4f' % userScore, fontScore, (0, 0, 0), screen, 30, 45, False)  # Draw the score
        
        #draw trucks
        game.all_trucks.draw(screen)

        userScore += 0.00001
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
