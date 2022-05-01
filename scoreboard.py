import pygame.font
from pygame.sprite import Group
from capitan_america import *

class score_board:
    
    def __init__(self,instance_game):
        self.screen = instance_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.game = instance_game
        
        self.stats = instance_game.stats
        self.setting = instance_game.setting
        
        self.text_color = (255,255,255)
        
        all_fonts = pygame.font.get_fonts()
        
        self.font = pygame.font.SysFont(all_fonts[0] , 45)
        self.font1 = pygame.font.SysFont(all_fonts[0], 15)
        self.captain = instance_game.a_captain
        
        self.render_score()
        self.render_best()
        self.render_level()
        self.render_captain()
        self.render_creator()
        
    def render_score(self):
        score_str = "score : " + str(self.stats.score)
        self.score_image = self.font.render(score_str,True, self.text_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 10
        
    def render_best(self):
        best_str = "high score : " + str(self.stats.best)
        self.best_image = self.font.render(best_str, True, self.text_color)

        self.best_rect = self.best_image.get_rect()
        self.best_rect.midbottom = self.screen_rect.midbottom
        
        
    def render_level(self):
        level_str = "level : " + str(self.stats.level)
        self.level_image = self.font.render(level_str,True, self.text_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 5
        
    def render_creator(self):
        creator = self.setting.creator_name
        self.creator_image = self.font1.render(creator,True, self.text_color)
        
        self.creator_rect = self.creator_image.get_rect()
        self.creator_rect.left = self.screen_rect.left
        self.creator_rect.bottom = 600
        
    
    def render_captain(self):
        self.captains = Group()
        for captain_number in range(self.stats.captain_left):
            ocaptain = captian_america(self.game)
            ocaptain.rect.x = ocaptain.rect.width * captain_number
            ocaptain.rect.y = 0
            
            self.captains.add(ocaptain)
            
    
            
    
        
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.best_image, self.best_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.captains.draw(self.screen)
        self.screen.blit(self.creator_image, self.creator_rect)
    def check_best(self):
        if self.stats.score > self.stats.best:
            self.stats.best = self.stats.score
            self.render_best()
        
        
        