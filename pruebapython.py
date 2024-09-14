# Example file showing a circle moving on screen
import pygame
import pygame.gfxdraw

# pygame setup
pygame.init()

h = (720, 480)
hd = (1280, 720)
fhd = (1920,1080)
screenSize = fhd
screen = pygame.display.set_mode((screenSize), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
player1speed = 240
player2speed = 340
topbar = 8
leftbar = 257


player1_pos = pygame.Vector2(257,8) #pygame.Vector2(screen.get_width() / 2 -    900, screen.get_height() / 2)
player2_pos = pygame.Vector2(0,100)#screen.get_width() / 2 + 400, screen.get_height() / 2)
playersize = (56,56)





#pygame.draw.circle(screen, "purple", player2_pos, 40)
class square:
    def __init__(self, width, height, x, y, collider):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.collider = collider

# revisar esto:
blockSize = [74,74]
solidBlocks2 = []
blockLengh = 100
for i in range(1,9+1,2):
    for u in range (1,11+1,2):
        solidBlocks2.append((screen, 
            "black", 
            (leftbar+blockSize[0]*u,topbar+blockSize[1]*i,blockSize[0], blockSize[1]), 
            blockLengh2))

class player:
    def __init__(self,x,y,sprite,bTimer):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.bTimer = bTimer
class bomb(square):
    def __init__(self,square,player):
        self.timer = player.timer
    def putBomb():
        print("aqui va un metodo para poner una bomba, crear una lista de bombas")

class sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60,60))
        self.image.fill((0,128,255))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
sP1Group = pygame.sprite.Group()
sPlayer1 = sprite()
sP1Group.add(sPlayer1)
isSquareIn = []



p1 = player(257,8,sPlayer1.rect,100)
p2 = player(257,8,sPlayer1.rect,100)


"""
blocklengh = 100
blockSize  = (74,74)
rect1 = (leftbar+blockSize[0]*1,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect2 = (leftbar+blockSize[0]*3,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect3 = (leftbar+blockSize[0]*5,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect4 = (leftbar+blockSize[0]*7,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect5 = (leftbar+blockSize[0]*9,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect6 = (leftbar+blockSize[0]*11,topbar+blockSize[1]*1,blockSize[0], blockSize[1])
rect7 = (leftbar+blockSize[0]*1,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect8 = (leftbar+blockSize[0]*3,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect9 = (leftbar+blockSize[0]*5,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect10 = (leftbar+blockSize[0]*7,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect11 = (leftbar+blockSize[0]*9,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect12 = (leftbar+blockSize[0]*11,topbar+blockSize[1]*3,blockSize[0], blockSize[1])
rect13 = (leftbar+blockSize[0]*1,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect14 = (leftbar+blockSize[0]*3,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect15 = (leftbar+blockSize[0]*5,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect16 = (leftbar+blockSize[0]*7,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect17 = (leftbar+blockSize[0]*9,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect18 = (leftbar+blockSize[0]*11,topbar+blockSize[1]*5,blockSize[0], blockSize[1])
rect19 = (leftbar+blockSize[0]*1,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect20 = (leftbar+blockSize[0]*3,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect21 = (leftbar+blockSize[0]*5,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect22 = (leftbar+blockSize[0]*7,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect23 = (leftbar+blockSize[0]*9,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect24 = (leftbar+blockSize[0]*11,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
rect25 = (leftbar+blockSize[0]*1,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rect26 = (leftbar+blockSize[0]*3,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rect27 = (leftbar+blockSize[0]*5,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rect28 = (leftbar+blockSize[0]*7,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rect29 = (leftbar+blockSize[0]*9,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rect30 = (leftbar+blockSize[0]*11,topbar+blockSize[1]*9,blockSize[0], blockSize[1])
rectdoble = (leftbar+blockSize[0]*6,topbar+blockSize[1]*7,blockSize[0], blockSize[1])
solidblocks =(
    (screen, "black", rect1, blocklengh),
    (screen, "black", rect2, blocklengh),
    (screen, "black", rect3, blocklengh),
    (screen, "black", rect4, blocklengh),
    (screen, "black", rect5, blocklengh),
    (screen, "black", rect6, blocklengh),
    (screen, "black", rect7, blocklengh),
    (screen, "black", rect8, blocklengh),
    (screen, "black", rect9, blocklengh),
    (screen, "black", rect10, blocklengh),
    (screen, "black", rect11, blocklengh),
    (screen, "black", rect12, blocklengh),
    (screen, "black", rect13, blocklengh),
    (screen, "black", rect14, blocklengh),
    (screen, "black", rect15, blocklengh),
    (screen, "black", rect16, blocklengh),
    (screen, "black", rect17, blocklengh),
    (screen, "black", rect18, blocklengh),
    (screen, "black", rect19, blocklengh),
    (screen, "black", rect20, blocklengh),
    (screen, "black", rect21, blocklengh),
    (screen, "black", rect22, blocklengh),
    (screen, "black", rect23, blocklengh),
    (screen, "black", rect24, blocklengh),
    (screen, "black", rect25, blocklengh),
    (screen, "black", rect26, blocklengh),
    (screen, "black", rect27, blocklengh),
    (screen, "black", rect28, blocklengh),
    (screen, "black", rect29, blocklengh),
    (screen, "black", rect30, blocklengh)
    #(screen, "black", rectdoble, blocklengh)
)
"""

