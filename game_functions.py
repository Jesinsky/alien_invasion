import sys

import pygame

def check_evenets():
    """Respond to to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()