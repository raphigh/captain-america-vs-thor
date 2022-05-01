import pygame

from pygame.sprite import Sprite

class thor(Sprite):
    
    def __init__(self,instance_game):
        
        super().__init__()
        self.screen = instance_game.screen
        self.setting = instance_game.setting
        
        self.image = pygame.image.load(self.setting.thor_image)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height + 25
        
        self.x = float(self.rect.x)
        
        
        
    def update(self):
        self.x += self.setting.thor_speed * self.setting.fleet_direction_thor
        self.rect.x = self.x