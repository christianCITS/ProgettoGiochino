import pygame
from game import *

class Mappa:

    def __init__(self,larghezza,altezza):
        self.larghezza=larghezza
        self.altezza=altezza
        self.bordi=[]
        self.latoQuad=30
        

    
    def creaMappa(self):
        self.creaBordi()
        self.disegnaBordi()
    

    def creaBordi(self):
        #lato sinistro
        for i in range(self.altezza// self.latoQuad):
            self.bordi.append(pygame.Rect(0,i*self.latoQuad,self.latoQuad,self.latoQuad))
        #lato destro
        for i in range(self.altezza// self.latoQuad):
            self.bordi.append(pygame.Rect(self.larghezza-self.latoQuad,i*self.latoQuad,self.latoQuad,self.latoQuad))
        #lato sopra
        for i in range(self.larghezza// self.latoQuad):
            self.bordi.append(pygame.Rect(i*self.latoQuad,0,self.latoQuad,self.latoQuad))
        #lato sotto 
        for i in range(self.larghezza// self.latoQuad):
            self.bordi.append(pygame.Rect(i*self.latoQuad,self.altezza-self.latoQuad,self.latoQuad,self.latoQuad))

    
    def disegnaBordi(self):
            game=GameSingleton()
            for rect in self.bordi:
                pygame.draw.rect(game.screen,"red",rect)
           
        
    








    





    


    
