import pygame
import random
import math
# Initialize Pygame

pygame.init()

#Loading Resources

icon = pygame.image.load('bullet.png')
bullet=pygame.image.load('riflebullet.png')
simo= pygame.image.load('player.png')
russian= pygame.image.load('russian.png')
background = pygame.image.load('snow background.png')


# Define window dimensions and positions

window_width = 800
window_height = 600
playerx=400
playery=500
enemyx=random.randint(50,750)
enemyy=50
bulletx=0
bullety=500
poschange=0
speed=0.5
enemyspeed=4
enemyxchange=5
enemyychange=20
bulletxchange=1
bulletychange=10
bulletstate='ready'
bulletmag=7
scorev=0
font=pygame.font.Font('SegaArcadeFontRegular.ttf',25)
fontbig=pygame.font.Font('ARCADECLASSIC.ttf',80)
# Create game window

game_window = pygame.display.set_mode((window_width, window_height))

#creating functions
def showmag(x,y):
    bult=font.render("BULLETS: "+str(bulletmag),True,(0,0,0))
    game_window.blit(bult,(x,y))
def gameover():
    G_O= fontbig.render("GAME OVER",True,(0,0,0))
    game_window.blit(G_O,(200,250))
def showscore(x,y):
    score=font.render("SCORE: "+str(scorev),True,(0,0,0))
    game_window.blit(score,(x,y))
def display():
    game_window.blit(background,(0,0))
def player(x,y):
    game_window.blit(simo,(x,y))
def enemy(x,y):
    game_window.blit(russian,(x,y))
def fire(x,y):
    global bulletstate
    if(bulletstate!='empty'):
        bulletstate='fire'
        game_window.blit(bullet, (x+40,y+40))
def collision(x2,y2,x3,y3):
    distance=math.sqrt(math.pow(x2-x3,2)+math.pow(y2-y3,2))
    if distance<40:
        return True
    else:
        return False
# Set window title

pygame.display.set_caption("White Death")
pygame.display.set_icon(icon)


# Run game loop

running = True
while running:
    # Handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                poschange=-speed
            if event.key==pygame.K_d:
                poschange=speed
            if event.key==pygame.K_s:
                bulletx=playerx
                fire(bulletx,bullety)
                bulletmag-=1
        if event.type==pygame.KEYUP:
            poschange=0
    


    # Draw game objects


    
    display()



    enemy(enemyx,enemyy)
    player(playerx,playery)
    showscore(10,10)
    showmag(10,40)

    # Update game state
    if bulletstate == 'fire':
        fire(playerx,bullety)
        bullety-=bulletychange
        if(bullety<0):
            bullety=playery
            if bulletmag>0:
                bulletstate='ready'
            else:
                bulletstate='empty'


    playerx+=poschange
    if (playerx>720):
        playerx=720
    elif (playerx<10):
        playerx=10


    enemyx+=enemyxchange
    if (enemyx>=720):
        enemyx=720
        enemyxchange=-enemyspeed
        enemyy+=enemyychange
    elif (enemyx<=10):
        enemyx=15
        enemyxchange=enemyspeed
        enemyy+=enemyychange
    
    coll= collision(enemyx,enemyy,bulletx,bullety)
    death=collision(playerx,playery,enemyx,enemyy)
    if coll==True and death==False:
            enemyx=random.randint(0,700)
            bullety=playery
            bulletstate='ready'
            scorev+=1
            bulletmag+=1
            enemyy=100
    death=collision(playerx,playery,enemyx,enemyy)
    if death:
        gameover()
        enemyy=100
        enemyspeed=0
        gameover()
    if(bulletmag<0):
        bulletmag=0
    if (scorev>0 and scorev%10==0):
        bulletmag=7

    if(bulletmag==0 or death):
        for i in range(1000):
            gameover()
            enemyxchange=0
            enemyychange=0
            bulletspeed=0
            
        

    # Update game window

    pygame.display.update()

# Quit Pygame

pygame.quit()
