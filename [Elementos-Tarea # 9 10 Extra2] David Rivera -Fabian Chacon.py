from pygame.locals import*
import sys
import pygame
import random
import time
ANCHO=800
ALTO=600
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Mata al monstruo')
cantidadcorazones=10
cantbalas=0
puntosganados=0

prueba=[]


pygame.init()



def sumayresta(c1,c2,c3,c4,c5,c6):
    global cantidadcorazones
    global cantbalas
    global puntosganados
    if c1==1:
        cantidadcorazones=cantidadcorazones+1
    if c1==2:
        cantidadcorazones=cantidadcorazones-1
    if c2==1:
        cantbalas=cantbalas+1
    if c3==1:
        cantbalas=cantbalas+2
    if c4==1:
        cantbalas=cantbalas+3
    if c5==1:
        cantbalas=cantbalas-1
    if c6==1:
        puntosganados=puntosganados+10



posx=300
posy=300

color_negro =(0,0,64)

cont=0

posreal=[(300,300)]
posant=[]
#funcion basada en puntos dependiendo de lo que pisa
def quehacer(mp):

    if mp=='cora':
        sumayresta(1,0,0,0,0,0)
        
    elif mp=='arma1':
        sumayresta(0,1,0,0,0,0)

    elif mp=='arma2':
        sumayresta(0,0,1,0,0,0)
        
    elif mp=='arma3':
        sumayresta(0,0,0,1,0,0)

    elif mp=='monster':
        if cantbalas>0:
            sumayresta(0,0,0,0,1,0)
            sumayresta(0,0,0,0,0,1)
            
        elif cantbalas==0:
            sumayresta(2,0,0,0,0,1)
    else:
        pass


    
def manejopuntaje(posgx,posgy):
    
    if posgx==100 and posgy==100:
        mp= prueba[0]
        quehacer(mp)

    elif posgx==300 and posgy==100:
        mp= prueba[1]
        quehacer(mp)

    elif posgx==500 and posgy==100:
        mp= prueba[2]
        quehacer(mp)

    elif posgx==100 and posgy==300:
        mp= prueba[3]
        quehacer(mp)

    elif posgx==300 and posgy==300:
        mp= prueba[4]
        quehacer(mp)

    elif posgx==500 and posgy==300:
        mp= prueba[5]
        quehacer(mp)

    elif posgx==100 and posgy==500:
        mp= prueba[6]
        quehacer(mp)
  
    elif posgx==300 and posgy==500:
        mp= prueba[7]
        quehacer(mp)

    elif posgx==500 and posgy==500:
        mp= prueba[8]
        quehacer(mp)

    else:
        pass
    
#esta crea el objeto por cada movimiento
def posicionar_pormov(h,vmat,rezgx,rezgy):
    if h=='cora':
        prueba[vmat]=h
        matriz[vmat]=Corazon(rezgx,rezgy)
        matriz[vmat].posic(rezgx,rezgy)

    elif h=='monster':
        prueba[vmat]=h
        matriz[vmat]=Monstruo(rezgx,rezgy)
        matriz[vmat].posic(rezgx,rezgy)

    elif h=='arma1':
        prueba[vmat]=h
        matriz[vmat]=Arma1(rezgx,rezgy)
        matriz[vmat].posic(rezgx,rezgy)
        
    elif h=='arma2':
        prueba[vmat]=h
        matriz[vmat]=Arma2(rezgx,rezgy)
        matriz[vmat].posic(rezgx,rezgy)

    elif h=='arma3':
        prueba[vmat]=h
        matriz[vmat]=Arma3(rezgx,rezgy)
        matriz[vmat].posic(rezgx,rezgy)
        
#retorna valor de matriz si la posx, posy se encuentra metemos
#el valor de la lista y renombramos el diccionario
def nueva_creacion(rezgx,rezgy):
    
    #Tira el tipo de objeto que va a salir
    probabilidad= random.randint(1,10)
    h=0
    if probabilidad>=0 and probabilidad<=4:
        h=('monster')
        
        
    elif probabilidad>=5 and probabilidad<=7:
        probabilidad2=random.randint(1,10)
        if probabilidad2>=0 and probabilidad2<=5:
            h=('arma1')
            
        elif probabilidad2>=6 and probabilidad2<=8:
            h=('arma2')
            
        else:
            h=('arma3')

    else:
        h=('cora')

    

    #Esta parte modifica el diccionario para saber donde colocar 

    if rezgx==100 and rezgy==100:
        dic[matriz[0]]=h
        vmat=0
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==300 and rezgy==100:
        dic[matriz[1]]=h
        vmat=1
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==500 and rezgy==100:
        dic[matriz[2]]=h
        vmat=2
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==100 and rezgy==300:
        dic[matriz[3]]=h
        vmat=3
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==300 and rezgy==300:
        dic[matriz[4]]=h
        vmat=4
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==500 and rezgy==300:
        dic[matriz[5]]=h
        vmat=5
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==100 and rezgy==500:
        dic[matriz[1]]=h
        vmat=6
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==300 and rezgy==500:
        dic[matriz[1]]=h
        vmat=7
        posicionar_pormov(h,vmat,rezgx,rezgy)
    elif rezgx==500 and rezgy==500:
        dic[matriz[1]]=h
        vmat=8
        posicionar_pormov(h,vmat,rezgx,rezgy)
    else:
        pass
    

#esta funcion lo que hace es crear listas con la posicion
#actual del gato y su posicion anterior
def log_del_juego(posgx,posgy,rezgx,rezgy):
    if posreal[-1]==(posgx,posgy):
        pass
    else:
        posreal.append((posgx,posgy))

    if posreal[-1]==(rezgx,rezgy):
        pass
    else:
        posant.append((rezgx,rezgy))
        nueva_creacion(rezgx,rezgy)
        

class Gatito(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('imagenes/GATITO.png')
        self.rect=self.image.get_rect()
        self.rect.centerx= 300
        self.rect.centery= 300
        self.rezagox=300
        self.rezagoy=300
        
   
    def update(self,evento):
        
        if evento.key == pygame.K_LEFT and self.rect.left>0:
            self.speed= [-200,0]
            self.rezagox-=200
            
        elif evento.key == pygame.K_RIGHT and self.rect.right<ANCHO-200:
            self.speed= [200,0]
            self.rezagox+=200
            
        elif evento.key == pygame.K_UP and self.rect.top>0:
            self.speed= [0,-200]
            self.rezagoy-=200
            
        elif evento.key == pygame.K_DOWN and self.rect.bottom<ALTO:
            self.speed= [0,200]
            self.rezagoy+=200
            
        else:
            self.speed= [0,0]

        
        jugador.rezago()

        self.rect.move_ip(self.speed)


    def rezago(self):
        rezgx=self.rect.centerx
        rezgy=self.rect.centery
        posgx=self.rezagox
        posgy=self.rezagoy
        log_del_juego(posgx,posgy,rezgx,rezgy)
        manejopuntaje(posgx,posgy)
        



        
class Corazon(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

    def posic(self,posx,posy):
        self.image= pygame.image.load('imagenes/corazon.png')
        self.rect=self.image.get_rect()
        self.rect.centerx= posx
        self.rect.centery= posy

class Arma1(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

    def posic(self,posx,posy):
        self.image= pygame.image.load('imagenes/arma.jpg')
        self.rect=self.image.get_rect()
        self.rect.centerx= posx
        self.rect.centery= posy
        
class Arma2(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

    def posic(self,posx,posy):
        self.image= pygame.image.load('imagenes/doblearma.jpg')
        self.rect=self.image.get_rect()
        self.rect.centerx= posx
        self.rect.centery= posy

class Arma3(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

    def posic(self,posx,posy):
        self.image= pygame.image.load('imagenes/triplearma.jpg')
        self.rect=self.image.get_rect()
        self.rect.centerx= posx
        self.rect.centery= posy

class Monstruo(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

    def posic(self,posx,posy):
        self.image= pygame.image.load('imagenes/gatitomalo.png')
        self.rect=self.image.get_rect()
        self.rect.centerx= posx
        self.rect.centery= posy
        
    

        
        


    

class Grid:
    def __init__(self):
        self.grid_lines = [((0,200),(600,200),), #primera linea horiz
                           ((0,400),(600,400)), #segunda linea horiz
                           ((200,0),(200,600)), #primera linea vert
                           ((400,0),(400,600))] #segunda linea vert

        

    def draw(self,pantalla):
        for line in self.grid_lines:
            pygame.draw.line(pantalla, (200,200,200), line[0], line[1], 2)



#esta funcion lo que hace es definir las posiciones iniciales
a=0
b=1
c=2
d=3
e=4
f=5
g=6
v=7
i=8

matriz=[a,b,c,d,e,f,g,v,i]
dic={}
x=0
posx=0
posy=0
    

for i in range(0,9):
    probabilidad= random.randint(1,10)
    
    if probabilidad>=0 and probabilidad<=4:
        h=('monster')
        
        
    elif probabilidad>=5 and probabilidad<=7:
        probabilidad2=random.randint(1,10)
        if probabilidad2>=0 and probabilidad2<=5:
            h=('arma1')
            
        elif probabilidad2>=6 and probabilidad2<=8:
            h=('arma2')
            
        else:
            h=('arma3')
            
              
    else:
        h=('cora')
    prueba.append(h)
    pos=matriz[i]
    dic[pos]=h


for j in range(0,9):
    if matriz[j]==a:
        posx=100
        posy=100
       

    elif matriz[j]==b:
        posx=300
        posy=100
       

    elif matriz[j]==c:
        posx=500
        posy=100
     

    elif matriz[j]==d:
        posx=100
        posy=300
      

    elif matriz[j]==e:
        posx=300
        posy=300
        

    elif matriz[j]==f:
        posx=500
        posy=300
        
    elif matriz[j]==g:
        posx=100
        posy=500
        

    elif matriz[j]==v:
        posx=300
        posy=500
        

    elif matriz[j]==i:
        posx=500
        posy=500
        

    else:
        continue



    
    if dic[matriz[j]]=='cora':
        matriz[j]=Corazon(posx,posy)
        matriz[j].posic(posx,posy)

    elif dic[matriz[j]]=='monster':
        matriz[j]=Monstruo(posx,posy)
        matriz[j].posic(posx,posy)

    elif dic[matriz[j]]=='arma1':
        matriz[j]=Arma1(posx,posy)
        matriz[j].posic(posx,posy)
        
    elif dic[matriz[j]]=='arma2':
        matriz[j]=Arma2(posx,posy)
        matriz[j].posic(posx,posy)

    elif dic[matriz[j]]=='arma3':
        matriz[j]=Arma3(posx,posy)
        matriz[j].posic(posx,posy)
        


jugador= Gatito()
grid=Grid()

def juego_terminado():
    fuente= pygame.font.SysFont('Arial',50)
    texto= fuente.render('JUEGO TERMINADO',True,(255,255,255))
    texto_rect= texto.get_rect()
    texto_rect.center=[300,300]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    time.sleep(3)
    sys.exit()

def mostrar_corazones():
    fuente= pygame.font.SysFont('Consolas',20)
    texto= fuente.render('Corazones:'+str(cantidadcorazones),True,(255,255,255))
    texto_rect= texto.get_rect()
    texto_rect.center=[700,100]
    pantalla.blit(texto, texto_rect)

def mostrar_puntuacion():
    fuente= pygame.font.SysFont('Consolas',20)
    texto= fuente.render('Puntuacion:'+str(puntosganados),True,(255,255,255))
    texto_rect= texto.get_rect()
    texto_rect.center=[700,300]
    pantalla.blit(texto, texto_rect)
    
def mostrar_balas():
    fuente= pygame.font.SysFont('Consolas',20)
    texto= fuente.render('Balas:'+str(cantbalas),True,(255,255,255))
    texto_rect= texto.get_rect()
    texto_rect.center=[700,500]
    pantalla.blit(texto, texto_rect)
while True:
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type== pygame.KEYDOWN:
            jugador.update(evento)
            matriz[0].update(evento)
            matriz[1].update(evento)
            matriz[2].update(evento)
            matriz[3].update(evento)
            matriz[4].update(evento)
            matriz[5].update(evento)
            matriz[6].update(evento)
            matriz[7].update(evento)
            matriz[8].update(evento)
            continue

    if cantidadcorazones==0:
        juego_terminado()
        sys.exit()
        
        
    pantalla.fill(color_negro) 
    mostrar_corazones()
    mostrar_puntuacion()
    mostrar_balas()
    pantalla.blit(matriz[0].image,matriz[0].rect)
    pantalla.blit(matriz[1].image,matriz[1].rect)
    pantalla.blit(matriz[2].image,matriz[2].rect)
    pantalla.blit(matriz[3].image,matriz[3].rect)
    pantalla.blit(matriz[4].image,matriz[4].rect)
    pantalla.blit(matriz[5].image,matriz[5].rect)
    pantalla.blit(matriz[6].image,matriz[6].rect)
    pantalla.blit(matriz[7].image,matriz[7].rect)
    pantalla.blit(matriz[8].image,matriz[8].rect)
    
    
    pantalla.blit(jugador.image,jugador.rect)
    grid.draw(pantalla)
    pygame.display.flip()
    



