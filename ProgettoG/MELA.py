import pygame
from game import *



class Mela:

    def __init__(self, x,y,raggio):
        self.y = y
        self.x = x
        self.faccia = 'MELADIMITRI.jpg'
        self.immagine= pygame.image.load(self.faccia)
        self.immagine= pygame.transform.scale(self.immagine, (2*raggio, 2*raggio))
        self.raggio=raggio
        self.forma=None
        self.hitmela = self.immagine.get_rect(center=(self.x, self.y))

    
    
    def creaDimitri(self,game):

        game.screen.blit(self.immagine, self.hitmela)



    

        

        
    


    


    
        
    
    


