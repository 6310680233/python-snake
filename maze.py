
from random import *
from subprocess import call
from os import system, name
from time import sleep
import msvcrt


WIDTH = 32
HEIGH = 16
X_INDEX = 0
Y_INDEX = 1
snake = [[0,0],[1,0],[2,0]]
matrix = [[]]
food_position = [5,5]
velocity = [-1,0]
score = 0

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

def drawSnake(x,y):
    canDraw = False
    for coord in snake:
        if(x == coord[X_INDEX] and y == coord[Y_INDEX]):
            canDraw = True

    if snake[0][X_INDEX] < 0: snake[0][X_INDEX] = WIDTH
    if snake[0][Y_INDEX] < 0: snake[0][Y_INDEX] = HEIGH
    if snake[0][X_INDEX] > WIDTH: snake[0][X_INDEX] = 0
    if snake[0][Y_INDEX] > HEIGH: snake[0][Y_INDEX] = 0

    if(canDraw):
        print('*',end='')
    else:
        print(' ',end='')

def createMaze():
    matrix.clear()
    startMaze()
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
            if(col == 1):
                drawSnake(x,y)
            else:
                print('-',end='')
            x+=1
        x=0
        y+=1
        print('|')

    endMaze()

def updateVelocity():
    print(f'Velocity : ',velocity)
    print(f'Score : ',score)
    snake.insert(0, [snake[0][X_INDEX] + (velocity[X_INDEX]), snake[0][Y_INDEX] + velocity[Y_INDEX]])
    snake.pop()

def onKeyPressed():
    key = ord(msvcrt.getch())
    print(key)
    if(key==72): # UP
        velocity[1] = -1
    if(key==80): # DOWN
        velocity[1] = 1
    if(key==77): # RIGHT
        velocity[0] = 1
    if(key==75): # LEFT
        velocity[0] = -1
    

createMaze()
while True:
    #onKeyPressed()
    clear()
    updateVelocity()
    redraw()
    sleep(0.5)