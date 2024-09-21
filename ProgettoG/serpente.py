import pygame
from game import *
from mappa import *
from MELA import *
from blocco import *


class Serpente:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grandezza:list[Blocco] = []
        self.posizioni_precedenti = []
        #posizione giocatore
        self.destra=True
        self.sinistra=False
        self.su=False
        self.giu=False
        self.testa=Blocco(self.x,self.y,self.destra,self.sinistra,self.su,self.giu)
        self.velocita=400
        self.grandezza.append(self.testa)

    
        


    '''def muoviSerpente(self,tasto,dt):
        lunghezza_serp = len(self.grandezza)
        
        for i in range(lunghezza_serp):
            #Ciclo al contrario
            j = lunghezza_serp - i - 1
            if j == 0:
                self.grandezza[j].muoviBlocco(tasto,dt)
            
            
            else:
                print("ciao")            
                self.grandezza[j].seguiBlocco(self.grandezza[j-1].su,
                                                           self.grandezza[j-1].giu,
                                                           self.grandezza[j-1].destra,
                                                           self.grandezza[j-1].sinistra,
                                                           dt)'''
    def muoviSerpente(self, tasto, dt):
        # Prima aggiorniamo la testa
        self.grandezza[0].muoviBlocco(tasto, dt, self.velocita)
        
        # Memorizziamo la posizione attuale della testa
        pos_testa = (self.grandezza[0].x, self.grandezza[0].y)
        self.posizioni_precedenti.insert(0, pos_testa)  # Inseriamo in testa la posizione attuale

        # Manteniamo solo le posizioni che servono per tutti i blocchi
        if len(self.posizioni_precedenti) > len(self.grandezza) * 10:  # Distanza maggiore tra i blocchi
            self.posizioni_precedenti.pop()  # Rimuoviamo la più vecchia

        # Aggiorniamo le posizioni degli altri blocchi in base alla coda di posizioni
        for i in range(1, len(self.grandezza)):
            # Ogni blocco segue la posizione precedente del blocco davanti a sé
            x_precedente, y_precedente = self.posizioni_precedenti[i*4+3]  # Spazio aumentato con un fattore di 10
            self.grandezza[i].seguiBlocco(x_precedente, y_precedente)

    
                     



        

    def checkCollisioni(self,game):
        for mela in game.mele:
                if  self.grandezza[0].rect.colliderect(mela.hitmela):
                    self.velocita+= 100
                    game.aggiornaPunt(mela)
        


        for bordi in game.mappa.bordi:
            if self.grandezza[0].rect.colliderect(bordi):
                game.perso= True
                
        for blocco in self.grandezza:
            if self.grandezza[0].rect.colliderect(blocco.rect) and blocco is not self.grandezza[0]:
                game.perso=True

        
        
        
    
    def disegnaSerp(self,game):
        i=0
        for blocco in self.grandezza:
            #print(blocco.x,blocco.y,i)
            i+=1
            blocco.disegnaBlocco(game)


    def crescitaSerp(self):
        x = self.grandezza[-1].x
        y = self.grandezza[-1].y
        if self.grandezza[-1].destra:
            blocco=Blocco(x+200,y,self.grandezza[-1].destra,self.grandezza[-1].sinistra,self.grandezza[-1].su,self.grandezza[-1].giu)
        if self.grandezza[-1].sinistra:
            blocco=Blocco(x-200,y,self.grandezza[-1].destra,self.grandezza[-1].sinistra,self.grandezza[-1].su,self.grandezza[-1].giu)
        if self.grandezza[-1].su:
            blocco=Blocco(x,y+200,self.grandezza[-1].destra,self.grandezza[-1].sinistra,self.grandezza[-1].su,self.grandezza[-1].giu)
        if self.grandezza[-1].giu:
            blocco=Blocco(x,y-200,self.grandezza[-1].destra,self.grandezza[-1].sinistra,self.grandezza[-1].su,self.grandezza[-1].giu)
        self.grandezza.append(blocco)
        


        



    

