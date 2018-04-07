import os
from random import randint
from CC3501Utils import *
from texturas_opengl import *
from texto import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

class Animal(Figura):
    def __init__(self,vel,pos=Vector(0,0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)
        self.vel=vel

    def figura(self):

        #torso
        glBegin(GL_QUADS)
        glColor3f(255.0/255,140.0/255,178.0/255)#rosa
        glVertex2f(18,0)
        glVertex2f(-18, 0)
        glVertex2f(-18, -45)
        glVertex2f(18, -45)
        glEnd()

        #brazo izq
        glBegin(GL_QUADS)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255) #marron
        glVertex2f(-18, -20)
        glVertex2f(-38, -20)
        glVertex2f(-38, -28)
        glVertex2f(-18, -28)
        glEnd()

        #brazo der
        glBegin(GL_QUADS)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(18, -20)
        glVertex2f(18, -28)
        glVertex2f(38, -28)
        glVertex2f(38, -20)
        glEnd()

        #pierna izq
        glBegin(GL_QUADS)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(-6, -45)
        glVertex2f(-18, -45)
        glVertex2f(-18, -60)
        glVertex2f(-6, -60)
        glEnd()

        #pierna der
        glBegin(GL_QUADS)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(6, -45)
        glVertex2f(6, -60)
        glVertex2f(18, -60)
        glVertex2f(18, -45)
        glEnd()

        #oreja izq
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  #marron
        glVertex2f(-25.0, 15.0)
        radio = 10
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio - 25, sin(ang_i) * radio + 15)
        glEnd()

        # oreja der
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(25.0, 15.0)
        radio = 10
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio + 25, sin(ang_i) * radio + 15)
        glEnd()

        # cabeza
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(0.0, 0.0)
        radio = 40
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(3 / 4 * cos(ang_i) * radio, 1 / 2 * sin(ang_i) * radio)
        glEnd()

        #nariz
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255.0/255,140.0/255,178.0/255)#rosa
        glVertex2f(0.0, -5)
        radio = 20
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(3 / 4 * cos(ang_i) * radio, 2 / 5 * sin(ang_i) * radio - 5)
        glEnd()

        #orificio nariz izq
        glBegin(GL_QUADS)
        glColor3f(0,0,0)#negro
        glVertex2f(-2, -1)
        glVertex2f(-6, -1)
        glVertex2f(-6, -10)
        glVertex2f(-2, -10)
        glEnd()

        # orificio nariz der
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)  # negro
        glVertex2f(2, -1)
        glVertex2f(2, -10)
        glVertex2f(6, -10)
        glVertex2f(6, -1)
        glEnd()

        # ojo izq
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 0)  # negro
        glVertex2f(-15.0, 6.0)
        radio = 5
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio - 15, sin(ang_i) * radio + 6)
        glEnd()

        #ojo der
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0,0,0)  # negro
        glVertex2f(15.0,6.0)
        radio = 5
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio + 15 ,sin(ang_i) * radio + 6)
        glEnd()

    def mover_en_y(self, dt):
        # modificamos la velocidad con la aceleracion de gravedad
        self.vel.y = self.vel.y + dt*g.y

        # modificamos la posicion con la velocidad en y
        self.pos.y = self.pos.y + self.vel.y*dt

    def mover_en_x(self,dt):
        # modificamos la velocidad con la aceleracion en x
        self.vel.x = self.vel.x + dt*aceleracionX.x

        # modificamos la posicion con la velocidad en x
        self.pos.x = self.pos.x + self.vel.x*dt

