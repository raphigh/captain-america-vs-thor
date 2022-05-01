import pygame

import sys

import random

import pygwidgets

from time import sleep

from setting import *


from capitan_america import *
from thor import *
from shield import *
from loki import *
from thanos import *
from thor_hammer import *
from gamestat import *
from button import *
from scoreboard import *




class mygame:
    
    """overall class to manage game assetes and behavior"""
    def __init__(self):
        
        pygame.init()
        self.setting = setting()
        self.screen = pygame.display.set_mode((self.setting.width,self.setting.height))
        self.setting.width = self.screen.get_rect().width
        self.setting.height = self.screen.get_rect().height
        pygame.display.set_caption("capitan_america vs thor")
        self.shield_count = 0
        self.stats = gamestats(self)
        self.a_captain = captian_america(self) 
        #scoreboard
        self.sb = score_board(self)
        
        self.a_captain = captian_america(self) 
        
        self.thor_list = pygame.sprite.Group()
        self._create_thor()
        
        self.hammer_list = pygame.sprite.Group()
        
        self.loki_list = pygame.sprite.Group()
        self._create_loki()
        
        self.thanos_list = pygame.sprite.Group()
        self._create_thanos()
        
        self.shield_list = pygame.sprite.Group()
        
        self.thor_last_shot = pygame.time.get_ticks()
        
        self.btn_play = Button(self, "PLAY")
        
        self.oInputText = pygwidgets.InputText(self.screen, (20, 200), initialFocus=True,
                      textColor=(0, 0, 255),
                      fontSize=28)
        
        self.oDisplayTextTitle = pygwidgets.DisplayText(self.screen, (0, 20), self.setting.player_name,
                                           fontSize=36,
                                           width=640,
                                           textColor=(255,255,255),
                                           justified='center')
        
        
        
        
        
    def draw_bg(self):
        self.screen.blit(self.setting.bg, (0,0))
        
    def _fire_shield(self):
        if self.shield_count <self.setting.shield_allowed:
            new_shield = shield(self)
            self.shield_list.add(new_shield)
            self.shield_count += 1
        
    def _fire_hammer(self):
        new_hammer = hammer(self)
        self.hammer_list.add(new_hammer)
                
        
    def run_game(self):
        while True :
            self._check_events() 
            
            if self.stats.game_active:
            
                time_now = pygame.time.get_ticks()
                
                if time_now - self.thor_last_shot > self.setting.thor_cooldown :
                    try:
                        attacking_thor = random.choice(self.thor_list.sprites())
                    except:
                        pass
                    ohammer = hammer(self,attacking_thor.rect.centerx,attacking_thor.rect.bottom)
                    self.hammer_list.add(ohammer)
                    self.thor_last_shot = time_now
                
                
                
                 
                self.a_captain.update()
                self._update_shield()
                self._update_hammer()
                self._update_thor()
                self._update_loki()
                self._update_thanos()
                self._name_update()
            self._update_screen()
                
            
            
            
    def _check_events(self): 
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.a_captain.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.a_captain.moving_left = True
                if event.key == pygame.K_SPACE:
                    self._fire_shield()
                    
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 
                 if self.btn_play.rect.collidepoint(mouse_pos) and not self.stats.game_active :
                     self.setting.initialize_dynamic_settings()
                     self.stats.game_active = True
                     self.stats.reset_stat()
                     self.sb.render_score()
                     self.sb.render_level()
                     self.sb.render_captain()
                     self.sb.render_creator()
                     self.thor_list.empty()
                     self.loki_list.empty()
                     self.thanos_list.empty()
                     self.shield_list.empty()
                     self.hammer_list.empty()
                     self.shield_count = 0
                     
                     self._create_thor()
                     self._create_loki()
                     self._create_thanos()
                     
                     self.a_captain.reset_captain()
                     print(self.setting.player_name)
                     
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.a_captain.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.a_captain.moving_left = False
                    
            if self.oInputText.handleEvent(event):
                self.setting.player_name = self.oInputText.getValue()
                
                
                    
                    
                    
            
                    
    
    def _create_thor(self):
        othor = thor(self)
        thor_width = othor.rect.width
        available_space_x = self.setting.width - (2*thor_width)
        number_thor_x = available_space_x // (2*thor_width)
        
        for thor_number in range(number_thor_x):
            othor = thor(self)
            othor.x = thor_width + 2* thor_width * thor_number
            othor.rect.x = othor.x
            self.thor_list.add(othor)
            
    def _create_loki(self):
        oloki = loki(self)
        loki_width = oloki.rect.width
        loki_height = oloki.rect.height
        available_space_x = self.setting.width - (2*loki_width)
        number_loki_x = available_space_x // (2*loki_width)
        
        for loki_number in range(number_loki_x):
            oloki = loki(self)
            oloki.x = loki_width + 2* loki_width * loki_number
            oloki.y = 2.5*loki_height
            oloki.rect.x = oloki.x
            oloki.rect.y = oloki.y
            
            self.loki_list.add(oloki)
            
    def _create_thanos(self):
        othanos = thanos(self)
        thanos_width = othanos.rect.width
        thanos_height = othanos.rect.height
        available_space_x = self.setting.width - (2*thanos_width)
        number_thanos_x = available_space_x // (2*thanos_width)
        
        for thanos_number in range(number_thanos_x):
            othanos = thanos(self)
            othanos.x = thanos_width + 2* thanos_width * thanos_number
            othanos.y = 4.5*thanos_height
            othanos.rect.x = othanos.x
            othanos.rect.y = othanos.y
            
            self.thanos_list.add(othanos)
        
    def _update_screen(self): 
        
        self.draw_bg()
        self.a_captain.draw_captain()
        self.sb.show_score()
        self.oDisplayTextTitle.draw()
        for oshield in self.shield_list:
            oshield.draw_shield()
            
        self.hammer_list.draw(self.screen)
        self.thor_list.draw(self.screen)
        self. loki_list.draw(self.screen)
        self.thanos_list.draw(self.screen)
        
        if not self.stats.game_active :
            self.btn_play.draw_button()
            self.oInputText.draw()
            
        pygame.display.update()
        
        
        
        
    def _update_shield(self):
        self.shield_list.update()
        for oshield in self.shield_list.copy():
            if oshield.rect.bottom < 0:
                self.shield_list.remove(oshield)
        
        thor_collisions = pygame.sprite.groupcollide(self.shield_list,self.thor_list,True,True)
        if thor_collisions:
            self.stats.score += self.setting.thor_score
            self.sb.render_score()
            self.sb.check_best()
        loki_collisions = pygame.sprite.groupcollide(self.shield_list,self.loki_list,True,True) 
        if loki_collisions:
            self.stats.score += self.setting.loki_score
            self.sb.render_score()
            self.sb.check_best()
        thanos_collisions = pygame.sprite.groupcollide(self.shield_list,self.thanos_list,True,True)
        if thanos_collisions:
            self.stats.score += self.setting.thanos_score
            self.sb.render_score()
            self.sb.check_best()
            
            
        
        if not self.thanos_list and not self.thor_list and not self.loki_list:
            self.setting.speed_up()
            self._create_thor()
            self._create_loki()
            self._create_thanos() 
            self.shield_count = 0  
            self.stats.level += 1
            self.sb.render_level()
            
    def _update_hammer(self):
        self.hammer_list.update()
        for ohammer in self.hammer_list.copy():
            if ohammer.rect.top > self.setting.height :
                self.hammer_list.remove(ohammer)
        if not self.thor_list:
            self.hammer_list.empty()
            
        if pygame.sprite.spritecollideany(self.a_captain, self.hammer_list):
            #print("captain injured")
            self._captain_hits()
            
            
    def _name_update(self):
        self.oDisplayTextTitle = pygwidgets.DisplayText(self.screen, (0, 25), self.setting.player_name,
                                           fontSize=55,
                                           width=640,
                                           textColor=(255,255,255),
                                           justified= 'center')
            
    def _captain_hits(self):
        
        if self.stats.captain_left > 0:
        
            self.stats.captain_left -= 1
            self.sb.render_captain()
        
            self.a_captain.reset_captain()
        
        
            self.shield_list.empty()
            self.shield_count = 0
            self.thor_list.empty()
            self.thanos_list.empty()
            self.loki_list.empty()
            self.hammer_list.empty()
            
            self._create_thor()
            self._create_loki()
            self._create_thanos()
            
            sleep(0.01)
            
    
        else:
            self.stats.game_active = False
        
        
        
            
            
    def _update_thor(self):
        self._chek_direction_thor()
        self.thor_list.update()
        
           
            
    def _update_loki(self):
        self._chek_direction_loki()
        self.loki_list.update()
        
    def _update_thanos(self):
        self._chek_direction_thanos()
        self.thanos_list.update()
        
    def _chek_direction_thor(self):
        for thor in self.thor_list.sprites():
            if thor.rect.right >= self.screen.get_rect().right or thor.rect.left <= 0 :
                self.setting.fleet_direction_thor *= -1
                
    def _chek_direction_loki(self):
        for loki in self.loki_list.sprites():
            if loki.rect.right >= self.screen.get_rect().right or loki.rect.left <= 0 :
                self.setting.fleet_direction_loki *= -1
                
    def _chek_direction_thanos(self):
        for thanos in self.thanos_list.sprites():
            if thanos.rect.right >= self.screen.get_rect().right or thanos.rect.left <= 0 :
                self.setting.fleet_direction_thanos *= -1
                    
    
    
        
    
if __name__ == "__main__" :
    ogame = mygame()
    ogame.run_game()
            

        
        
        
 