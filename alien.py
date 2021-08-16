import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien imafge and set its rect attribute.
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact postition.
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)