class Muro(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        ####Muro izquierdo####
        #rectangulo base
        glBegin(GL_QUADS)
        glColor3f(34/256.0, 124/256.0, 214/256.0)  # azul claro
        glVertex2f(0,0)
        glVertex2f(150, 0)
        glVertex2f(150, 600)
        glVertex2f(0, 600)
        glEnd()
        ##Lineas pintadas muro izquierdo
        #Linea 1
        glBegin(GL_TRIANGLES)
        glColor3f(38/256.0, 64/256.0, 94/256.0)  #azul oscuro
        glVertex2f(0, 0)
        glVertex2f(60, 0)
        glVertex2f(0, 60)
        glEnd()
        #Linea 2
        glBegin(GL_POLYGON)
        glColor3f(38/256.0, 64/256.0, 94/256.0)  #azul oscuro
        glVertex2f(0, 180)
        glVertex2f(0, 120)
        glVertex2f(120, 0)
        glVertex2f(150,0)
        glVertex2f(150, 30)
        glEnd()
        #Linea 3
        glBegin(GL_QUADS)
        glColor3f(38/256.0, 64/256.0, 94/256.0)  #azul oscuro
        glVertex2f(0, 300)
        glVertex2f(0, 240)
        glVertex2f(150, 90)
        glVertex2f(150, 150)
        #Linea 4
        glVertex2f(0, 420)
        glVertex2f(0, 360)
        glVertex2f(150, 210)
        glVertex2f(150, 270)
        #Linea 5
        glVertex2f(0,540)
        glVertex2f(0, 480)
        glVertex2f(150, 330)
        glVertex2f(150, 390)

        #Linea 6
        glVertex2f(0, 600)
        glVertex2f(150,450)
        glVertex2f(150, 510)
        glVertex2f(60, 600)
        glEnd()
        #Linea 7
        glBegin(GL_TRIANGLES)
        glColor3f(38/256.0, 64/256.0, 94/256.0)  #azul oscuro
        glVertex2f(120,600)
        glVertex2f(150, 570)
        glVertex2f(150, 600)
        glEnd()

        ###Muro dererecho###
        #rectangulo base
        glBegin(GL_QUADS)
        glColor3f(214/256.0, 121/256.0, 34/256.0)  # naranjo
        glVertex2f(800, 0)
        glVertex2f(800, 600)
        glVertex2f(650, 600)
        glVertex2f(650, 0)
        glEnd()
        ##Lineas pintadas muro derecho
        # Linea 1
        glBegin(GL_TRIANGLES)
        glColor3f(252/256.0,185/256.0,98/256.0)  # amarillo
        glVertex2f(800, 60)
        glVertex2f(740, 0)
        glVertex2f(800, 0)
        glEnd()
        # Linea 2
        glBegin(GL_POLYGON)
        glColor3f(252/256.0,185/256.0,98/256.0)  # amarillo
        glVertex2f(800, 180)
        glVertex2f(650, 30)
        glVertex2f(650, 0)
        glVertex2f(680, 0)
        glVertex2f(800, 120)
        glEnd()
        # Linea 3
        glBegin(GL_QUADS)
        glColor3f(252/256.0,185/256.0,98/256.0)  # amarillo
        glVertex2f(800, 300)
        glVertex2f(650, 150)
        glVertex2f(650, 90)
        glVertex2f(800, 240)
        # Linea 4
        glVertex2f(800, 420)
        glVertex2f(650, 270)
        glVertex2f(650, 210)
        glVertex2f(800, 360)
        # Linea 5
        glVertex2f(800, 540)
        glVertex2f(650, 390)
        glVertex2f(650, 330)
        glVertex2f(800, 480)
        # Linea 6
        glVertex2f(800, 600)
        glVertex2f(740, 600)
        glVertex2f(650, 510)
        glVertex2f(650, 450)
        glEnd()
        # Linea 7
        glBegin(GL_TRIANGLES)
        glColor3f(252/256.0,185/256.0,98/256.0)  # amarillo
        glVertex2f(680, 600)
        glVertex2f(650, 600)
        glVertex2f(650, 570)
        glEnd()

class Piso(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        # piso
        glBegin(GL_QUADS)
        glColor3f(244/256.0, 66/256.0, 104/256.0) #rojo
        glVertex2f(150, 0)
        glVertex2f(150, -40)
        glVertex2f(650, -40)
        glVertex2f(650, 0)
        glEnd()

class Piano(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        #Rectangulo
        glBegin(GL_QUADS)
        glColor3f(1,1,1)
        glVertex2f(-70, 0)
        glVertex2f(-70,-20)
        glVertex2f(70, -20)
        glVertex2f(70, 0)
        glEnd()
        #Lineas entre las teclas blancas del piano
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)
        glVertex2f(-50, 0)
        glVertex2f(-50, -20)
        glVertex2f(-30, 0)
        glVertex2f(-30, -20)
        glVertex2f(-10, 0)
        glVertex2f(-10, -20)
        glVertex2f(10, 0)
        glVertex2f(10, -20)
        glVertex2f(30, 0)
        glVertex2f(30, -20)
        glVertex2f(50, 0)
        glVertex2f(50, -20)
        glEnd()
        #Teclas negras
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        ##Tecla 1
        glVertex2f(-55, 0)
        glVertex2f(-55, -12)
        glVertex2f(-45, -12)
        glVertex2f(-45, -0)
        ##Tecla2
        glVertex2f(-35, 0)
        glVertex2f(-35, -12)
        glVertex2f(-25, -12)
        glVertex2f(-25, -0)
        ##Tecla3
        glVertex2f(5, 0)
        glVertex2f(5, -12)
        glVertex2f(15, -12)
        glVertex2f(15, -0)
        ##Tecla4
        glVertex2f(25, 0)
        glVertex2f(25, -12)
        glVertex2f(35, -12)
        glVertex2f(35, -0)
        ##Tecla5
        glVertex2f(45, 0)
        glVertex2f(45, -12)
        glVertex2f(55, -12)
        glVertex2f(55, -0)
        glEnd()

class Flauta(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        # Cuerpo de la flauta (Rectangulo)
        glBegin(GL_QUADS)
        glColor3f(252/256.0, 239/256.0, 127/256.0) #Color amarillento
        glVertex2f(-70, 0)
        glVertex2f(-70, -20)
        glVertex2f(70, -20)
        glVertex2f(70, 0)
        #Base de la flauta
        glVertex2f(-70, 3)
        glVertex2f(-70, -23)
        glVertex2f(-50, -23)
        glVertex2f(-50, 3)
        #Caja de resonancia
        glVertex2f(30, 3)
        glVertex2f(30, -23)
        glVertex2f(50, -23)
        glVertex2f(50, 3)
        glEnd()
        #Orificios flauta(4 orificios)
        ##Orificio 1
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(-40, -10.0)
        radio = 4
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio - 40, sin(ang_i) * radio -10)
        glEnd()
        ##Orificio 2
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(-20, -10.0)
        radio = 4
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio - 20, sin(ang_i) * radio - 10)
        glEnd()
        ##Orificio 3
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(0, -10.0)
        radio = 4
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio, sin(ang_i) * radio - 10)
        glEnd()
        ##Orificio 4
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(178.0 / 255, 107.0 / 255, 1.0 / 255)  # marron
        glVertex2f(20, -10.0)
        radio = 4
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio + 20, sin(ang_i) * radio - 10)
        glEnd()

