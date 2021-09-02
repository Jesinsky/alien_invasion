class Settings():
    """A class to store all settings for Alien Invasion Game."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (94, 94, 94)
        
        # Ship Settings
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (85, 197, 219)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed_factor = .75