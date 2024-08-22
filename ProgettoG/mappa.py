import pygame

class Mappa:

    def __init__(self,larghezza,altezza):
        self.larghezza=larghezza
        self.altezza=altezza
        self.bordi=[]

    
    def creaMappa(self,screen):
        self.creaBordi()
        self.disegnaBordi(screen)
    




    def creaBordi(self):
        latoQuad=30
        #lato sinistro
        for i in range(self.altezza// latoQuad):
            self.bordi.append(pygame.Rect(0,i*latoQuad,latoQuad,latoQuad))
        #lato destro
        for i in range(self.altezza// latoQuad):
            self.bordi.append(pygame.Rect(self.larghezza-latoQuad,i*latoQuad,latoQuad,latoQuad))
        #lato sopra
        for i in range(self.larghezza// latoQuad):
            self.bordi.append(pygame.Rect(i*latoQuad,0,latoQuad,latoQuad))
        #lato sotto 
        for i in range(self.larghezza// latoQuad):
            self.bordi.append(pygame.Rect(i*latoQuad,self.altezza-latoQuad,latoQuad,latoQuad))

    
    def disegnaBordi(self,screen):
            for rect in self.bordi:
                pygame.draw.rect(screen,"black",rect)
        






    





    


    