class Baqueta(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        # Cuerpo de la baqueta (Rectangulo)
        glBegin(GL_QUADS)
        glColor3f(242 / 256.0, 254 / 256.0, 127 / 181.0)  # Color crema
        glVertex2f(-70, 0)
        glVertex2f(-70, -20)
        glVertex2f(70, -20)
        glVertex2f(70, 0)
        #Base baqueta (color gris)
        glColor3f(226/256.0, 216/256.0, 118/256.0)  # Color cream oscuro
        glVertex2f(-70, 0)
        glVertex2f(-70, -20)
        glVertex2f(-40, -20)
        glVertex2f(-40, 0)
        glEnd()
        #punta baqueta
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(242 / 256.0, 254 / 256.0, 127 / 181.0)  # Color crema
        glVertex2f(60, -10.0)
        radio = 13
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio +60, sin(ang_i) * radio - 10)
        glEnd()
        #linea
        glBegin(GL_LINES)
        glColor3f(226/256.0, 216/256.0, 118/256.0) # Color crema oscuro
        glVertex2f(47,0)
        glVertex2f(47,-20)
        glEnd()

class Reloj(Figura):
    def __init__(self,pos=Vector(0.0,0.0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(18/256.0, 40/256.0, 76/256.0)  # azul
        glVertex2f(0, 0)
        radio = 60
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio , sin(ang_i) * radio )
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1,1,1)  # marron
        glVertex2f(0, 0)
        radio = 50
        ang = 2 * pi / 40
        for i in range(41):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio, sin(ang_i) * radio)
        glEnd()

class Manecilla(Figura):
    def __init__(self,pos=Vector(0,0),rgb = (1.0,1.0,1.0)):
        super().__init__(pos,rgb)

    def figura(self,vel=pi/2.0):
        self.vel=vel
        glLineWidth(8) #Ancho manecilla 8 pixeles
        glBegin(GL_LINES)
        glColor3f(0,0,0)  # Color crema
        glVertex2f(0,0)
        glVertex2f(cos(self.vel)*40.0,sin(self.vel)*40.0)
        glEnd()
        glLineWidth(1)#Volver a ancho originial para no  afectar a otras figuras

def chocar_muros():
    if jugador.pos.x > 650-38:
        jugador.vel.x = -20  # rebotar
        jugador.pos.x = 650-38 # quedarse dentro de la pantalla

    if jugador.pos.x < 150+38:
        jugador.vel.x = 20
        jugador.pos.x = 150+38

    if jugador.pos.y < piso.pos.y+60:
        jugador.vel.y = 0
        jugador.pos.y = piso.pos.y+60

def chocar_plataformas(plataforma):
        return((plataforma.pos.y+7 >=jugador.pos.y-60>=plataforma.pos.y-20) and (plataforma.pos.x-70-18<jugador.pos.x<plataforma.pos.x+70+18))

def sobre_mitad():
    return(jugador.pos.y >= (alto/2 + 60))

def generar_plataformas():
    for i in range(100):
        plataforma = randint(1, 3)  # Seleccion un numero al azar del 1 al 3; 1=piano,2=faluta,3=baqueta
        if(plataforma==1):
            p = Piano(Vector(randint(250,550),(i+1)*70+40))
        elif(plataforma==2):
            p = Flauta(Vector(randint(250, 550), (i + 1) * 70 + 40))
        elif(plataforma==3):
            p = Baqueta(Vector(randint(250, 550), (i + 1) * 70  + 40))

        plataformas.append(p) #agregar a mi lista de plataforma

