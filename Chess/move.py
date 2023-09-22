import pygame,sys
from gameState import GAMESTATE

class MOVE():
    def __init__(self):
        self.gameState=GAMESTATE()
        self.x=0
        self.y=0
        self.tx=0
        self.ty=0
    def makeMove(self,x,y,tx,ty):
        self.gameState.board[tx][ty] = self.gameState.board[x][y]
        self.gameState.board[x][y]='--'
