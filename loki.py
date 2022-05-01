import pygame

from pygame.sprite import Sprite

class loki(Sprite):
    
    def __init__(self,instance_game):
        
        super().__init__()
        self.screen = instance_game.screen
        self.setting = instance_game.setting
        
        self.image = pygame.image.load(self.setting.loki_image)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height + 25
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.x += self.setting.loki_speed * self.setting.fleet_direction_loki
        self.rect.x = self.x