import pygame
import random
from MELA import Mela
from serpente import Serpente
from mappa import *


class Game:
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance
    

    def __init__(self):
        self.mappa = Mappa(1920,1080)
        self.mele = []


    def spawnabro(self):
        mela = Mela(random.randint(self.mappa.larghezza-100,1500),random.randint(self.mappa.altezza-100,850))
        self.mele.append(mela)
    
    