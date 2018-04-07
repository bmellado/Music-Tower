from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame


def draw_text(x, y, text, color=(0, 0, 0, 0), fondo=(255,255,255, 0), tamaño=90):
    position = (x, y)
    font = pygame.font.Font(None, tamaño)
    text_surface = font.render(text, True, color, fondo)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos2d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
