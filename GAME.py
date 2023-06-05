import pygame, sys,random,time,os,shelve
from pygame.locals import *

pygame.init()

GAMEWINDOW = pygame.display.set_mode((400, 600),0,32)
pygame.display.set_caption('Rapid Roll')

Black=( 0, 0, 0)
Green=( 0, 128, 0)
Red=(255, 0, 0)
WHITE = (255, 255, 255)
Blue=(0,0,255)
FPS=150
fpsClock = pygame.time.Clock()

thornImg = pygame.image.load('imgs/thorn.png')
plankImg = pygame.image.load('imgs/plank.png')
thornplankImg = pygame.image.load('imgs/thornplank.png')
ballImg = pygame.image.load('imgs/ball.png')
lifeplankImg=pygame.image.load('imgs/lifeplank.png')
playImg=pygame.image.load('imgs/play.png')
highscorebgImg=pygame.image.load('imgs/highscorebg.png')
difficultyImg=pygame.image.load('imgs/difficulty.png')
playagainImg=pygame.image.load('imgs/playagain.png')
gameoverImg=pygame.image.load('imgs/gameover.png')
quitImg=pygame.image.load('imgs/quit.png')
escapeImg=pygame.image.load('imgs/escape.png')
helpImg=pygame.image.load('imgs/HOW TO PLAY.png')
elixrImg=pygame.image.load('imgs/xp elixr.png')
shortplankImg=pygame.image.load('imgs/shortplank.png')
shieldImg=pygame.image.load('imgs/shield.png')
lifeballImg=pygame.image.load('imgs/lifeball.png')

life=4
speed=0
mode='EASY'

class plank():
    def __init__(self):
        self.x=random.randint(0,350)

    def plank_moving_up(self,speed):
        self.y-=(0.5+speed)

    def relocating_plank(self):
        if self.y<20:
            self.y=600
            self.x=random.randint(0,350)
    def ball_on_planks(self,speed,score):
        if score<200:
         if ball.y+24<self.y+2 and ball.y+24>self.y-2 and ball.x>self.x-25 and ball.x<self.x+50:
           ball.y=ball.y-(1.5+speed)
        
        if score>200:
          if ball.y+24<self.y+2 and ball.y+24>self.y-2 and ball.x>self.x-20 and ball.x<self.x+35:
           ball.y=ball.y-(1.5+speed)
class ball():
    def __init__(self):
        self.Img= pygame.image.load('imgs/ball.png')
        self.y=455
        self.x=plank5.x+15
        self.shield=False

    def ball_life_lost(self,life):
       if ball.shield==False:   
        time.sleep(0.5)
        self.y=200
        self.x=random.randint(0,400)                             
        life=life-1
        return life
       if ball.shield==True:
        time.sleep(0.5)
        self.y=200
        self.x=random.randint(0,400)
        ball.shield=False
        ball.Img= pygame.image.load('imgs/ball.png')
        return life
              
plank1=plank()
plank2=plank()
plank3=plank()
plank4=plank()
plank5=plank()
plank6=plank()
plank7=plank()
plank8=plank()
plank9=plank()
plank10=plank()

ball=ball()

def initialize():
 plank1.y=60
 plank2.y=120
 plank3.y=180
 plank4.y=240
 plank5.y=300
 plank6.y=360
 plank7.y=840
 plank9.y=480
 plank10.y=540
 plank8.y=random.randint(3000,5000)
 ball.x=plank9.x+15
 start=0
 score=0
 scorecount=0
 x_change = 0
 speed=0
 x=y=0
 xpos=ypos=0
 difficulty_click=False
 highscore_click=False
 ball_on_plank=True
 playagain=False
 main_menu=False
 life_increased=False
 play=True
 coin_reached=False

 d = shelve.open('score.txt')
 highscore=high1 = d['score1']
 high2 = d['score2']
 high3 = d['score3']
 high4 = d['score4']
 high5 = d['score5']
 xp = d['xp']
 d.close()

 input1=xp
 lvl=1
 increment=500
 target=increment
 for x in range (input1+1):
     if x==target:
      lvl+=1
      increment+=500
      target+=increment

 target-=increment
 progress=input1-target
 if progress==increment:
    progress=0
 level_target=increment

 progress_perc=(progress/level_target)*100
  
 return  start,score,scorecount,x_change,ball_on_plank,life_increased,play,x,y,xpos,ypos,difficulty_click,highscore_click,highscore,high1,high2, high3,high4,high5,playagain,main_menu,xp,lvl,progress, level_target,progress_perc,coin_reached

