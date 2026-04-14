import pygame

from utils import *

REF_W, REF_H = 1536, 864


class Menu:
    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock

        self.font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 72)
        self.font_small = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 48)
        self.font_hover = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 64)

        self.rect_buton1 = pygame.Rect(0,0,0,0)
        self.rect_buton2 = pygame.Rect(0,0,0,0)
        self.rect_buton3 = pygame.Rect(0,0,0,0)


    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():

                # Quitter :
                "X"
                if event.type == pygame.QUIT:
                    return False
                "Quitter"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_buton3.collidepoint(event.pos):
                        return False

            self.draw(mouse_pos)

            self.clock.tick(60)







    def draw(self,mouse_pos):
        self.screen.fill((4, 82, 148))
        screen_size = self.screen.get_size()
        # Bouton 1
        if self.rect_buton1.collidepoint(mouse_pos):
            buton1_text = self.font_hover.render("Bouton 1", True, (0,0,0))
        else:
            buton1_text = self.font_small.render("Bouton 1", True, (255,255,255))

        self.font_hover = get_font(64, "assets/fonts/JetBrainsMono-Bold.ttf",buton1_text,screen_size)
        self.font_small = get_font(48, "assets/fonts/JetBrainsMono-Bold.ttf",buton1_text,screen_size)
        center = scale_pos(buton1_text,REF_W//2,250,screen_size)
        self.rect_buton1 = buton1_text.get_rect(center=(center[0],center[1]))
        self.screen.blit(buton1_text, self.rect_buton1)

        # Bouton 2
        if self.rect_buton2.collidepoint(mouse_pos):
            buton2_text = self.font_hover.render("Bouton 2", True, (0, 0, 0))
        else:
            buton2_text = self.font_small.render("Bouton 2", True, (255, 255, 255))

        self.font_hover = get_font(64, "assets/fonts/JetBrainsMono-Bold.ttf", buton2_text,screen_size)
        self.font_small = get_font(48, "assets/fonts/JetBrainsMono-Bold.ttf", buton2_text,screen_size)
        center = scale_pos(buton2_text,REF_W // 2, 400,screen_size)
        self.rect_buton2 = buton2_text.get_rect(center=(center[0], center[1]))
        self.screen.blit(buton2_text, self.rect_buton2)

        # Bouton 3 (Quitter)
        if self.rect_buton3.collidepoint(mouse_pos):
            buton3_text = self.font_hover.render("Quitter", True, (0, 0, 0))
        else:
            buton3_text = self.font_small.render("Quitter", True, (255, 255, 255))

        self.font_hover = get_font(64, "assets/fonts/JetBrainsMono-Bold.ttf", buton3_text,screen_size)
        self.font_small = get_font(48, "assets/fonts/JetBrainsMono-Bold.ttf", buton3_text,screen_size)
        center = scale_pos(buton3_text,REF_W // 2, 550,screen_size)
        self.rect_buton3 = buton3_text.get_rect(center=(center[0], center[1]))
        self.screen.blit(buton3_text, self.rect_buton3)

        pygame.display.flip()
