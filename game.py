import pygame
import ctypes

REF_W, REF_H = 1920, 1080

from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Mon Jeu")
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.user32.ShowWindow(hwnd, 3)

        self.clock = pygame.time.Clock()
        self.running = True

    def get_scale(self):
        w, h = self.screen.get_size()
        return w / REF_W, h / REF_H

    def scale(self, x, y, w, h):
        sx, sy = self.get_scale()
        return int(x * sx), int(y * sy), int(w * sx), int(h * sy)