def canMoveUp(player, playerspeed):
    if player.y - playerspeed * dt > topbar:
            for block in solidBlocks2:
                if ((block[2][0] < player.x and block[2][0]+blockSize[0] >player.x)  or \
                    (block[2][0] < player.x+playersize[0] and block[2][0]+blockSize[0] \
                    > player.x+playersize[0])) and \
                    (block[2][1]+blockSize[1] > player.y-playerspeed*dt and \
                    block[2][1]<player.y):
                    return False
            return True
    else:
        return False
def moveUp(player, playerspeed):
    return player.y - playerspeed * dt
def canMoveDown(player, playerspeed):
    if player.y +playersize[1]+playerspeed*dt < topbar + 814:
            for block in solidBlocks2:
                if ((block[2][0] < player.x and block[2][0]+blockSize[0] >player.x)  or \
                    (block[2][0] < player.x+playersize[0] and block[2][0]+blockSize[0] \
                    > player.x+playersize[0])) and \
                    (block[2][1] < player.y+playersize[1]+playerspeed*dt and \
                    block[2][1]+blockSize[1] > player.y):
                    return False
            return True    
    else:
        return False
def moveDown(player,playerspeed):
    return player.y + playerspeed* dt
def canMoveLeft(player, playerSpeed):
    if leftbar < player.x-playerSpeed * dt:
        for block in solidBlocks2:
            if ((block[2][1]<player.y and block[2][1]+blockSize[1] > player.y) or \
                (block[2][1]<player.y+playersize[1] and block[2][1]+blockSize[1] > player.y+playersize[1]))\
                and (block[2][0]+blockSize[0]>player.x-playerSpeed * dt and\
                    block[2][0]<player.x):
                return False
        return True
    else:
        return False
def moveLeft(player, playerspeed):
    return player.x- playerspeed*dt
def canMoveRight(player,playerSpeed):
    if leftbar+962 > player.x+playersize[0]+playerSpeed * dt:
        for block in solidBlocks2:
            if((block[2][1]<player.y and block[2][1]+blockSize[1] > player.y) or \
                (block[2][1]<player.y+playersize[1] and block[2][1]+blockSize[1] > player.y+playersize[1]))\
                and (block[2][0]<player.x+playersize[0]+playerSpeed * dt and\
                block[2][0]>player.x+playersize[0]):
                return False
        return True
    else:
        return False
def moveRight(player, playerSpeed):
    return player.x+playerSpeed*dt

def arribaAbajo(player):
    #(player1_pos.y > 8 and player.y < 28) or\
    abajoarriba=False
    if (player.y > 8 and player.y < 28 and not keys[pygame.K_w]) or\
        (player.y > rect25[1]+blockSize[1] and not keys[pygame.K_s]):
        abajoarriba = True
    if  abajoarriba or\
        (player.y > topbar+blockSize[1]*2 and player.y < topbar+blockSize[1]*10) :
        #or\
        #(player.y > topbar+blockSize[1]*6 and player.y < topbar+blockSize[1]*6+50) or\
        #(player.y > topbar+blockSize[1]*8 and player.y < topbar+blockSize[1]*8+10) or\
        #(player.y > topbar+blockSize[1]*10 and player.y < topbar+blockSize[1]*10+30):

            #izquieda
            if not keys[pygame.K_d] and ( (player.x < rect1[0] and player.x > leftbar+8) or\
                (player.x < rect2[0] and player.x > rect1[0]+blockSize[0]) or\
                (player.x < rect3[0] and player.x > rect2[0]+blockSize[0]) or\
                (player.x < rect4[0] and player.x > rect3[0]+blockSize[0]) or\
                (player.x < rect5[0] and player.x > rect4[0]+blockSize[0]) or\
                (player.x < rect6[0] and player.x > rect5[0]+blockSize[0]) ):
                print(player.x , " " , player.y)
                player.x -= player1speed * dt
            #derecha
            if not keys [pygame.K_a] and ( (player.x + playersize[0] > rect1[0]+blockSize[0] and \
                player.x < rect1[0]+blockSize[0]) or\
                (player.x + playersize[0] > rect2[0]+blockSize[0] and
                player.x < rect2[0]+blockSize[0]) or
                (player.x + playersize[0] > rect3[0]+blockSize[0] and
                player.x < rect3[0]+blockSize[0]) or
                (player.x + playersize[0] > rect4[0]+blockSize[0] and
                player.x < rect4[0]+blockSize[0]) or
                (player.x + playersize[0]> rect5[0]+blockSize[0] and
                player.x < rect5[0]+blockSize[0]) or
                (player.x + playersize[0] > rect6[0]+blockSize[0] and
                player.x < rect6[0]+blockSize[0])):
                player.x += player1speed * dt
