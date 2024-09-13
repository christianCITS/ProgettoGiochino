import pygame
from game import *
from mappa import *
from MELA import *
from blocco import *


class Serpente:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grandezza = []
        #posizione giocatore
        self.destra=True
        self.sinistra=False
        self.su=False
        self.giu=False
        self.testa=Blocco(self.x,self.y,self.destra,self.sinistra,self.su,self.giu)
        self.velocita=220
        self.grandezza.append(self.testa)

    
        


    def muoviSerpente(self,tasto,dt):
        self.grandezza[0].muoviBlocco(tasto,dt)
        lunghezza_serp = len(self.grandezza)
        
        for i in range(lunghezza_serp):
            self.grandezza[lunghezza_serp - i].muoviBlocco(self.grandezza[lunghezza_serp - i].su,self.grandezza[lunghezza_serp - i].giu.self.grandezza[lunghezza_serp - i].destra,self.grandezza[lunghezza_serp - i].sinistra,self.grandezza[lunghezza_serp - i].velocita)

            



        

    def checkCollisioni(self,game):
        for mela in game.mele:
                if  self.testa.colliderect(mela.hitmela):
                    self.velocita+= 20
                    game.aggiornaPunt(mela)


        for bordi in game.mappa.bordi:
            if self.testa.colliderect(bordi):
                game.perso= True
                

    


        
       
        





    def disegnaSerp(self,game):
        for blocco in self.grandezza:
            blocco.disegnaBlocco(game)


        






    def crescitaSerp(self):
        pass
       


        



    

