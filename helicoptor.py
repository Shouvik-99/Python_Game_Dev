import pygame
import random
import time
pygame.init()
max_score=0
crash_sound=pygame.mixer.Sound('Crash1.wav')
pygame.mixer.music.load('heli_sound.wav')
width=800
height=300
Display=pygame.display.set_mode((width,height))
pygame.display.set_caption("PILOT FANTASY")
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
violet=(155,0,255)
clock=pygame.time.Clock()
gamequit=False
heli1=pygame.image.load('heli-1.png')
heli2=pygame.image.load('heli-2.png')
heli3=pygame.image.load('heli-3.png')
heli4=pygame.image.load('heli-4.png')
def score_count(count):
    font=pygame.font.SysFont(None,25)
    text=font.render('SCORE:{}'.format(count),True,black)
    Display.blit(text,(10,10))
def show_maxscore(max_score,score):
    if max_score==score:
        font=pygame.font.SysFont(None,25)
        text=font.render('MAX SCORE:{}'.format(score),True,violet)
        Display.blit(text,(250,0))
    else:
        font=pygame.font.SysFont(None,25)
        text=font.render('MAX SCORE:{}'.format(max_score),True,violet)
        Display.blit(text,(250,0))    
def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    display_message('GAME OVER')
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                game_loop()
            if event.key==pygame.K_DOWN:
                    pygame.quit()
                    quit()
        elif event.type==pygame.QUIT:
            pygame.quit()
            quit()
def text_objects(text,font):
    textSurface=font.render(text,True,red)
    return textSurface,textSurface.get_rect()
def display_message(text):
    largeText=pygame.font.Font('freesansbold.ttf',85)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=(int((width/2)),int((height/2)))
    Display.blit(TextSurf,TextRect)
def blocks(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(Display,color,[blockx,blocky,blockw,blockh])
def game_loop():
    global max_score
    pygame.mixer.music.play(-1)
    x=100
    y=height-200
    v_up=0
    v_down=0
    block_startx=width+100
    block_starty=random.randrange(0,height)
    block_speed=2
    block_width=40
    block_height=120
    currentimage=1
    heliheight=29
    heliwidth=80
    score=0
    while not gamequit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit==True
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                v_down=2
                if event.key==pygame.K_UP:
                    v_up=-4   
            elif event.type==pygame.KEYUP:
                v_up=0
                v_down=2
        #Display.fill(white)        
        '''if y>height-29:
            v_down=0
            block_speed=0
            v_up=0
            crash()'''
        if y<0:
            v_up=0
        y=y+v_up+v_down
        Display.fill(white)
        if currentimage==1:
            Display.blit(heli1,(x,y))
            currentimage+=1
        elif currentimage==2:
            Display.blit(heli2,(x,y))
            currentimage+=1
        elif currentimage==3:
            Display.blit(heli3,(x,y))
            currentimage+=1
        elif currentimage==4:
            Display.blit(heli4,(x,y))
            currentimage=1    
        if block_startx==-10:
            score+=1
            #max_score+=1
            block_startx=width+100
            block_starty=random.randrange(0,height)
        #Display.fill(white)    
        block_startx=block_startx-block_speed
        blocks(block_startx,block_starty,block_width,block_height,black)
        if y>height-29:
            block_speed=0
            v_down=0
            v_up=0
            crash()
            if score>max_score:
                max_score=score
            show_maxscore(max_score,score)
        score_count(score)
        #y+heliheight>block_starty and y+heliheight<block_starty+block_height
        #y>block_starty and y+heliheight< block_starty+block_height
        if (0) or (y>block_starty and y<block_starty+block_height) or (0):
            if x+heliwidth>=block_startx and x<=block_startx+block_width:
                block_speed=0
                v_down=0
                v_up=0
                crash()
                if score>max_score:
                    max_score=score
                show_maxscore(max_score,score)
        pygame.display.update()
        clock.tick(201)
game_loop()
