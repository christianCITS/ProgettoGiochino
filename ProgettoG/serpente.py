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
        self.velocita=220
    
        


    def muoviSerpente(self,tasto,dt):
        if tasto== 'w':
            self.destra=False
            self.sinistra=False
            self.su=True
            self.giu=False

        if self.su:
            self.y -= self.velocita * dt

        if tasto== 's':
            self.destra=False
            self.sinistra=False
            self.su=False
            self.giu=True

        if self.giu:
            self.y += self.velocita * dt

        if tasto== 'a':
            self.destra=False
            self.sinistra=True
            self.su=False
            self.giu=False

        if self.sinistra:
            self.x -= self.velocita * dt

        if tasto== 'd':
            self.destra=True
            self.sinistra=False
            self.su=False
            self.giu=False

        if self.destra:    
            self.x += self.velocita * dt
        

        self.testa.update(self.x, self.y,30,30)

    def checkCollisioni(self,game):
        for mela in game.mele:
                if  self.testa.colliderect(mela.hitmela):
                    self.velocita+= 100
                    game.aggiornaPunt(mela)

        for bordi in game.mappa.bordi:
            if self.testa.colliderect(bordi):
                game.perso= True
                

    


        
       
        





    def disegnaSerp(self,game):

        a=self.testa
        print(self.testa)
        pygame.draw.rect(game.screen,"black",a)






    def collisioneDimitri(self):
        pass



    

