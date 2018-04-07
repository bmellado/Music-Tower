# importar librería gráfica
from OpenGL.GL import *
from OpenGL.GLU import *

from PIL import Image

# importar librería para manejar eventos
import pygame
from pygame.locals import *

# METODO PARA CARGAR UNA TEXTURA DESDE UN ARCHIVO
def generarTex(file, repeat):
    # leer el archivo
    image = Image.open(file)
    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)
    # Crear la textura en opengl
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    if repeat:
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    else:
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    return texture



#####################################################################
# Funciones de dibujo
#####################################################################

def dibujarRectangulo(rx, ry, px, py, o, texture):
    # rx,ry : tamaño en ambas direcciones. Si se quiere cubrir toda la pantalla se usa el tamaño de la pantalla.
    # px,py : posición
    # o		: orientación (ángulo en grados)
    glPushMatrix()

    glTranslatef(px, py, 0.0)
    glScalef(rx, ry, 0.0)
    glRotatef(o, 0.0, 0.0, 1.0)

    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_POLYGON)  # setea método de dibujo

    glTexCoord2f(0.0, 0.0)
    glVertex2f(-0.5, -0.5)

    glTexCoord2f(1.0, 0.0)
    glVertex2f(0.5, -0.5)

    glTexCoord2f(1.0, 1.0)
    glVertex2f(0.5, 0.5)

    glTexCoord2f(0.0, 1.0)
    glVertex2f(-0.5, 0.5)

    glEnd()  # fin del método de dibujo

    glDisable(GL_TEXTURE_2D)

    glPopMatrix()


def dibujarTriangulo(rx, ry, px, py, o, texture):
    # rx,ry : tamaño en ambas direcciones.
    # px,py : posición
    # o		: orientación (ángulo en grados)
    glPushMatrix()

    glTranslatef(px, py, 0.0)
    glScalef(rx, ry, 0.0)
    glRotatef(o, 0.0, 0.0, 1.0)

    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D, texture)

    glBegin(GL_TRIANGLES)  # setea método de dibujo

    glTexCoord2f(0.0, 0.0)
    glVertex2f(-0.5, -0.5)

    glTexCoord2f(1.0, 0.0)
    glVertex2f(0.5, -0.5)

    glTexCoord2f(0.5, 1.0)
    glVertex2f(0.0, 0.5)

    glEnd()  # fin del método de dibujo

    glDisable(GL_TEXTURE_2D)

    glPopMatrix()


