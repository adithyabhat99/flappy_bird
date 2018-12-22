import time 
import random
import pygame
pygame.init()

class Game():
    color=(255,200,100)
    dis_w=500
    dis_h=576
    bird_h=24
    x_change=5
    y_change=0


    lists=pygame.sprite.Group()
    gameDisplay=pygame.display.set_mode((dis_w,dis_h))
    pygame.display.set_caption('Flappy Bird')
    clock=pygame.time.Clock()
    bird=pygame.image.load('resources/bluebird.png')
    background=pygame.image.load('resources/background-day.png')
    thing1=pygame.image.load('resources/pipe-green.png')
    thing2=pygame.image.load('resources/pipe-red.png')

    def bi(self,x,y):
        self.gameDisplay.blit(self.bird,(x,y))

    def back(self):
        self.gameDisplay.blit(self.background,(0,0))

    

    def things1(self):
        if self.chh==0:
            self.thingy=-30
        elif self.chh==1:
            self.thingy=300
        self.thingx=490
        return self.thingx,self.thingy
        


    def text_objects(self,text,col):
        self.textSurface=col.render(text,True,self.color)
        return self.textSurface,self.textSurface.get_rect()

    def message(self,str):
        self.col=pygame.font.Font('freesansbold.ttf',50)
        self.textSurface,self.textRect=self.text_objects(str,self.col)
        self.textRect.center=((self.dis_w*0.5),(self.dis_h*0.4))
        self.gameDisplay.blit(self.textSurface,self.textRect)
        pygame.display.update()


    def reset(self):
        self.message('Game Over')
        time.sleep(0.5)
        self.gameloop()
        
        

    def gameloop(self):
        self.Exit=False
        self.x=(self.dis_w*0)
        self.y=(self.dis_h*0.5)
        self.xx=0
        while not self.Exit:
            for self.event in pygame.event.get():
                if self.event.type== pygame.QUIT:
                    pygame.quit()
                    quit()
            self.back()
            if self.xx%80==40 or self.xx==0:
                self.chh=random.randrange(2)
                if self.chh==1:
                    ob=objects(self.thing1)
                if self.chh==0:
                    ob=objects(self.thing2)
                ob.rect.x,ob.rect.y=self.things1()
                self.lists.add(ob)
            self.xx+=1
            self.lists.draw(self.gameDisplay)
            self.lists.update()
            self.bi(self.x,self.y)

            if self.event.type==pygame.KEYDOWN:
                if self.event.key==pygame.K_DOWN:
                    self.y_change=20
                elif self.event.key==pygame.K_UP:
                    self.y_change=-20

            if self.event.type==pygame.KEYUP:
                self.y_change=0
            
            if self.x==0.4*(self.dis_w):
                self.x_change=0
            else:
                self.x_change=5

            self.x+=self.x_change
            self.y+=self.y_change
            

            if self.y<self.dis_h-self.bird_h and self.y<0:
                self.reset()
            
            if self.y>self.dis_h-self.bird_h:
                self.reset()

            pygame.display.update()
            self.clock.tick(80)

#Child class of Game class and PyGame Sprite to move and load images randomly
class objects(pygame.sprite.Sprite,Game):  
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.load(image)
    
    def load(self,image):
        self.image=image
        self.rect = self.image.get_rect()
        pygame.display.update()

    def update(self):
        self.rect.x-=7
        

game=Game()
game.gameloop()
pygame.quit()
quit()
