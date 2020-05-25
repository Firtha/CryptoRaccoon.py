import pygame

class Truck(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.attack = 25
        self.image = pygame.image.load('../img/garbage-truck.png')
        self.image = pygame.transform.scale(self.image,(280,280))
        self.rect = self.image.get_rect()
        self.rect.x = 630
        self.rect.y = 750
        self.velocity = 5
    
    def drive(self):
        self.rect.x -= self.velocity