def mover_manecilla(tiempo):
    return int(round(tiempo/1000))

def accion(dt):
    global bajarPlataformas,relojIniciado,inicioReloj,velPlataforma
    estaChocando=False

    ##Dibujar figuras
    dibujarRectangulo(400, 400, 400, 300, 0, fondo)
    for fig in plataformas:
        fig.dibujar()
    muro.dibujar()
    piso.dibujar()
    reloj.dibujar()
    #######

    #Ciclo que verifica los choques del jugador con la plataforma, si se llega
    #al segundo peldaño se comienzan a bajar las plataformas
    for i in range(0,100):
        if(chocar_plataformas(plataformas[i])):
            jugador.pos.y=plataformas[i].pos.y+60
            jugador.vel.y=0
            estaChocando=True
            if(estaChocando and i==1):
                 bajarPlataformas=True
            if(bajarPlataformas):
                jugador.pos.y-=2
                piso.pos.y-=1


    #Funcionamiento del reloj, comienza cuando las plataformas empiezan a bajar
    if(bajarPlataformas):
        if (relojIniciado == False):
            inicioReloj = pygame.time.get_ticks()
            relojIniciado = True
        tiempo = pygame.time.get_ticks() - inicioReloj
        segundo = mover_manecilla(tiempo)

        #La cuenta regresiva es de 15, cada 15 segundos la plataforma baja mas rapido
        if (tiempo / 1000 >= 15):
            inicioReloj = pygame.time.get_ticks()
            velPlataforma+=1
        #Imprimir texto de un digito
        if(segundo<=9):
            draw_text(710, 465, str(segundo))
        #Imprimir texto de dos digitos
        else:
            draw_text(692, 465, str(segundo))

    #Si esta saltando que desactive el estaChocando para que se pueda mover en el eje y
    if(estaSaltando):
        estaChocando=False
    #Si el jugador no esta chocando con alguna plataforma o el piso que se mueva en el eje y
    if not(estaChocando):
        jugador.mover_en_y(dt / 60.0)
    #Si el jugador se encuentra sobre la mitad de la pantalla, baja la camara para que no choque con la parte superior
    if(sobre_mitad()):
        jugador.pos.y-=3
        for i in range(100):
            plataformas[i].pos.y -= 3
    #Mueve al jugador en el eje x
    jugador.mover_en_x(dt / 60.0)
    #Funcion que detiene movimiento cuando choca con muros
    chocar_muros()
    #Comienza a bajar las plataformas cuando esta en el sgdo peldaño
    if (bajarPlataformas):
        for i in range(100):
            plataformas[i].pos.y -= velPlataforma
    #Dibuja al jugador
    jugador.dibujar()

def main():
    global g,aceleracionX,alto,ancho,vel,plataformas,estaChocando,estaSaltando,bajarPlataformas,piso,jugador,muro,reloj,manecilla,inicioReloj,relojIniciado,ang
    global velPlataforma,fondo
    ancho = 800
    alto = 600
    init(ancho,alto,"Music Tower")
    #sprite para el fondo
    fondo = generarTex("fondo.jpg", True)
    #musica
    pygame.mixer.music.load('preludio.mp3')
    pygame.mixer.music.play(0)


    #Definir y generar plataformas
    plataformas = []
    generar_plataformas()

    #Variables que indican el estado de un parametro
    bajarPlataformas=False
    estaSaltando = False
    relojIniciado = False

    #Definir figuras
    jugador=Animal(Vector(0,0),Vector(400,100))
    muro=Muro(Vector(0,0))
    piso=Piso(Vector(0,40))
    reloj=Reloj(Vector(725,500))

    #Vectores de las aceleraciones de gravedad y eje x
    g = Vector(0.0, -9.8)
    aceleracionX =  Vector(0,0)
    velPlataforma = 2
    #angulo manecilla



    t0 = pygame.time.get_ticks()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT: # cerrar ventanas
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    estaSaltando=True
                    jugador.vel.y=38
                    jugador.pos.y+=8

        ###Controles de las teclas izquierda y derecha
        pulsada = pygame.key.get_pressed()

        if pulsada[K_RIGHT]:
            aceleracionX=Vector(3,0)
        elif pulsada[K_LEFT]:
            aceleracionX = Vector(-3,0)
        elif ((pulsada[K_RIGHT] and pulsada[K_LEFT])==False):
            aceleracionX=Vector(0,0)
            jugador.vel.x=0


        # limpia la pantalla para volver a dibujar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        t1 = pygame.time.get_ticks()

        accion(t1 - t0)
        estaSaltando = False

        if (jugador.pos.y <= 60):
            run = False

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

        t0=t1
    pygame.quit()


main()
