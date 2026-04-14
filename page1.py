import pygame

from utils import resource_path
class page1:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font_small = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 32)
        self.font_hover = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 42)