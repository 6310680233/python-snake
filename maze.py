from random import *
from subprocess import call
from os import system, name
from time import sleep
import msvcrt

FPS = 60
WIDTH = 32
HEIGH = 16
X_INDEX = 0
Y_INDEX = 1
snake = [[0,0],[1,0],[2,0]]
matrix = [[]]
food_position = [5,5]
velocity = [-1,0]
SCORE = 0
key = 0

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def startMaze():
    print('|',end='')
    for start in range(WIDTH):
        print('-',end='')
    print('|')

def endMaze():
    print('|',end='')
    for end in range(WIDTH):
        print('-',end='')
    print('|')

def drawSnake(x,y,area=1):
    canDraw = False
    for coord in snake:
        if(x == coord[X_INDEX] and y == coord[Y_INDEX]):
            canDraw = True

    snake_x = snake[0][X_INDEX]
    snake_y = snake[0][Y_INDEX]
    if snake_x < 0: snake_x = WIDTH
    if snake_y < 0: snake_y = HEIGH
    if snake_x > WIDTH: snake_x = 0
    if snake_y > HEIGH: snake_y = 0


    if(canDraw):
        if (area == 2 and snake_x == x and snake_y == y):
            #respawnFood()
            print('=',end='')
        else:
            print('*',end='')
    else:
        print(' ',end='')

def respawnFood():
    index_x = 0
    index_y = 0
    for i in matrix:
        for j in i:
            available = matrix[index_y][index_x]
            if(available == 2):
                matrix[index_y][index_x] = 1
            index_x += 1
        index_y += 1
    print('spawned food')

def createMaze():
    matrix.clear()
    startMaze()
    foodReady = False
    for row in range(HEIGH):
        print('|',end='')
        colList = []
        for col in range(WIDTH):
            drawCol = False
            available = 0
            if(drawCol):
                print('-',end='')
                available = 0
            else:
                if(random()*100 >= 50 and foodReady == False):
                    foodReady = True
                    print('+',end='')
                    available = 2
                else:
                    print(' ',end='')
                    available = 1
            colList.append(available)
        print('|')
        matrix.append(colList)
    endMaze()
    print('end')

def redraw():
    startMaze()
    x=0
    y=0
    for row in matrix:
        print('|',end='')
        for col in row:
            if(col == 1 or col == 2):
                drawSnake(x,y,col)
            else:
                print('-',end='')
            x+=1
        x=0
        y+=1
        print('|')

    endMaze()

def updateVelocity():
    print(f'Velocity : {velocity}')
    print(f'Head : {snake[0]}')
    print(f'Score : {SCORE}')
    print(f'FPS : {FPS}')
    snake.insert(0, [snake[0][X_INDEX] + (velocity[X_INDEX]), snake[0][Y_INDEX] + velocity[Y_INDEX]])
    snake.pop()

def onKeyPressed():
    key = ord(msvcrt.getch())
    if(key==72): # UP
        velocity[0] = 0
        velocity[1] = -1
    if(key==80): # DOWN
        velocity[0] = 0
        velocity[1] = 1
    if(key==77): # RIGHT
        velocity[0] = 1
        velocity[1] = 0
    if(key==75): # LEFT
        velocity[0] = -1
        velocity[1] = 0
    

createMaze()
while True:
    clear()
    updateVelocity()
    redraw()
    onKeyPressed()
    sleep(1/FPS)