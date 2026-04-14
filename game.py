import pygame
import ctypes

from menu import Menu


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

        self.menu = Menu(self.screen,self.clock)

    def run(self):
        current = "menu"

        while self.running:
            if current == "menu":
                result = self.menu.run()

                if result == False:
                    self.running = False


        pygame.quit()