def terminate():
    while True:
       GAMEWINDOW.blit(quitImg,(0,0))
       pygame.display.update()    
       event = pygame.event.wait()  

       if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
          x1pos,plank1.ypos=event.pos
          if x1pos>65  and x1pos<130 and plank1.ypos>330 and plank1.ypos<380 :
            pygame.quit()
            sys.exit()
          if x1pos>200  and x1pos<330 and plank1.ypos>330 and plank1.ypos<380 :
             break 

def showlife(life):
 if life>=1:
  GAMEWINDOW.blit(lifeballImg,(360,2))
 if life>=2:
  GAMEWINDOW.blit(lifeballImg,(340,2))
 if life>=3:
  GAMEWINDOW.blit(lifeballImg,(320,2))
 if life>=4:
  GAMEWINDOW.blit(lifeballImg,(300,2))
 if life>=5:
  GAMEWINDOW.blit(lifeballImg,(280,2))
 if life>=6:
  GAMEWINDOW.blit(lifeballImg,(260,2))  

def shield(shield_reached):
  if score>200:
      shield_relocation=-15
  else:
      shield_relocation=0
 
  if shield_reached==False:
       GAMEWINDOW.blit(shieldImg,(plank8.x+15+shield_relocation,plank8.y-20))
  if ball.y+24<plank8.y+2 and ball.y+24>plank8.y-2 and ball.x>plank8.x-25 and ball.x<plank8.x+50 and shield_reached==False:
      shield_reached=True
      ball.shield=True
      ball.Img=pygame.image.load('imgs/shieldball.png')
  if plank1.y<20.5:
      shield_reached=False

  return shield_reached
def blitting():

   GAMEWINDOW.blit(ball.Img,(ball.x,ball.y))                    
   GAMEWINDOW.blit(thornImg,(0,20))
   GAMEWINDOW.blit(plankImg,(plank1.x,plank1.y))
   GAMEWINDOW.blit(plankImg,(plank2.x,plank2.y))
   GAMEWINDOW.blit(plankImg,(plank3.x,plank3.y))                         
   GAMEWINDOW.blit(plankImg,(plank4.x,plank4.y))
   GAMEWINDOW.blit(plankImg,(plank5.x,plank5.y))
   GAMEWINDOW.blit(thornplankImg,(plank6.x,plank6.y))
   GAMEWINDOW.blit(plankImg,(plank8.x,plank8.y))
   GAMEWINDOW.blit(plankImg,(plank9.x,plank9.y))
   GAMEWINDOW.blit(thornplankImg,(plank10.x,plank10.y))   

   if life_increased==False:
    GAMEWINDOW.blit(lifeplankImg,(plank7.x,plank7.y))
   if life_increased==True:
    GAMEWINDOW.blit(plankImg,(plank7.x,plank7.y+25))
  
   obj = pygame.font.Font('freesansbold.ttf',54)            
   surf1 = obj.render(' %s...'%int(1),True,Red)
   surf2 = obj.render(' %s...'%int(2),True,Red)
   surf3 = obj.render(' %s...'%int(3),True,Red)

   if start<140:
         GAMEWINDOW.blit(surf3,(150,250))
   if start<299 and start>140:      
         GAMEWINDOW.blit(surf2,(150,250))
   if start<500 and start>300:
         GAMEWINDOW.blit(surf1,(150,250))

def showscore(scorecount,start,score):
    
   obj = pygame.font.Font('freesansbold.ttf',14)            
   surf = obj.render('SCORE: %s'%int(score),True,(0,0,0))
   GAMEWINDOW.blit(surf,(10,2))

def plankcontrols(speed,start):
    plank1.plank_moving_up(speed)
    plank2.plank_moving_up(speed)
    plank3.plank_moving_up(speed)
    plank4.plank_moving_up(speed)
    plank5.plank_moving_up(speed)
    plank6.plank_moving_up(speed)
    plank7.plank_moving_up(speed)
    plank8.plank_moving_up(speed)
    plank9.plank_moving_up(speed)
    plank10.plank_moving_up(speed)
    return speed,start 

