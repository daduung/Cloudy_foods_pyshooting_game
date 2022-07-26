import random
from time import sleep
from tkinter import BOTTOM, CENTER
from turtle import speed
import pygame
from pygame.locals import *

# 윈도우 크기 설정 : 원하는 크기로 변경 가능
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (250,250,50)
RED = (250,50,50)

#Frame per seconds : 1초에 몇개 읽냐
FPS = 60

        
        
#전투기 만들기
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Fighter, self).__init__()
        self.image = pygame.image.load('character.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(WINDOW_WIDTH /2)
        self.rect.y = int(WINDOW_HEIGHT - self.rect.height)
        self.dx = 0 
        self.dy = 0 
        
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        if self.rect.x < 0 or self.rect.x + self.rect.width > WINDOW_WIDTH :
            self.rect.x -= self.dx
        if self. rect.y < 0 or self.rect.y + self.rect.height > WINDOW_HEIGHT:
            self.rect.y -= self.dy
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)     
    
    # 충돌    
    def collide(self, sprites) :
        for sprite in sprites :
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
# # 보스 만들기
# class Boss(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Boss, self).__init__()
#         self.image = pygame.image.load('machine.png')
#         self.rect= self.image.get_rect()
#         self.rect.x= int(WINDOW_WIDTH / 3)
#         self.rect.y= 0
    
#     def draw(self, screen):
#         screen.blit(self.image, self.rect) 
        
#     # 충돌    
#     def collide(self, sprites) :
#         for sprite in sprites :
#             if pygame.sprite.collide_rect(self, sprite):
#                 return sprite
      

# 미사일 만들기
class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Missile, self).__init__()
        self.image = pygame.image.load('ketchup.png')
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
        self.sound = pygame.mixer.Sound('missile0.mp3')
    
    def launch(self):   
        self.sound.play()
        
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0 :
            self.kill()
    
    def collide(self, sprites):
        for sprite in sprites :
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

#레이저 만들기
class Laser(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Laser, self).__init__()
        self.image = pygame.image.load('Laser.png')
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = xpos
        self.rect.y = ypos
        #self.sound = pygame.mixer.Sound('missile0.mp3')
    
    #def launch(self):   
    #    self.sound.play()
        
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0 :
            self.kill()
    
    def collide(self, sprites):
        for sprite in sprites :
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

# 보스
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.image = pygame.image.load('boss.png')
        self.rect= self.image.get_rect()
        self.rect.x= 15
        self.rect.y= 30
    
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    # 충돌    
    def collide(self, sprites) :
        for sprite in sprites :
            if pygame.sprite.collide_rect(self, sprite):
                return sprite


# 음식 떨어지기
class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed) :
        super(Rock, self).__init__()
        rock_images = ('food1.png','food2.png','food3.png','food4.png','food5.png','food6.png','food7.png',
                       'food8.png','food9.png','food10.png','food11.png','food12.png','food14.png',
                       'food15.png','food16.png','food17.png','food18.png','food19.png','food20.png','food21.png',
                       'food22.png','food23.png','food24.png','food25.png','food26.png','food27.png','food28.png',
                       'food29.png','food30.png','food31.png','food32.png','food33.png','food34.png','food35.png',
                       'food36.png','food37.png','food38.png','food39.png','food40.png','food41.png','food42.png')
        
        self.image = pygame.image.load(random.choice(rock_images))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
    
    def update(self):
        self.rect.y += self.speed
        
    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT :
            return True
    
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect) #화면에 구현

#아이템
class Item(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, speed):
        super(Item, self).__init__()
        self.image = pygame.image.load('item.png')
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.speed = speed
    
    def update(self):
        self.rect.y += self.speed

    def out_of_screen(self):
        if self.rect.y > WINDOW_HEIGHT:
            return True

    def collide(self, sprites):
        for sprite in sprites :
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
       
# 폭발이미지
def occur_explosion(surface, x, y):
    explosion_image = pygame.image.load("explosion.png")
    explosion_rect = explosion_image.get_rect()
    explosion_rect.x = x
    explosion_rect.y = y
    surface.blit(explosion_image, explosion_rect)
    
    explosion_sounds = ('explosion0.mp3')    
    #explosion_sound = pygame.mixer.Sound(random.choice(explosion_sounds))    
    explosion_sound = pygame.mixer.Sound(explosion_sounds)    
    explosion_sound.play()

