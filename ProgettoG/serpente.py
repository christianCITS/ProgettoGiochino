import pygame
from game import *
from mappa import *
from MELA import *

class Serpente:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grandezza = []
        #posizione giocatore
        self.testa=pygame.Rect(x,y,30,30)
        self.destra=True
        self.sinistra=False
        self.su=False
        self.giu=False
    
        


    def muoviSerpente(self,tasto,dt):
        if tasto== 'w':
            self.destra=False
            self.sinistra=False
            self.su=True
            self.giu=False

        if self.su:
            self.y -= 50 * dt

        if tasto== 's':
            self.destra=False
            self.sinistra=False
            self.su=False
            self.giu=True

        if self.giu:
            self.y += 50 * dt

        if tasto== 'a':
            self.destra=False
            self.sinistra=True
            self.su=False
            self.giu=False

        if self.sinistra:
            self.x -= 50 * dt

        if tasto== 'd':
            self.destra=True
            self.sinistra=False
            self.su=False
            self.giu=False

        if self.destra:    
            self.x += 50 * dt
        

        self.testa.update(self.x, self.y,30,30)
        





    def disegnaSerp(self,game):

        a=self.testa
        print(self.testa)
        pygame.draw.rect(game.screen,"black",a)






    def collisioneDimitri(self):
        pass



    