def plank_relocation(speed,life,life_increased):
   plank1.relocating_plank()
   plank2.relocating_plank()
   plank3.relocating_plank()
   plank4.relocating_plank()
   plank5.relocating_plank()
   plank6.relocating_plank()
   plank9.relocating_plank()
   plank10.relocating_plank()

   if plank8.y<20.1:
    plank8.y=6000+(speed*10)
    plank8.x=random.randint(0,350)    

   if plank7.y<20 and life<6:
    plank7.y=2000+(speed*10)
    plank7.x=random.randint(0,350)
    life_increased=False

   return speed,life,life_increased     

def ball_controls(scorecount,life):

   ball.y=ball.y+1                                                

   if ball.y>800:
      life=ball.ball_life_lost(life)   
     
   if ball.y<50:
      life=ball.ball_life_lost(life) 

   return scorecount,life 
  
def if_ball_is_on_the_plank(speed,life,life_increased,scorecount,ball_on_plank,score ):

   if (ball.y+24<plank1.y+2 and ball.y+24>plank1.y-2 and ball.x>plank1.x-25 and ball.x<plank1.x+50) :   
       ball_on_plank=True
   elif (ball.y+24<plank2.y+2 and ball.y+24>plank2.y-2 and ball.x>plank2.x-25 and ball.x<plank2.x+50):
       ball_on_plank=True 
   elif (ball.y+24<plank3.y+2 and ball.y+24>plank3.y-2 and ball.x>plank3.x-25 and ball.x<plank3.x+50):
       ball_on_plank=True
   elif (ball.y+24<plank4.y+2 and ball.y+24>plank4.y-2 and ball.x>plank4.x-25 and ball.x<plank4.x+50):
       ball_on_plank=True
   elif (ball.y+24<plank5.y+2 and ball.y+24>plank5.y-2 and ball.x>plank5.x-25 and ball.x<plank5.x+50):
       ball_on_plank=True
   elif (ball.y+24<plank8.y+2 and ball.y+24>plank8.y-2 and ball.x>plank8.x-25 and ball.x<plank8.x+50):
       ball_on_plank=True       
   elif (ball.y+24<plank9.y+2 and ball.y+24>plank9.y-2 and ball.x>plank9.x-25 and ball.x<plank9.x+50):
       ball_on_plank=True       
   
   elif (ball.y<plank7.y+2 and ball.y>plank7.y-2 and ball.x>plank7.x-25 and ball.x<plank7.x+50):
       ball_on_plank=True
   else:
       ball_on_plank=False

   
   plank1.ball_on_planks(speed,score)
   plank2.ball_on_planks(speed,score)
   plank3.ball_on_planks(speed,score)
   plank4.ball_on_planks(speed,score)
   plank5.ball_on_planks(speed,score)
   plank8.ball_on_planks(speed,score)
   plank9.ball_on_planks(speed,score)
   
   if (ball.y+18<plank6.y+2 and ball.y+18>plank6.y-2 and ball.x>plank6.x-25 and ball.x<plank6.x+50) or (ball.y+18<plank10.y+2 and ball.y+18>plank10.y-2 and ball.x>plank10.x-25 and ball.x<plank10.x+50):
      life=ball.ball_life_lost(life)
      if (ball.x>plank6.x-25 and ball.x<plank6.x+50) or (ball.x>plank10.x-25 and ball.x<plank10.x+50):
        ball.x=random.randint(0,400)
   if score<200:      
    if ball.y<plank7.y+2 and ball.y>plank7.y-2 and ball.x>plank7.x-25 and ball.x<plank7.x+50:

      if life_increased==False and ball.y<plank7.y+2 and ball.y>plank7.y-2 and ball.x>plank7.x-10 and ball.x<plank7.x+35:
        life=life+1
        life_increased=True
      ball.y=ball.y-(1.5+speed)  

   if score>200:
    if ball.y<plank7.y+2 and ball.y>plank7.y-2 and ball.x>plank7.x-25 and ball.x<plank7.x+25:
     ball.y=ball.y-(1.5+speed)  
     if life_increased==False:
      life=life+1
      life_increased=True
   return speed,life,life_increased,scorecount,ball_on_plank  

