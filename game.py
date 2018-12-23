import time 
import random
import pygame
pygame.init()

class Game():
    color=(255,200,100)
    dis_w=1366
    dis_h=768
    bird_h=24
    x_change=5
    y_change=0
    score=0
    x=(dis_w*0)
    y=(dis_h*0.5)
    crashed=False
    hitbox=(x+10,y+10,30,30)

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
            self.thingy=400
        self.thingx=1360
        return self.thingx,self.thingy
        
    def text_objects(self,text,col):
        self.textSurface=col.render(text,True,self.color)
        return self.textSurface,self.textSurface.get_rect()

    def message(self,str,m,n):
        self.font=pygame.font.Font('freesansbold.ttf',50)
        self.textSurface,self.textRect=self.text_objects(str,self.font)
        self.textRect.center=(m,n)
        self.gameDisplay.blit(self.textSurface,self.textRect)
        pygame.display.update()



    def reset(self):
        self.message('Game Over',(self.dis_w*0.5),(self.dis_h*0.4))
        time.sleep(0.5)
        self.score=0
        for i in self.lists:
            del i
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
                self.lists.add(ob) #creating list of objects(images) of objects class
            self.xx+=1
            self.lists.draw(self.gameDisplay)
            self.lists.update()
            self.bi(self.x,self.y)

            if self.event.type==pygame.KEYDOWN:
                if self.event.key==pygame.K_SPACE:
                    self.y_change=-20

            if self.event.type==pygame.KEYUP:
                self.y_change=5
            
            if self.x==500:
                self.x_change=0
            else:
                self.x_change=5

            self.x+=self.x_change
            self.y+=self.y_change
            self.hitbox=(self.x-self.x_change,self.y-self.y_change,30,30)
            pygame.draw.rect(self.gameDisplay,self.color,self.hitbox,2)

            

            if self.y<self.dis_h-self.bird_h and self.y<-20:
                self.reset()
            
            if self.y>self.dis_h-self.bird_h:
                self.reset()

            if self.crashed==True:
                self.reset()

            self.message(str(self.score),50,50)
            
            pygame.display.update()
            self.clock.tick(80)

#Child class of Game class and PyGame Sprite to move objects
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
        if self.rect.x<-50:
            Game.score+=1
            pygame.display.update()
            self.kill()

        self.hitbox=(self.rect.x+7,self.rect.y,52,320)
        
        if Game.hitbox[1]>self.hitbox[1] and Game.hitbox[1]-30<self.hitbox[1]:
            Game.crashed=True

        pygame.draw.rect(Game.gameDisplay,Game.color,self.hitbox,2)
    
    
    
        


        

        
            
        

    


game=Game()
game.gameloop()
pygame.quit()
quit()
