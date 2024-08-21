import pygame

class Mappa:

    def __init__(self,altezza,larghezza):
        self.altezza=altezza
        self.larghezza=larghezza
        self.bordi=[]
    
    def creaMappa(self):
        screen = pygame.display.set_mode((self.altezza,self.larghezza))
    




    def creaBordi(self):
        latoQuad=30
        for i in range(self.altezza/ latoQuad):
            self.bordi.append(pygame.Rect())

        


    





    


    
