import pygame

class setting:
    """a class to store all setting in my game"""
    
    def __init__(self):
        
        self.width = 800
        self.height = 600
        self.bg = pygame.image.load("img/background.jpg")
       
        self.game_speed_scale = 1.1
        self.score_scale = 10
        
        self.player_name = "rafiea"
        self.creator_name = "@ra.phi"
        
        
        #thor setting
        
        
        #shield settings
        
        self.shield_allowed = 100
        
        #images
        self.captain_image ="img/captain_america.png"
        self.thor_image = "img/thor.png"
        self.shield_image = "img/shield.png"
        self.loki_image = "img/loki.png"
        self.thanos_image = "img/thanos.png"
        self.hammer_image = "img/hammer.png"
        
        #enemies settings
        
        
        
        #1 is right -1 is left
        
        self.fleet_direction_thor = 1
        self.fleet_direction_loki = 1
        self.fleet_direction_thanos = 1
        
        
        #time
        
        
        
        #hammer
        
        
        #captain
        
        self.captain_allowed = 3
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        self.capitan_speed = 1.5
        self.shield_speed = 1.0
        self.thor_speed = 1
        self.loki_speed = 0.5
        self.thanos_speed = 0.75
        self.hammer_speed = 1.0
        self.thor_score = 50
        self.loki_score = 30
        self.thanos_score = 20
        self.thor_cooldown = 1000
        
            
            
    def speed_up(self):
        self.capitan_speed *= self.game_speed_scale
        self.shield_speed *= self.game_speed_scale
        self.thor_speed *= self.game_speed_scale
        self.loki_speed *= self.game_speed_scale
        self.thanos_speed *= self.game_speed_scale
        self.hammer_speed *= self.game_speed_scale
        self.thor_score += self.score_scale
        self.loki_score  += self.score_scale
        self.thanos_score += self.score_scale
        self.thor_cooldown -= 50