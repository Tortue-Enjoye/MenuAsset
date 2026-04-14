import pygame
import ctypes

REF_W, REF_H = 1536, 864


class Game:
    def __init__(self):
        # Initialisation
        pygame.init()
        print(pygame.display.Info())
        pygame.display.set_caption("Mon Jeu")
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

        # Resize à la bonne taille

        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.user32.ShowWindow(hwnd, 3)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()

        pygame.quit()

    def update(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    # Permet d'obtenir les ratios de taille du screen
    def get_scale(self):
        w, h = self.screen.get_size()
        return w / REF_W, h / REF_H

    # Retourne les valeurs pour placer / resize des éléments
    def scale(self, x, y, w, h):
        sx, sy = self.get_scale()
        return int(x * sx), int(y * sy), int(w * sx), int(h * sy)