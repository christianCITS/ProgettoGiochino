import pygame



class Blocco:


    def __init__(self,x,y,destra,sinistra,su,giu):
        self.x=x
        self.y=y
        self.rect=pygame.Rect(x,y,30,30)
        self.destra=destra
        self.sinistra=sinistra
        self.su=su
        self.giu=giu
        self.velocita=220


    

    def muoviBlocco(self,tasto,dt):
        if tasto== 'w' and not self.giu:
            self.destra=False
            self.sinistra=False
            self.su=True
            self.giu=False
        

        if self.su:
            self.y -= self.velocita * dt

        if tasto== 's' and not self.su:
            self.destra=False
            self.sinistra=False
            self.su=False
            self.giu=True

        if self.giu:
            self.y += self.velocita * dt

        if tasto== 'a' and not self.destra:
            self.destra=False
            self.sinistra=True
            self.su=False
            self.giu=False

        if self.sinistra:
            self.x -= self.velocita * dt

        if tasto== 'd' and not self.sinistra:
            self.destra=True
            self.sinistra=False
            self.su=False
            self.giu=False

        if self.destra:    
            self.x += self.velocita * dt
        

        self.rect.update(self.x, self.y,30,30)


    def muoviBlocco(self,su,giu,destra,sinistra,dt):
        if su and not self.giu:
            self.destra=False
            self.sinistra=False
            self.su=True
            self.giu=False
        

        if self.su:
            self.y -= self.velocita * dt

        if giu and not self.su:
            self.destra=False
            self.sinistra=False
            self.su=False
            self.giu=True

        if self.giu:
            self.y += self.velocita * dt

        if sinistra and not self.destra:
            self.destra=False
            self.sinistra=True
            self.su=False
            self.giu=False

        if self.sinistra:
            self.x -= self.velocita * dt

        if destra and not self.sinistra:
            self.destra=True
            self.sinistra=False
            self.su=False
            self.giu=False

        if self.destra:    
            self.x += self.velocita * dt
        

        self.rect.update(self.x, self.y,30,30)
    
    


    def disegnaBlocco(self,game):

        a=self.rect
        pygame.draw.rect(game.screen,"black",a)






    