def key_controls(start,speed,x_change,main_menu):
   for event in pygame.event.get():
    if event.type == QUIT:
     terminate()
          
    if event.type == pygame.KEYDOWN and start>500:
     if event.key == pygame.K_LEFT:
        x_change = -(0.5+speed)
     elif event.key == pygame.K_RIGHT and start>500:
         x_change = 0.5+speed
     if event.key == pygame.K_ESCAPE:
         while True:
             GAMEWINDOW.blit(escapeImg,(0,0))
             pygame.display.update()
             event = pygame.event.wait()  

             if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:

               x2pos,plank2.ypos=event.pos

               if x2pos>115  and x2pos<290 and plank2.ypos>160 and plank2.ypos<210 :
                   break

               if x2pos>140  and x2pos<250 and plank2.ypos>380 and plank2.ypos<430 :
                   terminate()

               if x2pos>75  and x2pos<340 and plank2.ypos>265 and plank2.ypos<325 :
                   time.sleep(0.5)
                   main_menu=True
                   break
                   
    if event.type == pygame.KEYUP:
     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:                       
         x_change = 0
        
   ball.x += x_change
   if ball.x<0:
     ball.x=0
   if ball.x>375:
     ball.x=375
            
   GAMEWINDOW.blit(ball.Img, (ball.x,ball.y))
   pygame.display.update()
   return start,speed,x_change,main_menu


def display_final_score(score,playagain,xp):
   ball.y=455
   ball.x=plank5.x+15
   for j in range(200):
       GAMEWINDOW.blit(gameoverImg,(0,0))
       j+=1
       pygame.display.update()
       
   xp=xp+score
   d = shelve.open('score.txt')
   d['xp']=xp
   d.close()
   endscore=score

   if endscore>highscore:
    d = shelve.open('score.txt')  
    d['score'] = endscore           
    d.close()

   for i in range (500):

      GAMEWINDOW.blit(playagainImg,(0,0))   
      i+=1
      if endscore>highscore:
          obj = pygame.font.Font('freesansbold.ttf',40)                                  
          surf = obj.render('NEW HIGH SCORE ',True,Black)
          GAMEWINDOW.blit(surf,(30,100))
           
      obj = pygame.font.Font('freesansbold.ttf',30)                                  
      surf = obj.render('YOUR SCORE IS: %s'%int(score),True,Black)
      GAMEWINDOW.blit(surf,(50,200))

      obj = pygame.font.Font('freesansbold.ttf',20)                                  
      surf = obj.render('YOUR PREVIOUS HIGH SCORE: %s'%int(highscore),True,Black)
      GAMEWINDOW.blit(surf,(30,300))

      if i>20:
       event = pygame.event.wait()  

       if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
          x1pos,plank1.ypos=event.pos
          if x1pos>190  and x1pos<400 and plank1.ypos>515 and plank1.ypos<560 :
              playagain=True
          if x1pos>300  and x1pos<370 and plank1.ypos>575 and plank1.ypos<600 :
              terminate()
                           
       if playagain==True:
           return playagain
           break
              
       if event.type == pygame.QUIT:
          terminate()
          
      pygame.display.update()
  
         
def score_increment_rate(score,mode):
        if mode=='EASY':
         score=score+1
        if mode=='MEDIUM':
         score=score+2
        if mode=='HARD':
         score=score+3
        if mode=='NIGHTMARE':
         score=score+4
        return score       
def increments(speed,start,scorecount,score,ball_on_plank,mode):
      
     if scorecount%1000==0:                                        
       speed=speed+0.1
     start+=1
     scorecount+=1

     if score>=0 and score<=100:
      if scorecount%20==0 and start>500 and ball_on_plank==False:
          score=score_increment_rate(score,mode)
     
     if score>=100 and score<=200:
      if scorecount%17==0 and start>500 and ball_on_plank==False:
          score=score_increment_rate(score,mode)

     if score>=200 and score<=300:  
      if scorecount%15==0 and start>500 and ball_on_plank==False:
          score=score_increment_rate(score,mode)

     if score>=300 and score<=400:
      if scorecount%12==0 and start>500 and ball_on_plank==False:
         score=score_increment_rate(score,mode)

     if score>=400 and score<=500:
      if scorecount%10==0 and start>500 and ball_on_plank==False:
         score=score_increment_rate(score,mode)
     
     if score>=500:
      if scorecount%8==0 and start>500 and ball_on_plank==False:
         score=score_increment_rate(score,mode)
       
     return speed,start,scorecount,score,ball_on_plank
  
