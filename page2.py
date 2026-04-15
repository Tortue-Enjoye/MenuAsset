import pygame

from utils import *

REF_W, REF_H = 1536, 864

class Page2:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

        self.font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 64)
        self.font_small = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 32)
        self.font_hover = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 42)

        self.back_rect = pygame.Rect(0, 0, 0, 0)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        return "menu"

            self.draw()
            self.clock.tick(60)

    def draw(self):
        self.screen.fill((4, 82, 148))
        mouse_pos = pygame.mouse.get_pos()

        screen_size = self.screen.get_size()

        # Titre
        title = self.font.render("Page 2", True, (255,255,255))
        self.font = get_font(64, "assets/fonts/JetBrainsMono-Bold.ttf",title,screen_size)
        center = scale_pos(title, REF_W // 2-100, 100, screen_size)
        self.screen.blit(title,(center[0],center[1]))


        self.font_small = get_font(32, "assets/fonts/JetBrainsMono-Bold.ttf",title,screen_size)
        self.font_hover = get_font(42, "assets/fonts/JetBrainsMono-Bold.ttf",title,screen_size)

        # Bouton retour
        if self.back_rect.collidepoint(mouse_pos):
            back_text = self.font_hover.render("← Retour", True, (0, 0, 0))
        else:
            back_text = self.font_small.render("← Retour", True, (255,255,255))


        center = scale_pos(back_text,REF_W//2, 800,screen_size)
        self.back_rect = back_text.get_rect(center=(center[0], center[1]))
        self.screen.blit(back_text, self.back_rect)

        pygame.display.flip()
