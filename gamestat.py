class gamestats:
    def __init__(self,instance_game):
        self.setting = instance_game.setting
        self.game_active = False
        self.reset_stat()
        self.best = 0
        
        
        
        
    def reset_stat(self):
        self.captain_left = self.setting.captain_allowed
        self.score = 0
        self.level = 1
        