def show_difficulty(x,y,speed,difficulty_click,event,mode):
    while play:

        speed=0
        GAMEWINDOW.blit(difficultyImg,(0,0))
        if event.type == pygame.QUIT:
          terminate()
        event = pygame.event.wait()  

        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
          xpos,ypos=event.pos
          if xpos>120  and xpos<240 and ypos>100 and ypos<150 :
              speed+=0
              difficulty_click=True
              mode='EASY'
          if xpos>80  and xpos<290 and ypos>225 and ypos<275 :
              speed+=0.5
              difficulty_click=True
              mode='MEDIUM'
          if xpos>110  and xpos<250 and ypos>335 and ypos<385 :
              speed+=1
              difficulty_click=True
              mode='HARD'
          if xpos>50  and xpos<330 and ypos>450 and ypos<510 :
              speed+=1.5
              difficulty_click=True
              mode='NIGHTMARE'
          if xpos>320  and xpos<390 and ypos>550 and ypos<575 :
              difficulty_click=True 
        pygame.display.update()

        if difficulty_click==True:
            x=y=0
            break

    return x,y,speed,difficulty_click,event,mode

def update_highscore(score):
 d = shelve.open('score.txt')
 highscore1 = d['score1']
 highscore2 = d['score2']
 highscore3 = d['score3']
 highscore4 = d['score4']
 highscore5 = d['score5']
 d.close()
 endscore=score

 highscore_arrange=[highscore1,highscore2,highscore3,highscore4,highscore5,endscore]
 highscore_arrange.sort()
 highscore_arrange.reverse()
 highscore_arrange.pop(5)

 high1=highscore_arrange[0]
 high2=highscore_arrange[1]
 high3=highscore_arrange[2]
 high4=highscore_arrange[3]
 high5=highscore_arrange[4]
 
 d = shelve.open('score.txt')    
 d['score1'] = high1           
 d['score2'] = high2           
 d['score3'] = high3          
 d['score4'] = high4          
 d['score5'] = high5           
 d.close() 

def show_highscore (high1,high2,high3,high4,high5,highscore_click,x,y):
 while True:
     
  GAMEWINDOW.blit(highscorebgImg,(0,0))
  obj = pygame.font.Font('freesansbold.ttf',40)                                  

  surf = obj.render('1. %s'%int(high1),True,Black)
  GAMEWINDOW.blit(surf,(30,100))

  surf = obj.render('2. %s'%int(high2),True,Black)
  GAMEWINDOW.blit(surf,(30,200))

  surf = obj.render('3. %s'%int(high3),True,Black)
  GAMEWINDOW.blit(surf,(30,300))

  surf = obj.render('4. %s'%int(high4),True,Black)
  GAMEWINDOW.blit(surf,(30,400))

  surf = obj.render('5. %s'%int(high5),True,Black)
  GAMEWINDOW.blit(surf,(30,500))

  obj = pygame.font.Font('freesansbold.ttf',20)
  surf = obj.render('BACK',True,Black)
  GAMEWINDOW.blit(surf,(300,550))

  event = pygame.event.wait()
  if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
   x,y=event.pos
   if x>300 and x<350 and y>550 and y<570:
       highscore_click=True
       x=y=0
       return highscore_click,x,y
  if highscore_click==True:
      pygame.display.update()
      break
       
  pygame.display.update()
  
def Help():
    while True:
        GAMEWINDOW.blit(helpImg,(0,0))
        pygame.display.update()
        event = pygame.event.wait() 
        if event.type == pygame.QUIT:
         terminate()
   
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
         xpos,ypos=event.pos
         pygame.display.update() 

         if xpos>300 and xpos<375 and ypos>570 and ypos<590:
             break
 
