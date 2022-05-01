import pygame
from pygame.sprite import Sprite



class hammer(Sprite):
    
    def __init__(self,instance_game,x,y):
        
        super().__init__()
        
        self.screen = instance_game.screen
        self.setting = instance_game.setting
        self.image = pygame.image.load(self.setting.hammer_image)
        
        self.rect = self.image.get_rect()
        self.rect.center =  [x,y]
        self.y = float(self.rect.y)
        
    def update(self):
        self.y += self.setting.hammer_speed
        self.rect.y = self.y
        

        
        
    