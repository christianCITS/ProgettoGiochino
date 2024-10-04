import pygame
import random
from MELA import Mela
from serpente import Serpente



def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance




class Game:

    


    def __init__(self):
        #grandezza display
        self.screen = pygame.display.set_mode((1080,750))
        self.mele = []
        self.mappa=None
        self.serpente=None
        self.font=None
        self.testo=None
        self.punteggio= 0
        self.testopunteggio=None
        self.perso=False

        
    
    def disegnaMele(self):
        for mela in self.mele:
            mela.creaDimitri(self)


        



    def spawnabro(self):
        randx=random.randint(self.mappa.latoQuad*2+10,self.mappa.larghezza-self.mappa.latoQuad*2+10)
        randy=random.randint(self.mappa.latoQuad*2+10,self.mappa.altezza-self.mappa.latoQuad*2+10)
        melaD = Mela(randx,randy,15)
        self.mele.append(melaD)
        



    
    def startaGioco(self,mappa):
        #crea fisicamente la mappa con gli attributi inseriti
        self.mappa=mappa
        self.mappa.creaMappa()
        self.spawnabro()
        self.serpente=Serpente(self.mappa.larghezza // 2,self.mappa.altezza // 2)
        self.font=pygame.font.SysFont("Arial Narrow",20)
        self.testo=self.font.render("Dimitri acciuffati = ",True,"black",None)
        self.testopunteggio=self.font.render(f"{self.punteggio}",True,"black",None)



    
    def getMappa(self):
        return self.mappa
    

    def disegnaFont(self):
        self.screen.blit(self.testo, (50, 50))  # Posizione del testo
        self.screen.blit(self.testopunteggio, (180, 50))  # Posizione del punteggio


    def aggiornaPunt(self,mela):
        self.mele.remove(mela)
        self.spawnabro()
        self.punteggio+=1
        self.testopunteggio=self.font.render(f"{self.punteggio}",True,"black",None)
        self.serpente.crescitaSerp()

    








        



@singleton
class GameSingleton(Game):
    pass