# 게임 오버 이미지
def occur_gameover(surface,x,y):
    gameover_image = pygame.image.load('gameover.png')
    gameover_rect = gameover_image.get_rect()
    gameover_rect.x = x
    gameover_rect.y = y
    surface.blit(gameover_image, gameover_rect)
    
    #gameover_sounds = ('gameover0.mp3')    
    #gameover_sound = pygame.mixer.Sound(random.choice(gameover_sounds))    
    #gameover_sound = pygame.mixer.Sound(gameover_sounds)    
    #gameover_sound.play()
    
# 승리 이미지
def occur_youwin(surface,x,y):
    youwin_image = pygame.image.load('youwin.png')
    youwin_rect = youwin_image.get_rect()
    youwin_rect.x = x
    youwin_rect.y = y
    surface.blit(youwin_image, youwin_rect)
    
def game_loop() :
    default_font = pygame.font.Font('MapoHongdaeFreedom.ttf', 28)
    background_image = pygame.image.load('background01.png')        
    gameover_sound = pygame.mixer.Sound('gameover.wav')    
    youwin_sound=pygame.mixer.Sound('youwin.wav')
    pygame.mixer.music.load('BGM2.mp3')
    pygame.mixer.music.play(-1) #무한반복
    fps_clock = pygame.time.Clock()
    life=pygame.image.load('life3.png')

    fighter = Fighter()
    boss = Boss()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    items = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    occur_prob = 40  #rpod
    shot_count = 0
    count_missed = 0
    shot_count_boss=0
    
    done = False
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    fighter.dx -=5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx +=5
                elif event.key == pygame.K_UP:
                    fighter.dy -=5
                elif event.key == pygame.K_DOWN:
                    fighter.dy +=5
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx, fighter.rect.y, 10) #미사일 나가는 속도 : speed=10
                    missile.launch()
                    missiles.add(missile)
            if event.type == pygame.KEYUP: #방향키에서 손을 뗐을 때
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighter.dx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighter.dy = 0
                       
        screen.blit(background_image, background_image.get_rect())
        screen.blit(life,life.get_rect())

        # 돌을 맞추면 암석이 점점 많이 등장하게
        occur_of_rocks = 1 + int(shot_count / 50)

        # 운석 스피드가 점점 올라가게                
        min_rock_speed = 1 + int(shot_count / 50)
        max_rock_speed = 1 + int(shot_count / 20)

        # 아이템 등장
        occur_of_items = 1 + int(shot_count / 500)
        
        min_item_speed = 1 + int(shot_count / 200)
        max_item_speed = 1 + int(shot_count / 100)
        
        # 보스 등장
        occur_of_boss= int(shot_count / 75)
        
        if random.randint(1, occur_prob) ==1:
            for i in range(occur_of_rocks): # 운석생성
                speed = random.randint(min_rock_speed, max_rock_speed)
                rock = Rock(random.randint(0,WINDOW_WIDTH - 30), 0, speed) #운석이 윈도우 끝에 있으면 안보이니까 -30해서 이동시킨 것.
                rocks.add(rock)
        draw_text('파괴한 음식: {}'.format(shot_count), default_font, screen, 380, 20, YELLOW)

        if random.randint(1, occur_prob+300) ==1:
            for i in range(occur_of_items): # 아이템생성
                speed = random.randint(min_item_speed, max_item_speed)
                item = Item(random.randint(0,WINDOW_WIDTH - 30), 0, speed)
                items.add(item)
       
        for missile in missiles:
            rock = missile.collide(rocks) #미사일을 운석이랑 다 충돌했는지 비교해봐서 충돌했으면 반환을 해주는 것
            if rock:
                missile.kill()
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1

        for laser in lasers:
            rock = laser.collide(rocks) #미사일을 운석이랑 다 충돌했는지 비교해봐서 충돌했으면 반환을 해주는 것
            if rock:
                rock.kill()
                occur_explosion(screen, rock.rect.x, rock.rect.y)
                shot_count += 1
                
        for rock in rocks : 
            if rock.out_of_screen() :
                rock.kill()
                count_missed += 1

        for item in items :
            item = fighter.collide(items)
            if item:
                item.kill()
                laser = Laser(0, 640, 10) #미사일 나가는 속도 : speed=10
                lasers.add(laser)
 
        if occur_of_boss >=1:
            boss.draw(screen)
            draw_text('보스체력: {}'.format(25 - shot_count_boss), default_font, screen, 380, 60, RED)
            if boss.collide(missiles):
                    missile.kill()
                    occur_explosion(screen, boss.rect.x, boss.rect.y)
                    shot_count_boss +=1
                    
                    if shot_count_boss == 25:
                        missile.kill()
                        boss.kill()
                        pygame.mixer_music.stop()
                        occur_explosion(screen, boss.rect.x, boss.rect.y)
                        occur_youwin(screen, 0, 0)
                        pygame.display.update()
                        youwin_sound.play()
                        sleep(2)
                        done = True

        rocks.update()
        rocks.draw(screen)
        missiles.update()
        missiles.draw(screen)
        fighter.update()
        fighter.draw(screen)
        items.update()
        items.draw(screen)
        lasers.update()
        lasers.draw(screen)
        pygame.display.flip()
        
        if count_missed == 1:
            life = pygame.image.load('life2.png')
            screen.blit(life, life.get_rect())
        
        if count_missed == 2:
            life = pygame.image.load('life.png')
            screen.blit(life, life.get_rect())
        
        # 3번 운석이 떨어지면 게임 끝나도록 설정 (목숭3개)
        if fighter.collide(rocks) or count_missed >= 3:
            pygame.mixer_music.stop()
            occur_explosion(screen, fighter.rect.x, fighter.rect.y)
            occur_gameover(screen, 0, 0)
            pygame.display.update()
            gameover_sound.play()
            sleep(2)
            done = True
            
        fps_clock.tick(FPS)
        
        if shot_count== 25:
            background_image = pygame.image.load('background02.png')
            screen.blit(background_image, background_image.get_rect())

        if shot_count== 45:
            background_image = pygame.image.load('background03.png')
            screen.blit(background_image, background_image.get_rect())

        if shot_count== 75:
            background_image = pygame.image.load('background04.png')
            screen.blit(background_image, background_image.get_rect())
        
    return 'game_menu'
              
        
