import pygame,sys
from gameState import GAMESTATE
from settings import *

class GAME:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('CHESS')
        self.clock = pygame.time.Clock()
        self.gameState=GAMESTATE()
        self.selected=()
        self.whiteToMove = True
    def run(self):
        self.gameState.loadImages()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos= pygame.mouse.get_pos()
                    pos=(pos[0]//blockSize,pos[1]//blockSize)
                    y,x=pos
                    piece_color = self.gameState.board[x][y][0]

                    if self.selected:
                        if self.gameState.makeMove(self.selected[0],self.selected[1], x, y):
                            self.selected = ()
                            self.whiteToMove = not self.whiteToMove
                        else:
                            if (piece_color == 'w' and self.whiteToMove) or (
                                    piece_color == 'b' and not self.whiteToMove):
                                self.selected = (x, y)
                    else:
                        if (piece_color == 'w' and self.whiteToMove) or (piece_color == 'b' and not self.whiteToMove):
                            self.selected = (x, y)
            if not self.gameState.running:
                self.gameState.drawBoard()
                self.gameState.drawPieces()
                self.clock.tick(FPS)
                font = pygame.font.Font(None, 100)
                game_over_text = font.render("CHECKMATE", True, (17, 79, 21))
                text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                self.screen.blit(game_over_text, text_rect)
                pygame.display.update()
            else:
                self.gameState.drawBoard()
                self.gameState.drawPieces()
                self.clock.tick(FPS)
                pygame.display.update()

if __name__ == '__main__':
    game = GAME()
    game.run()