#####         MAIN GAME                ######

while life<=6 :
  start,score,scorecount,x_change,ball_on_plank,life_increased,play,x,y,xpos,ypos,difficulty_click,highscore_click,highscore,high1,high2,high3,high4,high5,playagain,main_menu,xp,lvl,progress,level_target,progress_perc,shield_reached=initialize() 

  GAMEWINDOW.blit(playImg,(0,0))

  obj = pygame.font.Font('freesansbold.ttf',15)                                  
  surf = obj.render('%s'%int(lvl),True,Black)
  GAMEWINDOW.blit(surf,(205,15))

  surf = obj.render('%s'%int(progress),True,Black)
  GAMEWINDOW.blit(surf,(290,30))

  surf = obj.render('/',True,Black)
  GAMEWINDOW.blit(surf,(330,30))

  surf = obj.render('%s'%int(level_target),True,Black)
  GAMEWINDOW.blit(surf,(340,30))

  x=212
  for i in range(0,91,10):
      if progress_perc>i:
       GAMEWINDOW.blit(elixrImg,(x,1.5))
      x+=15
  x=212

  pygame.display.update()
  event = pygame.event.wait()
  if event.type == pygame.QUIT:
   terminate()
   
  if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
   x,y=event.pos
   pygame.display.update() 

  if x>310 and x<370 and y>550 and y<575:
     Help() 

  if x>50 and x<320 and y>430 and y<485:
     terminate()

  if x>50 and x<320 and y>260 and y<315:
     x,y,speed,difficulty_click,event,mode=show_difficulty(x,y,speed,difficulty_click,event,mode)        

  if x>50 and x<320 and y>350 and y<400 and highscore_click==False:
     highscore_click,x,y=show_highscore(high1,high2,high3,high4,high5,highscore_click,x,y)

  if x>50 and x<320 and y>160 and y<215:
     
##              THE GAME LOOP              ##
   while life>0 :                                                 
    
    GAMEWINDOW.fill(WHITE) 
      
    speed,start,scorecount,score,ball_on_plank=increments(speed,start,scorecount,score,ball_on_plank,mode)    ##    INCREMENTS       
   
    if start>500:
     speed,start=plankcontrols(speed,start ) ##    PLANK CONTROLS       
                                       
    speed,life,life_increased=plank_relocation(speed,life,life_increased)       ##   PLANK RELOCATION        

    if start>500: 
     scorecount,life=ball_controls(scorecount,life)   ##    BALL CONTROLS         

    blitting()                               ##    BLITTING IMAGES FOR GAME     

    shield_reached=shield(shield_reached)                  ##       SHIELD       

    showscore(scorecount,start,score)     ##         SCORE        
 
    showlife(life)                        ##       LIFE       
 
    speed,life,life_increased,scorecount,ball_on_plank=if_ball_is_on_the_plank(speed,life,life_increased,scorecount,ball_on_plank,score)          ##   BALL  ON PLANK 
    
    start,speed,x_change,main_menu=key_controls(start,speed,x_change,main_menu)         ##     KEY CONTROLS             

    if score<200 :
     plankImg = pygame.image.load('imgs/plank.png')
     lifeplankImg=pygame.image.load('imgs/lifeplank.png')
    if score==200:
     GAMEWINDOW.blit(shortplankImg,(10,50))
     pygame.display.update()
     time.sleep(1)
     score+=1
     plankImg = pygame.image.load('imgs/plank2.png')
     lifeplankImg=pygame.image.load('imgs/lifeplank2.png')
         
    
    if main_menu==True:
        life=2
        ball.y=455
        ball.x=plank5.x+15
        break

    if life<=0:
    
     update_highscore(score) 
     playagain=display_final_score(score,playagain,xp)
     if playagain==True:
          life=2
          speed=0 
          break
     else:   
           pygame.quit()
           sys.exit()
    fpsClock.tick(FPS)
if life>6:
           print('YOU HAVE CHANGED SOME VARIABLE VALUES THE GAME .....PLEASE GO BACK AND CHANGE TO ORIGINAL GAME ')
           pygame.quit()
           sys.exit()

###       END    OF     THE    GAME      CODE  ###