def derechaIzquierda(player):
    izquierdaderecha=False
    if (player.x + playersize[0] < rect1[0] and not keys[pygame.K_a]) or\
        (player.x > rect6[0]+blockSize[0] and not keys[pygame.K_d]):
        izquierdaderecha = True
    if  izquierdaderecha or\
    (player.x > rect1[0]+blockSize[0] and player.x+playersize[0]< rect2[0]) or\
    (player.x > rect2[0]+blockSize[0] and player.x+playersize[0]< rect3[0]) or\
    (player.x > rect3[0]+blockSize[0] and player.x+playersize[0]< rect4[0]) or\
    (player.x > rect4[0]+blockSize[0] and player.x+playersize[0]< rect5[0]) or\
    (player.x > rect5[0]+blockSize[0] and player.x+playersize[0]< rect6[0]):
        #Arriba
        if not keys[pygame.K_s] and ( 
            (player.y < rect1[1] and player.y+playersize[1] > rect1[1] ) or\
            (player.y < rect7[1] and player.y > rect1[1]+blockSize[1]) or\
            (player.y < rect13[1] and player.y > rect7[1]+blockSize[1]) or\
            (player.y < rect19[1] and player.y > rect13[1]+blockSize[1]) or\
            (player.y < rect25[1] and player.y > rect19[1]+blockSize[1])):
            player.y -= player1speed * dt
        #Abajo
        if not keys[pygame.K_w] and ( 
            (player.y < rect1[1]+blockSize[1] and player.y+playersize[1] > rect1[1]+blockSize[1]) or\
            (player.y < rect7[1]+blockSize[1] and player.y+playersize[1] > rect7[1]+blockSize[1]) or\
            (player.y < rect13[1]+blockSize[1] and player.y+playersize[1] > rect13[1]+blockSize[1]) or\
            (player.y < rect19[1]+blockSize[1] and player.y+playersize[1] > rect19[1]+blockSize[1]) or\
            (player.y < rect25[1]+blockSize[1] and player.y+playersize[1] > rect25[1]+blockSize[1])
            ):
            player.y += player1speed* dt 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    

    screen.fill("sky blue")
    
    pygame.draw.rect(screen,"white",
    (leftbar,topbar,962, 814),
    2,)


    for block in solidBlocks2:
        pygame.draw.rect(block[0],block[1],block[2],block[3],)
    
    

    pygame.draw.line(screen, "yellow", (player2_pos.x+40, player2_pos.y+40), (player1_pos.x+40, player1_pos.y+40), 10)
    
    rectplayer1 = (player1_pos.x, player1_pos.y, playersize[0], playersize[1])
    pygame.draw.rect(screen, "pink", rectplayer1, 50)
    rectplayer2 = (player2_pos.x, player2_pos.y, playersize[0], playersize[1])
    pygame.draw.rect(screen, "purple", rectplayer2, 50),
    
    move = True
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        arribaAbajo(player1_pos)  
        if canMoveUp(player1_pos, player1speed):
            player1_pos.y = moveUp(player1_pos, player1speed)
        move = True
    if keys[pygame.K_s]:
        arribaAbajo(player1_pos)
        if canMoveDown(player1_pos, player1speed):
            player1_pos.y = moveDown(player1_pos, player1speed) 
        move =True
    if keys[pygame.K_a]:
        derechaIzquierda(player1_pos)
        if canMoveLeft(player1_pos, player1speed):
            player1_pos.x = moveLeft(player1_pos, player1speed)
        move = True
    if keys[pygame.K_d]:
        derechaIzquierda(player1_pos)
        if canMoveRight(player1_pos, player1speed):
            player1_pos.x = moveRight(player1_pos,player1speed)
    if keys[pygame.K_p]:
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos.y -= player2speed * dt
    elif keys[pygame.K_DOWN]:
        player2_pos.y += player2speed * dt
    elif keys[pygame.K_LEFT]:
        player2_pos.x -= player2speed * dt
    elif keys[pygame.K_RIGHT]:
        player2_pos.x += player2speed * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    
    dt = clock.tick(60) / 1000

pygame.QUIT()