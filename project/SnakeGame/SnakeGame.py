import os
import sys
import random
import time
import pygame

# 윈도우창 초기 위치
win_posx = 700
win_posy = 300
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (win_posx, win_posy)

# 윈도우창 설정
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600

# 한번에 이동할 픽섹의 수
GRID = 30
GRID_WIDTH = int(WINDOW_WIDTH / GRID)
GRID_HEIGHT = int(WINDOW_HEIGHT / GRID)

# 색상설정
BACKGROUND = pygame.Color('#F5F7FA')
SNAKE_HEAD = pygame.Color('#967aDC')
SNAKE_BODY = pygame.Color('#AC92EC')
FOOD = pygame.Color('#DA4453')
SCOREBOX = pygame.Color('#CCD1D9')
FONT = pygame.Color('#434A54')

# 이동 방향
NORTH = (0, -1)
SOUTH = (0, 1)
WEST = (-1, 0)
EAST = (1, 0)


class Snake:
    def __init__(self):
        # 뱀모양 그리기
        self.length = 1
        self.createSnake()

        # 게임 점수
        self.game_score = 0

    def createSnake(self):
        self.positions = [(int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))]  # 몸을 이루는 픽섹들의 모임, 머리부터 생성, 화면 정중앙 위치
        self.direction = random.choice([NORTH, SOUTH, WEST, EAST])  # 첫 이동방향은 랜덤

    def moveNcheck(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        nxt_pos = ((head_x + (dir_x * GRID)) % WINDOW_WIDTH, (head_y + (dir_y * GRID)) % WINDOW_HEIGHT)

        # 자기 몸에 부딪히면 GAMEOVER
        if nxt_pos in self.positions[0:]:
            return 'DEAD'
        else:
            self.positions = [nxt_pos] + self.positions[:-1]
            return 'ALIVE'

    def setDir(self, arrowkey):
        # 기존 방향과 다른 키일 때만 self.direction 업데이트하기
        if (arrowkey[0] * -1, arrowkey[1] * -1) == self.direction:
            pass
        else:
            self.direction = arrowkey


class Foodbasket:
    def __init__(self):
        self.color = FOOD
        self.foods = []
        self.foods = self.makeFoods()

    def makeFoods(self):
        made = []
        if len(self.foods) < 3:
            make_num = random.randint(1, 2)
            for i in range(make_num):
                made.append(self.setPosition())
                return made

    def setPosition(self):
        return (random.randint(0, GRID_WIDTH - 1) * GRID,
                random.randint(0, GRID_HEIGHT - 1) * GRID)

    def refill(self):
        new_foods = self.makeFoods()
        self.foods.extend(new_foods)

class Game:
    def __init__(self):
        # pygame 환경설정
        pygame.display.set_caption('SNAKE GAME')
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def start(self):
        snake = Snake()
        game_score = 0
        foodbasket = Foodbasket()

        # 게임루프
        alive = True
        while alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: alive = False  # 닫기창 누르면 종료
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: alive = False  # q 누르면 종료
                    if event.key == pygame.K_UP: snake.setDir(NORTH)
                    if event.key == pygame.K_DOWN: snake.setDir(SOUTH)
                    if event.key == pygame.K_RIGHT: snake.setDir(EAST)
                    if event.key == pygame.K_LEFT: snake.setDir(WEST)

                    # 뱀의 다음 위치 구하고 GAMEOVER인지 확인하기
            if snake.moveNcheck() == 'ALIVE':
                # 음식 먹었는지 확인하기
                for idx, food in enumerate(foodbasket.foods):
                    if snake.positions[0] == food:
                        print('test')
                        snake.length += 1
                        game_score += 1

                        curr_tail_x, curr_tail_y = snake.positions[-1]
                        new_tail = (curr_tail_x + (-snake.direction[0] * GRID), curr_tail_y + (-snake.direction[1] * GRID))
                        snake.positions.append(new_tail)

                        foodbasket.foods = foodbasket.foods[:idx] + foodbasket.foods[idx + 1:]
                        foodbasket.refill()
                        break

                # 속도 갱신하기
                self.speed = snake.length / 2

                # 새로운 프레임 그리기
                self.updateFrame(snake, foodbasket.foods, game_score)
                pygame.display.flip()
                pygame.display.update()
                self.clock.tick(5 + self.speed)

            else:
                alive = False

        # pygame 종료
        self.gameover()
        print('pygame closed')
        pygame.quit()
        sys.exit()

    def updateFrame(self, snake, foods, game_score):
        # 배경 그리기
        self.screen.fill(BACKGROUND)

        # 새로운 뱀의 위치 표현하기
        for index, (pos_x, pos_y) in enumerate(snake.positions):
            if index == 0:
                self.drawRect(SNAKE_HEAD, pos_x, pos_y)
            else:
                self.drawRect(SNAKE_BODY, pos_x, pos_y)

        # 새로운 음식 위치 표현하기
        for pos_x, pos_y in foods:
            self.drawRect(FOOD, pos_x, pos_y)

        # 점수 보여주기
        self.show_info(snake, game_score)

    def drawRect(self, color, lefttop_x, lefttop_y):
        rect = pygame.Rect((lefttop_x, lefttop_y), (GRID, GRID))
        pygame.draw.rect(self.screen, color, rect)

    def show_info(self, snake, game_score):
        font = pygame.font.SysFont('malgungothic', 35)
        image = font.render(f' 점수 : {game_score} 뱀길이: {snake.length} LV: {int(self.speed // 2)} ', True, FONT)
        pos = image.get_rect()
        pos.move_ip(20, 20)
        pygame.draw.rect(image, SCOREBOX, (pos.x - 20, pos.y - 20, pos.width, pos.height), 2)
        self.screen.blit(image, pos)

    def gameover(self):
        font = pygame.font.SysFont('malgungothic', 50)
        image = font.render('GAME OVER', True, FONT)
        pos = image.get_rect()
        pos.move_ip(120, 220)
        self.screen.blit(image, pos)
        pygame.display.update()
        time.sleep(2)


# pygame 초기화
pygame.init()

# 게임 시작
game = Game()
game.start()