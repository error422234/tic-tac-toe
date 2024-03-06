import pygame
import random
WIDTH=300
HEIGHT=300
FPS=30
white=(255,255,255)
GREEN=(0,255,0)
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Крестики-нолики")
screen.fill(white)
BLACK=(0,0,0)
clock=pygame.time.Clock()
game_over=False
field=[["","",""],
       ["","",""],
       ["","",""]]
def draw_grid():
    pygame.draw.line(screen,(0,0,0),(100,0),(100,300),3)
    pygame.draw.line(screen,(0,0,0),(200,0),(200,300),3)
    pygame.draw.line(screen,(0,0,0),(0,100),(300,100),3)
    pygame.draw.line(screen,(0,0,0),(0,200),(300,200),3)
def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j]=="0":
                pygame.draw.circle(screen,BLACK,(j*100+50,i*100+50),45,3)
            elif field[i][j]=="x":
                pygame.draw.line(screen,(BLACK),(j*100+5,i*100+5),(j*100+95,i*100+95),3)
                pygame.draw.line(screen, (BLACK), (j * 100 + 95, i * 100 + 5), (j * 100 + 5,i*100+95),3)

def get_win_check(symbol):
    flag_win=False
    global win
    for line in field:
        if line.count(symbol)==3:
            flag_win=True
            win=[[0,field.index(line)],[1,field.index(line)],[2,field.index(line)]]
    for i in range(3):
        if field[0][i]==field[1][i]==field[2][i]==symbol:
            flag_win=True
            win=[[i,0],[i,1],[i,2]]
            print(win)
    if field[0][0]==field[1][1]==field[2][2]==symbol:
        flag_win=True
        win=[[0,0],[1,1],[2,2]]
        print(win)
    if field[0][2]==field[1][1]==field[2][0]==symbol:
        flag_win=True
        win=[[0,2],[1,1],[2,0]]
        print(win)
    return flag_win


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if field[pos[1]//100][pos[0]//100]=="":
                field[pos[1]//100][pos[0]//100]="x"
                x,y=random.randint(0,2),random.randint(0,2)
                while field[x][y]!="":
                  x,y=random.randint(0,2),random.randint(0,2)
                field[x][y]="0"
            player_win=get_win_check("x")
            ai_win=get_win_check("0")
            rezult=field[0].count("x")+field[0].count("0")+field[1].count("x")+field[1].count("0")+field[2].count("x")+field[2].count("0")
            if player_win or ai_win:
                game_over=True
                if player_win:
                    pygame.display.set_caption("Вы победили")
                else:
                    pygame.display.set_caption("Компьютер победил")
            elif rezult==8:
                pygame.display.set_caption("Ннчья")



    screen.fill(white)
    if game_over:
        pygame.draw.rect(screen,GREEN,(win[0][0]*100,win[0][1]*100,100,100))
        pygame.draw.rect(screen, GREEN,(win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[2][0] * 100, win[2][1] * 100, 100, 100))

    draw_tic_tac_toe()
    draw_grid()
    pygame.display.flip()
