import pygame
from mappa import *
from MELA import *
from serpente import *
from game import *
#from christian import *

# pygame setup
pygame.init()



def tastoPremuto(keys):
    direzione_corrente=""
    if keys[pygame.K_w]:
        direzione_corrente = 'w'
    elif keys[pygame.K_s]:
        direzione_corrente = 's'
    elif keys[pygame.K_a]:
        direzione_corrente = 'a'
    elif keys[pygame.K_d]:
        direzione_corrente = 'd'
    return direzione_corrente


#Inizzializza mappa
mappa=Mappa(1920,1080)
clock = pygame.time.Clock()
running = True
dt = 0
game=GameSingleton()
game.startaGioco(mappa)
#posizione del giocatore
print(game.screen)
player_pos = pygame.Vector2(game.screen.get_width() / 2, game.screen.get_height() / 2)

a=60
player_size = (30, 30)  # Dimensioni del rettangolo (larghezza, altezza)



destra=True
sinistra=False
su=False
giu=False

while running:

    #qunado il gioco viene chiuso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #colore sfondo
    game.screen.fill("light blue")
    
    #posizione giocatore
    rect=pygame.Rect(player_pos,player_size)
    
    #personaggio che va cambiato
    pygame.draw.rect(game.screen,"orange",rect)

    #bordi visivi della mappa NO BLOCCO
    game.mappa.disegnaBordi()
    for mela in game.mele:
        mela.creaDimitri(game)
    

    #Spostamento quadrato futuro serpente
    keys = pygame.key.get_pressed()
    tasto=tastoPremuto(keys)
    if tasto== 'w':
        destra=False
        sinistra=False
        su=True
        giu=False

    if su:
        player_pos.y -= 50 * dt

    if tasto== 's':
        destra=False
        sinistra=False
        su=False
        giu=True

    if giu:
        player_pos.y += 50 * dt

    if tasto== 'a':
        destra=False
        sinistra=True
        su=False
        giu=False

    if sinistra:
        player_pos.x -= 50 * dt

    if tasto== 'd':
        destra=True
        sinistra=False
        su=False
        giu=False

    if destra:    
        player_pos.x += 50 * dt
    
    #chiudere il gioc premenendo esc
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    #cambio di fps
    if keys[pygame.K_l]:
        if a==60:
            a=120
        elif a==120:
            a=60
            
    dt=clock.tick(a)/1000

pygame.quit()






    


