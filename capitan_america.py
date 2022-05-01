import pygame
from pygame.sprite import Sprite

class captian_america(Sprite):
    def __init__(self,instance_game):
        
        super().__init__()
        
        self.setting = instance_game.setting
        self.game_screen = instance_game.screen
        self.game_screen_rect = instance_game.screen.get_rect()
        self.game = instance_game
        
        self.image = pygame.image.load(self.setting.captain_image)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = self.game_screen_rect.centerx
        self.rect.bottom = self.game_screen_rect.bottom - 25
        
        self.moving_right = False
        self.moving_left = False
        
        self.x =float(self.rect.x) 
        
        
        
        
    def update(self):
        if self.moving_right and self.rect.right<self.game_screen_rect.right + 30 :
            self.x += self.setting.capitan_speed
            
        if self.moving_left and self.rect.left > -20:
            self.x -= self.setting.capitan_speed
            
        self.rect.x = self.x
        
        
        
        
        
       
        
    def draw_captain(self):
        self.game_screen.blit(self.image,self.rect)
        
    def reset_captain(self):
        self.rect.centerx = self.game_screen_rect.centerx
        self.rect.bottom = self.game_screen_rect.bottom - 25
        self.x =float(self.rect.x) 