import pygame
import sys
import  random
import time
up=(0,-1)
down=(0,1)
right=(1,0)
left=(-1,0)
file = 'explosion_sound.mp3'
winner= 'winner_music.mp3'
pygame.init()
pygame.mixer.init()
shoot_sound=pygame.mixer.Sound(file)
winner_sound=pygame.mixer.Sound(winner)
class Player:
    def __init__(self, sprite,size,x,y,name,id):
        self.sprite=pygame.image.load(sprite)
        self.surface=self.sprite
        self.size=size
        self.direction=up
        self.bullets=[]
        self.rect=self.sprite.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.last=pygame.time.get_ticks()
        self.reload=1500
        self.hp=3
        self.hp_font=pygame.font.Font("Roboto-Medium.ttf",24)
        self.name=name
        self.id=id

    def draw_tank(self,screen):
        pass
    def show_hp(self):
        show_hp=self.hp_font.render(self.name+" Hp: "+str(self.hp),1,game.black)
        if self.id==1:

            screen.blit(show_hp,(10,10))
        if self.id==2:

            screen.blit(show_hp,(10,700))

    def fire(self):
        now=pygame.time.get_ticks()
        if now-self.last>self.reload:
            new_bullet={
                "rect":pygame.Rect(self.rect.centerx, self.rect.centery,5,5),
                "direction":self.direction}
            self.bullets.append(new_bullet)
            self.last=now
    def bullets_direction(self):
        for projectile in self.bullets:
            projectile["rect"].x+=projectile["direction"][0]*5
            projectile["rect"].y+=projectile["direction"][1]*5
        self.bullets=[p for p in self.bullets if 0<=p["rect"].x<=screen_width and 0<=p["rect"].y<=screen_height]

    def is_collided_with(self, object):
        return self.rect.colliderect(object)
    def check_collision_with_enemy_bullets(self,bullets_list):
        for bullet in bullets_list:
            if self.is_collided_with(bullet["rect"]):
                bullet["rect"].x=2000
                self.hp-=1
                shoot_sound.play()











class Game:
    def __init__(self):

        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 100, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        self.fps_controller = pygame.time.Clock()
        self.winner=pygame.font.Font("Roboto-Medium.ttf",40)


    def init_and_check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

def finish():
    pygame.quit()
    sys.exit(0)
screen_width = 1000
screen_height = 750
fps=30
screen=pygame.display.set_mode((screen_width,screen_height))



game = Game()
game.init_and_check_for_errors()
pl_1=Player("tank_1.png",30,50,50,input("Player 1: "),1)
pl_2=Player("tank_2.png", 30, 550, 550,input("Player2: "),2)

game.init_and_check_for_errors()


while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pl_1.rect.x+=3
        pl_1.surface=pygame.transform.rotate(pl_1.sprite, -90)
        pl_1.direction=right
    elif keys[pygame.K_a]:
        pl_1.rect.x-=3
        pl_1.surface=pygame.transform.rotate(pl_1.sprite, +90)
        pl_1.direction=left
    elif keys[pygame.K_w]:
        pl_1.rect.y-=3
        pl_1.surface=pygame.transform.rotate(pl_1.sprite, 0)
        pl_1.direction=up

    elif keys[pygame.K_s]:
        pl_1.rect.y+=3
        pl_1.surface=pygame.transform.rotate(pl_1.sprite, -180)
        pl_1.direction=down




    if keys[pygame.K_RIGHT]:
        pl_2.rect.x+=3
        pl_2.surface=pygame.transform.rotate(pl_2.sprite, -90)
        pl_2.direction=right
    elif keys[pygame.K_LEFT]:
        pl_2.rect.x-=3
        pl_2.surface=pygame.transform.rotate(pl_2.sprite, +90)
        pl_2.direction=left
    elif keys[pygame.K_UP]:
        pl_2.rect.y-=3
        pl_2.surface=pygame.transform.rotate(pl_2.sprite, 0)
        pl_2.direction=up
    elif keys[pygame.K_DOWN]:
        pl_2.rect.y+=3
        pl_2.surface=pygame.transform.rotate(pl_2.sprite, -180)
        pl_2.direction=down



    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
           finish()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_f:
            pl_1.fire()



        if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
           pl_2.fire()
    pl_1.check_collision_with_enemy_bullets(pl_2.bullets)
    pl_2.check_collision_with_enemy_bullets(pl_1.bullets)
    pl_1.bullets_direction()
    pl_2.bullets_direction()
    screen.fill(game.green)
    pl_1.show_hp()
    pl_2.show_hp()










    screen.blit(pl_1.surface,pl_1.rect)
    screen.blit(pl_2.surface,pl_2.rect)
    # pl_1.is_collided_with(pl_2.bullets)
    # pl_2.is_collided_with(pl_1.bullets)
    for i in pl_1.bullets:
        pygame.draw.rect(screen,game.red,i["rect"])
    for i in pl_2.bullets:
        pygame.draw.rect(screen,game.red,i["rect"])

    if pl_1.hp==0:
        pl_1.rect.x=10000
        screen.fill(game.black)
        winner=game.winner.render(pl_2.name+" won",1,game.red)
        screen.blit(winner,(screen_width/2-75,screen_height/2-50))
        winner_sound.play()
    if pl_2.hp==0:
        pl_2.rect.x=10000
        screen.fill(game.black)
        winner=game.winner.render(pl_1.name+" won",1,game.red)
        screen.blit(winner,(screen_width/2-75,screen_height/2-50))
        winner_sound.play()


    pygame.display.update()


