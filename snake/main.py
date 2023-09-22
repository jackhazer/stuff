import pygame, sys , random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.validPos=[]
        for i in range(blockNumber):
            for j in range(blockNumber):
                self.validPos.append(Vector2(i,j))
        self.pos = random.choice(self.validPos)
    def getFruitPos(self):
        return self.pos
    def drawFruit(self):
        fruit_rect = pygame.Rect(self.pos.x*blockSize,self.pos.y*blockSize,blockSize,blockSize)
        pygame.draw.rect(screen,(220, 120, 20),fruit_rect)
    def generateFruit(self, invalidPos):
        self.validPos = [pos for pos in self.validPos if pos not in invalidPos]
        if not self.validPos:
            return True
        self.pos = random.choice(self.validPos)
        return False

class SNAKE:
    def __init__(self):
        self.x=0
        self.y=0
        self.direction=Vector2(1,0)
        self.pos= Vector2(self.x,self.y)
        self.body=[]
        self.length=190
    def drawSnake(self):
        for pos in self.body:
            snake_rect = pygame.Rect(pos.x*blockSize,pos.y*blockSize,blockSize,blockSize)
            pygame.draw.rect(screen, (0, 120, 20), snake_rect)
    def moveSnake(self):
        new_pos = self.pos
        if self.length <= len(self.body):
            self.body.pop(0)
        self.body.append(Vector2(new_pos))  # Create a new Vector2 instance for each segment
        self.pos += self.direction
    def collision(self):
        if self.pos.x<0 or self.pos.x>=blockNumber or self.pos.y<0 or self.pos.y>=blockNumber:
            return True
        if self.pos in self.body:
            return True
        return False
    def eat(self, fruit):
        if self.pos == fruit.getFruitPos():
            self.length += 1
            if fruit.generateFruit(self.body):
                return True
        return False
    def win(self):
        if self.length>=191:
            return True
        return False
pygame.init()
blockSize= 40
blockNumber= 20
screen = pygame.display.set_mode((blockNumber*blockSize,blockSize*blockNumber))
clock = pygame.time.Clock()
fruit=FRUIT()
snake=SNAKE()
FRAMERATE=pygame.USEREVENT
pygame.time.set_timer(FRAMERATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == FRAMERATE:
            if snake.collision() or snake.eat(fruit):
                pygame.quit()
                sys.exit()
            if snake.win():
                print('win!')
            snake.moveSnake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction.y!=1:
                snake.direction.y = -1
                snake.direction.x = 0
            elif event.key == pygame.K_DOWN and snake.direction.y!=-1:
                snake.direction.y = 1
                snake.direction.x = 0
            elif event.key == pygame.K_RIGHT and snake.direction.x!=-1:
                snake.direction.y = 0
                snake.direction.x = 1
            elif event.key == pygame.K_LEFT and snake.direction.x!=1:
                snake.direction.y = 0
                snake.direction.x = -1

    screen.fill((180,200,70))
    fruit.drawFruit()
    snake.drawSnake()
    pygame.display.update()
    clock.tick(60)