import pygame,sys
from pygame.math import Vector2
from settings import *
import copy

class GAMESTATE():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.images={}
        self.validMoves=[]
        self.wKingpos=(7,4)
        self.bKingpos=(0,4)
        self.pawnPos=(0,0)
        self.running=True
        self.isEnpassent=False
        self.board=[['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                    ['--', '--', '--', '--', '--', '--', '--', '--'],
                    ['--', '--', '--', '--', '--', '--', '--', '--'],
                    ['--', '--', '--', '--', '--', '--', '--', '--'],
                    ['--', '--', '--', '--', '--', '--', '--', '--'],
                    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

    def loadImages(self):
        pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
        for piece in pieces:
            self.images[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + '.png'),(blockSize, blockSize))
        self.images['bP'] = pygame.transform.scale(pygame.image.load('images/' + 'bp' + '.png'),(blockSize, blockSize))
        self.images['wP'] = pygame.transform.scale(pygame.image.load('images/' + 'wp' + '.png'),(blockSize, blockSize))
        self.images['bk'] = pygame.transform.scale(pygame.image.load('images/' + 'bK' + '.png'), (blockSize, blockSize))
        self.images['wk'] = pygame.transform.scale(pygame.image.load('images/' + 'wK' + '.png'), (blockSize, blockSize))
        self.images['br'] = pygame.transform.scale(pygame.image.load('images/' + 'bR' + '.png'), (blockSize, blockSize))
        self.images['wr'] = pygame.transform.scale(pygame.image.load('images/' + 'wR' + '.png'), (blockSize, blockSize))
    def drawBoard(self):
        for i in range(blockNumber):
            for j in range(blockNumber):
                isBlack=(i+j)%2
                square = pygame.Rect(j*blockSize,i*blockSize,blockSize,blockSize)
                color=(125,125,125) if isBlack else (255,255,255)
                pygame.draw.rect(self.display_surface, color, square)

    def drawPieces(self):
        for i in range(blockNumber):
            for j in range(blockNumber):
                if self.board[i][j]!='--':
                    piece = self.images[self.board[i][j]]
                    self.display_surface.blit(piece, (j * blockSize, i * blockSize))

    def isValid(self, x, y):
        self.validMoves = []
        if self.board[x][y][1].lower() == 'p':
            self.checkPawn(x, y)
        elif self.board[x][y][1] == 'N':
            self.checkKnight(x, y)
        elif self.board[x][y][1].upper() == 'R':
            self.checkRook(x, y)
        elif self.board[x][y][1] == 'B':
            self.checkBishop(x, y)
        elif self.board[x][y][1] == 'Q':
            self.checkRook(x, y)
            self.checkBishop(x, y)
        elif self.board[x][y][1].upper() == 'K':
            self.checkKing(x, y)
    def checkPawn(self, x, y):

        if self.board[x][y][0] == 'w':
            if self.isEnpassent:
                if (y>0 and (x,y-1)==self.pawnPos) or (y<7 and (x,y+1)==self.pawnPos):
                    self.validMoves.append((self.pawnPos[0]-1,self.pawnPos[1]))
            if self.board[x - 1][y] == '--':
                self.validMoves.append((x - 1, y))
            if self.board[x][y][1] == 'p' and self.board[x - 2][y] == '--':
                self.validMoves.append((x - 2, y))
            if x > 0 and y < 7 and self.board[x - 1][y + 1][0] == 'b':
                self.validMoves.append((x - 1, y + 1))
            if x > 0 and y > 0 and self.board[x - 1][y - 1][0] == 'b':
                self.validMoves.append((x - 1, y - 1))
        elif self.board[x][y][0] == 'b':
            if self.isEnpassent:
                if (y>0 and (x,y-1)==self.pawnPos) or (y<7 and (x,y+1)==self.pawnPos):
                    self.validMoves.append((self.pawnPos[0]+1,self.pawnPos[1]))
            if self.board[x + 1][y] == '--':
                self.validMoves.append((x + 1, y))
            if self.board[x][y][1] == 'p' and self.board[x + 2][y] == '--':
                self.validMoves.append((x + 2, y))
            if x < 7 and y < 7 and self.board[x + 1][y + 1][0] == 'w':
                self.validMoves.append((x + 1, y + 1))
            if x < 7 and y > 0 and self.board[x + 1][y - 1][0] == 'w':
                self.validMoves.append((x + 1, y - 1))
    def checkCastle(self,x,y,path):
        for square in path:
            temp = copy.deepcopy(self.board)
            tx, ty = square
            if self.board[tx][ty]!='--':
                return False
            self.board[tx][ty] = self.board[x][y]
            self.board[x][y] = '--'
            if self.isCheck(tx, ty):
                self.board = copy.deepcopy(temp)
                return False
            self.board = copy.deepcopy(temp)
        return True
    def checkKnight(self,x,y):
        for dx,dy in logic['N']:
            if 0<=x+dx<8 and 0<=y+dy<8 and self.board[x+dx][y+dy][0]!=self.board[x][y][0]:
                self.validMoves.append((x+dx,y+dy))
    def checkKing(self,x,y):
        for dx,dy in logic['K']:
            if 0<=x+dx<8 and 0<=y+dy<8 and self.board[x+dx][y+dy][0]!=self.board[x][y][0]:
                self.validMoves.append((x+dx,y+dy))
        if self.board[x][y][1]=='K' and self.board[x][0][1]=='R' and not self.isCheck(x,y) and self.checkCastle(x,y,[(x,y-1),(x,y-2)]):
            self.validMoves.append((x,y-2))
        if self.board[x][y][1]=='K' and self.board[x][7][1]=='R' and not self.isCheck(x,y) and self.checkCastle(x,y,[(x,y+1),(x,y+2)]):
            self.validMoves.append((x,y+2))
    def checkRook(self,x,y):
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in direction:
            i=1
            while 0<=x+dx*i<8 and 0<=y+dy*i<8 and self.board[x+dx*i][y+dy*i][0]!=self.board[x][y][0]:
                self.validMoves.append((x+dx*i,y+dy*i))
                if self.board[x+dx*i][y+dy*i]!='--':
                    break
                i += 1
    def checkBishop(self,x,y):
        direction = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in direction:
            i = 1
            while 0 <= x + dx * i < 8 and 0 <= y + dy * i < 8 and self.board[x + dx * i][y + dy * i][0] != \
                    self.board[x][y][0]:
                self.validMoves.append((x + dx * i, y + dy * i))
                if self.board[x + dx * i][y + dy * i] != '--':
                    break
                i += 1

    def isCheck(self,x,y):
        color=self.board[x][y][0]
        enemyColor='b' if color=='w' else 'w'
        kx,ky=self.wKingpos if color=='w' else self.bKingpos
        if self.board[x][y][1].upper()=='K':
            kx,ky=x,y
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in direction:
            i = 1
            while 0 <= kx + dx * i < 8 and 0 <= ky + dy * i < 8 and self.board[kx + dx * i][ky + dy * i] == '--':
                i += 1
            if 0 <= kx + dx * i < 8 and 0 <= ky + dy * i < 8 and self.board[kx + dx * i][ky + dy * i][0]==enemyColor and self.board[kx + dx * i][ky + dy * i][1] in 'RQ':
                return True
        direction = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in direction:
            i = 1
            while 0 <= kx + dx * i < 8 and 0 <= ky + dy * i < 8 and self.board[kx + dx * i][ky + dy * i] == '--':
                i += 1
            if 0 <= kx + dx * i < 8 and 0 <= ky + dy * i < 8 and self.board[kx + dx * i][ky + dy * i][
                0] == enemyColor and self.board[kx + dx * i][ky + dy * i][1] in 'BQ':
                return True
        direction = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
        for dx, dy in direction:

            if 0 <= kx + dx  < 8 and 0 <= ky + dy  < 8 and self.board[kx + dx ][ky + dy ][
                0] == enemyColor and self.board[kx + dx ][ky + dy ][1] in 'N':
                return True
        direction = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        for dx, dy in direction:

            if 0 <= kx + dx  < 8 and 0 <= ky + dy  < 8 and self.board[kx + dx ][ky + dy ][
                0] == enemyColor and self.board[kx + dx ][ky + dy ][1] in 'K':
                return True
        if enemyColor == 'b':
            if kx - 1 >= 0:
                if ky - 1 >= 0 and (self.board[kx - 1][ky - 1] == 'bp' or self.board[kx - 1][ky - 1] == 'bP'):
                    return True
                if ky + 1 < 8 and (self.board[kx - 1][ky + 1] == 'bp' or self.board[kx - 1][ky + 1] == 'bP'):
                    return True
        else:
            if kx + 1 < 8:
                if ky - 1 >= 0 and (self.board[kx + 1][ky - 1] == 'wp' or self.board[kx + 1][ky - 1] == 'wP'):
                    return True
                if ky + 1 < 8 and (self.board[kx + 1][ky + 1] == 'wp' or self.board[kx + 1][ky + 1] == 'wP'):
                    return True

        return False
    def isCheckmated(self,x,y):
        color = self.board[x][y][0]
        enemyColor = 'b' if color == 'w' else 'w'
        for i in range(blockNumber):
            for j in range(blockNumber):
                if self.board[i][j][0]==enemyColor:
                    self.isValid(i, j)
                    self.removeChecks(i, j)
                    if self.validMoves:
                        return False
        return True
    def removeChecks(self,x,y):
        i = 0
        while i < len(self.validMoves):
            temp = copy.deepcopy(self.board)
            tx, ty = self.validMoves[i]
            self.board[tx][ty] = self.board[x][y]
            self.board[x][y] = '--'
            if self.isCheck(tx, ty):
                self.validMoves.pop(i)
            else:
                i += 1
            self.board = copy.deepcopy(temp)

    def makeMove(self,x,y,tx,ty):
        self.isValid(x, y)
        print(self.validMoves)
        self.removeChecks(x,y)
        print(self.validMoves)
        if (tx,ty) in self.validMoves:
            target=self.board[tx][ty]
            self.board[tx][ty] = self.board[x][y]
            if self.isEnpassent:
                self.isEnpassent=False
            if self.board[tx][ty][1]=='p':
                if abs(tx-x)==2:
                    self.isEnpassent=True
                    self.pawnPos=(tx,ty)
                self.board[tx][ty] = self.board[tx][ty][0]+ 'P'
            elif self.board[tx][ty][1]=='P':
                if target=='--' and tx!=x and ty!=y:
                    self.board[x][ty]='--'
                elif tx==0 or tx==7:
                    self.board[tx][ty]=self.board[tx][ty][0]+'Q'
            elif self.board[tx][ty][1].upper()=='K':
                self.board[tx][ty]=self.board[tx][ty][0]+'k'
                if self.board[tx][ty][0]=='w':
                    self.wKingpos=(tx,ty)
                else:
                    self.bKingpos=(tx,ty)
                if ty-y==2:
                    self.board[tx][7]='--'
                    self.board[tx][5]=self.board[tx][ty][0]+'r'
                elif ty-y==-2:
                    self.board[tx][0] = '--'
                    self.board[tx][3] = self.board[tx][ty][0] + 'r'

            elif self.board[tx][ty][1]=='R':
                self.board[tx][ty]=self.board[tx][ty][0]+'r'
            self.board[x][y]='--'
            if self.isCheckmated(tx,ty):
                print('game over!')
                self.running=False

            return True
        else:
            print('invalidmove')
            return False