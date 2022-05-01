import pygame
from pygame.sprite import Sprite



class shield(Sprite):
    
    def __init__(self,instance_game):
        
        super().__init__()
        
        self.screen = instance_game.screen
        self.setting = instance_game.setting
        self.image = pygame.image.load(self.setting.shield_image)
        
        self.rect = self.image.get_rect()
        self.rect.midtop = instance_game.a_captain.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.setting.shield_speed
        
        self.rect.y = self.y
        
    def draw_shield(self):
        self.screen.blit(self.image, self.rect)
        
        
    