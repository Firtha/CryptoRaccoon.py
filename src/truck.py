import pygame

class Truck(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 25
        self.image = pygame.image.load('../img/garbage-truck.png')
        self.image = pygame.transform.scale(self.image,(280,280))
        self.rect = self.image.get_rect()
        self.rect.x = 630
        self.rect.y = 750
        self.velocity = 3
    
    def drive(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.rect.x += 250