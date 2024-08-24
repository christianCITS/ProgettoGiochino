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
        self.screen = pygame.display.set_mode((1920, 1080))
        self.mele = []
        self.mappa=None
    


        



    def spawnabro(self):
        mela = Mela(1000,500,20)
        self.mele.append(mela)



    
    def startaGioco(self,mappa):
        #crea fisicamente la mappa con gli attributi inseriti
        self.mappa=mappa
        self.mappa.creaMappa()
        self.spawnabro()



    
    def getMappa(self):
        return self.mappa



@singleton
class GameSingleton(Game):
    pass
