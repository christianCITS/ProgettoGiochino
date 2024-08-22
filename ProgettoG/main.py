import pygame
from mappa import *
from MELA import *
from serpente import *
from game import *
#from christian import *

# pygame setup
pygame.init()

#grandezza display
screen = pygame.display.set_mode((1920, 1080))

clock = pygame.time.Clock()
running = True
dt = 0

#posizione del giocatore
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

a=60
player_size = (30, 30)  # Dimensioni del rettangolo (larghezza, altezza)


#creazione bordi più mappa
mappa=Mappa(1920,1080)
mappa.creaMappa(screen)


while running:

    #qunado il gioco viene chiuso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #colore sfondo
    screen.fill("light blue")
    
    #posizione giocatore
    rect=pygame.Rect(player_pos,player_size)
    
    #personaggio che va cambiato
    pygame.draw.rect(screen,"orange",rect)

    #bordi visivi della mappa NO BLOCCO
    mappa.disegnaBordi(screen)

    #Spostamento quadrato futuro serpente
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 900 * dt
    if keys[pygame.K_s]:
        player_pos.y += 900 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 900 * dt
    if keys[pygame.K_d]:
        player_pos.x += 900 * dt

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



    