# 시작화면        
def game_menu():
    start_image = pygame.image.load('background0.png')
    screen.blit(start_image, [0,0]) 
    draw_x = int(WINDOW_WIDTH/2)      
    draw_y = int(WINDOW_HEIGHT/4)
    font_50 = pygame.font.Font('MapoHongdaeFreedom.ttf', 50)      
    font_30 = pygame.font.Font('MapoHongdaeFreedom.ttf', 30)
    font_20 = pygame.font.Font('MapoHongdaeFreedom.ttf', 20)
      
    draw_text('하늘에서 음식이', font_50, screen, draw_x, draw_y-50, RED)
    draw_text('내린다면', font_50, screen, draw_x, draw_y, RED)
    draw_text('...', font_30, screen, draw_x, draw_y +30, RED)
    draw_text('비정상적으로 커진', font_20, screen, draw_x, draw_y +80, BLACK)
    draw_text('음식들과 음식 복사기를 파괴하고', font_20, screen, draw_x+10, draw_y +110, BLACK)
    draw_text('지구를 구하라!', font_20, screen, draw_x, draw_y +140, BLACK)
    draw_text('엔터 키를 누르면', font_30, screen, draw_x, draw_y+200, WHITE)
    draw_text('게임이 시작됩니다', font_30, screen, draw_x, draw_y +240, WHITE)
       
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'play'
        if event.type == QUIT :
            return 'quit'
    
    return 'game_menu'
        
def main():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
    pygame.display.set_caption('하늘에서 음식이 내린다면')       #제목주기
    
    action = 'game_menu'
    while action != 'quit' :
        if action == 'game_menu':
            action = game_menu()
        elif action == 'play':
            action = game_loop()
            
    pygame.quit()


if __name__ == "__main__" : 
    main()        
        
        
# ctrl+shift+F10





 















