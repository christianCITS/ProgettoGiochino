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
mappa=Mappa(1080,750)
clock = pygame.time.Clock()
running = True
dt = 0
game=GameSingleton()
game.startaGioco(mappa)
#posizione del giocatore
player_pos = pygame.Vector2(game.screen.get_width() / 2, game.screen.get_height() / 2)
font=pygame.font.SysFont("Arial Narrow",80)
testo=font.render("GAME OVER",True,"black",None)
font2=pygame.font.SysFont("Liberation Sans",50)




a=60
player_size = (30, 30)  # Dimensioni del rettangolo (larghezza, altezza)



while running:
    if not game.perso:
        #riempe colore scelto sfondo
        game.screen.fill("white")
        
    
        #bordi visivi della mappa NO BLOCCO
        game.mappa.disegnaBordi()
        

        #Spostamento quadrato futuro serpente
        keys = pygame.key.get_pressed()
        tasto=tastoPremuto(keys)

        #chiudere il gioco premenendo esc
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        game.disegnaFont()
        game.serpente.muoviSerpente(tasto,dt)
        game.serpente.disegnaSerp(game)
        game.serpente.checkCollisioni(game)
        game.disegnaMele()
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        testostats=font2.render("Dimitri acciuffati = ",True,"black",None)
        testopunteggio=font2.render(f"{game.punteggio}",True,"black",None)
        game.screen.fill("red")
        game.screen.blit(testo, (400, 250))  # Posizione del testo
        game.screen.blit(testostats, (250, 400))  # Posizione del testo
        game.screen.blit(testopunteggio, (720,400))  # Posizione del punteggio 
        pygame.display.flip()
        
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    #cambio di fps
    if keys[pygame.K_l]:
        if a==60:
            a=120
        elif a==120:
            a=60
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    dt=clock.tick(a)/1000

pygame.quit()






    


