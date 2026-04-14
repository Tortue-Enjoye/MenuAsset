import sys
import os
import pygame

REF_W, REF_H = 1536, 864


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Permet d'obtenir les ratios de taille du screen
def get_scale(buton_text,screen_size):
    w, h = screen_size
    return w / REF_W, h / REF_H

# Retourne les valeurs pour placer et resize des éléments
def scale_all(buton_text, x, y, w, h,screen_size):
    sx, sy = get_scale(buton_text,screen_size)
    return int(x * sx), int(y * sy), int(w * sx), int(h * sy)

# Idem mais pour les positions seulement
def scale_pos(buton_text, x, y,screen_size):
    w, h = get_scale(buton_text,screen_size)
    return int(x * w), int(y * h)

def get_font(size,path,buton_text,screen_size):
    # On récupère le scale
    _, sy = get_scale(buton_text,screen_size)
    # On applique le ratio à la taille de base demandée
    return pygame.font.Font(resource_path(path), int(size * sy))