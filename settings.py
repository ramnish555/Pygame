class Settings:
    def __init__(self):
        """Initialize game Settings."""
        #Screen Settings
        self.screen_width = 900
        self.screen_height = 650
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        #alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 7
        # fleet direction of 1 represent right and -1 left.
        self.fleet_direction = 1

        #Level Up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5
        

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
