# Draw text : A function to draw some text on the screen, take multiple parameter
def draw_text(text, font, color, surface, x, y, center):
    textobj = font.render(text, 1, color)  # Create a textobject based on the text received as input
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.topleft = (x, y)  # Define the rectangle x,y position
    if center == True:
        surface_rect = surface.get_rect()  # Get the screen rect x and y data
        textrect.centerx = surface_rect.centerx  # Synchronize the rect x center of the text are to the screen
    surface.blit(textobj, textrect)


# Initialisation du background
def init_game_background(pygame, screen):
    fond = pygame.image.load("img/background.jpg").convert()
    screen.blit(fond, (0, 0))