# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:02:56 2020

@author: pranai
"""
board = [' ' for x in range(10)]
def insertletter(letter,pos):
    board[pos] = letter

def printboard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')
    print('-'*12)
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('-'*12)
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    print('-'*12)
    
def spaceisfree(pos):
    return board[pos]==' '

def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def iswinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
            (b[4]==l and b[5]==l and b[6]==l) or
            (b[7]==l and b[8]==l and b[9]==l) or
            (b[1]==l and b[4]==l and b[7]==l) or
            (b[2]==l and b[5]==l and b[8]==l) or
            (b[3]==l and b[6]==l and b[9]==l) or
            (b[1]==l and b[5]==l and b[9]==l) or
            (b[3]==l and b[5]==l and b[7]==l)) 

def playermove():
    flag = True
    while flag:
        move = input('Please select position to enter the x between 1 to 9 : ')
        try:
            move = int(move)
            if move > 0 and move <10:
                if spaceisfree(move):
                    flag = False
                    insertletter('X',move)
                else:
                    print('Sorry, this place is occupied!!')
            else:
                print('Please type a number between 1 to 9')        
        except:
            print('Please type a number')
        
def selectrandom(list):
    import random
    l = len(list)
    r = random.randrange(0,l)
    return list[r]
    
def computermove():
    possiblemoves = [x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move = 0
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(boardcopy,let):
                move=i
                return move
    
    cornersopen = []
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move = selectrandom(cornersopen)
        return move
    
    if 5 in possiblemoves:
        move = 5
        return move
    
    edgesopen = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)
        
    if len(edgesopen)>0:
        move = selectrandom(edgesopen)
        return move
            
def main():
    print('Welcome to the game!!!')
    printboard(board)
    
    while not(isboardfull(board)):
        if not(iswinner(board,'O')):
            playermove()
            printboard(board)
        else:
            print('Sorry, you lost the game!!')
            break    
        if not(iswinner(board,'X')):
            move = computermove()
            if move==0:
                print(' ')
            else:
                insertletter('O',move)
                print('Computer placed an O on position ',move,' : ')
                printboard(board)
        else:
            print('You win!!')
            break
        
    if isboardfull(board):
            print('Tie Game!!')
        
while True:
    x = input('Do you want to play (y/n) : ').lower()
    if x=='y':
        board = [' ' for x in range(10)]
        print('-'*12)
        main()
    else:
        break
            
    