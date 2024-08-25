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
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        direzione_corrente = 'w'
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        direzione_corrente = 's'
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        direzione_corrente = 'a'
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        direzione_corrente = 'd'
    return direzione_corrente


#Inizializza mappa
mappa=Mappa(1920,1080)
clock = pygame.time.Clock()
running = True
dt = 0
game=GameSingleton()
game.startaGioco(mappa)
#posizione del giocatore
player_pos = pygame.Vector2(game.screen.get_width() / 2, game.screen.get_height() / 2)

a=60
player_size = (30, 30)  # Dimensioni del rettangolo (larghezza, altezza)



while running:

    #qunado il gioco viene chiuso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #colore sfondo
    game.screen.fill("light blue")
    
   
    #bordi visivi della mappa NO BLOCCO
    game.mappa.disegnaBordi()
    for mela in game.mele:
        mela.creaDimitri(game)
    

    #Spostamento quadrato futuro serpente
    keys = pygame.key.get_pressed()
    tasto=tastoPremuto(keys)

    #chiudere il gioco premenendo esc
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    game.disegnaFont()
    game.serpente.muoviSerpente(tasto,dt)
    game.serpente.disegnaSerp(game)
    
    
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






    


