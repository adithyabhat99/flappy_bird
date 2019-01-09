import time
import random
import pygame

pygame.init()


class Game():
    color = (255, 200, 100)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    green1 = (100, 255, 100)
    red = (255, 0, 0)
    red1 = (255, 100, 100)
    dis_w = 1366
    dis_h = 768
    bird_h = 24
    x_change = 5
    y_change = 6
    score = 0
    x = (dis_w*0)
    y = (dis_h*0.5)
    Exit = False
    lists = pygame.sprite.Group()
    font = pygame.font.Font('freesansbold.ttf', 50)
    gameDisplay = pygame.display.set_mode((dis_w, dis_h))
    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()
    bird = pygame.image.load('resources/bluebird.png')
    background = pygame.image.load('resources/background-day.png')
    thing1 = pygame.image.load('resources/pipe-green.png')
    thing2 = pygame.image.load('resources/pipe-red.png')
    die = pygame.mixer.Sound('resources/music/die.wav')
    point = pygame.mixer.Sound('resources/music/score.wav')

    def bi(self, image, x, y):
        self.gameDisplay.blit(image, (x, y))

    def things1(self):
        if self.chh == 0:
            self.thingy = -30
        elif self.chh == 1:
            self.thingy = 400
        self.thingx = 1360
        return self.thingx, self.thingy

    def text_objects(self, text, col):
        self.textSurface = col.render(text, True, self.color)
        return self.textSurface, self.textSurface.get_rect()

    def message(self, strr, m, n, font):
        self.textSurface, self.textRect = self.text_objects(strr, font)
        self.textRect.center = (m, n)
        self.gameDisplay.blit(self.textSurface, self.textRect)
        pygame.display.update()

    def start(self):
        while not self.Exit:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.bi(self.background, 0, 0)
                self.smallText = pygame.font.Font("freesansbold.ttf", 20)
                self.mouse = pygame.mouse.get_pos()
                self.click = pygame.mouse.get_pressed()
                if 550+80 > self.mouse[0] > 550 and 280+40 > self.mouse[1] > 280:
                    pygame.draw.rect(self.gameDisplay,
                                     self.green1, (550, 280, 80, 40))
                    self.message("Go!", (550+(80/2)),
                                 (280+(40/2)), self.smallText)
                    if self.click[0]:
                        self.gameloop()
                else:
                    pygame.draw.rect(self.gameDisplay,
                                     self.green, (550, 280, 80, 40))
                    self.message("Go!", (550+(80/2)),
                                 (280+(40/2)), self.smallText)
                if 700+80 > self.mouse[0] > 700 and 280+40 > self.mouse[1] > 280:
                    pygame.draw.rect(self.gameDisplay,
                                     self.red1, (700, 280, 80, 40))
                    self.message("Stop", (700+(80/2)),
                                 (280+(40/2)), self.smallText)
                    if self.click[0]:
                        self.message('Bye!', (self.dis_w*0.5),
                                     (self.dis_h*0.4), self.font)
                        time.sleep(0.1)
                        pygame.quit()
                        quit()
                else:
                    pygame.draw.rect(self.gameDisplay,
                                     self.red, (700, 280, 80, 40))
                    self.message("Stop", (700+(80/2)),
                                 (280+(40/2)), self.smallText)
                self.message("Flappy Bird", 300, 300, self.font)
                pygame.display.update()
                self.clock.tick(80)

    def reset(self):
        self.message('Game Over', (self.dis_w*0.5),
                     (self.dis_h*0.4), self.font)
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(self.die)
        time.sleep(1)
        for i in self.lists:
            i.kill()
        Game.score = 0
        self.x_change = 5
        self.y_change = 0
        pygame.display.update()
        self.start()

    def gameloop(self):
        self.Exit = False
        self.x = (self.dis_w*0)
        self.y = (self.dis_h*0.5)
        self.xx = 0
        while not self.Exit:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.bi(self.background, 0, 0)
            if self.xx % 80 == 40 or self.xx == 0:
                self.chh = random.randrange(2)
                if self.chh == 1:
                    ob = objects(self.thing1)
                if self.chh == 0:
                    ob = objects(self.thing2)
                ob.rect.x, ob.rect.y = self.things1()
                # creating list of instance(images) of objects class and adding to list
                self.lists.add(ob)
            self.xx += 1
            self.lists.draw(self.gameDisplay)
            self.lists.update()
            self.bi(self.bird, self.x, self.y)

            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_SPACE:
                    self.y_change = -20

            if self.event.type == pygame.KEYUP:
                self.y_change = 6

            if self.x == 500:
                self.x_change = 0
            else:
                self.x_change = 5

            self.x += self.x_change
            self.y += self.y_change

            if self.y < self.dis_h-self.bird_h and self.y < -20:
                self.reset()

            if self.y > self.dis_h-self.bird_h:
                self.reset()

            for i in self.lists:
                if self.x > i.rect.x+7 and self.x < i.rect.x+52:
                    if i.rect.y == -30:
                        if self.y > 0 and self.y <= 290:
                            self.reset()
                    elif i.rect.y == 400:
                        if self.y >= 400:
                            self.reset()

            self.message(str(self.score), 50, 50, self.font)
            pygame.display.update()
            self.clock.tick(80)
# Child class of Game class and PyGame Sprite to move objects


class objects(pygame.sprite.Sprite, Game):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.load(image)

    def load(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        pygame.display.update()

    def update(self):
        if Game.score > 10:
            self.rect.x -= 15
        elif Game.score > 20:
            self.rect.x -= 20
        elif Game.score > 30:
            self.rect.x -= 25
        elif Game.score > 40:
            self.rect.x -= 30
        else:
            self.rect.x -= 8
        if self.rect.x < -50:
            pygame.mixer.Sound.play(Game.point)
            Game.score += 1
            pygame.display.update()
            self.kill()
        pygame.display.update()


game = Game()
game.start()
pygame.quit()
quit()
