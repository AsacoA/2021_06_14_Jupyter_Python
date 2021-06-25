import pygame
import sys
import numpy as np
pygame.init()

WHITE = (255, 255, 255) # RGB
TITLE = 'Dino Game'

# 게임 화면 크기
MAX_WIDTH, MAX_HEIGHT = 800, 400
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

# FPS - 설정
fps = pygame.time.Clock()

# 이미지 불러오기
dino_img1 = pygame.image.load('../res/img/dino1.png')
dino_img2 = pygame.image.load('../res/img/dino2.png')
obstacle_img1 = pygame.image.load('../res/img/obstacle_img1.png')
img = dino_img1

# window창 설정
pygame.display.set_caption(TITLE)
pygame.display.set_icon(dino_img1)

# 공룡 설정
DINI_SPEED = 8  # 낮을수록 빠름
i = 1

# 장애물 위치
obstacle_width, obstacle_height = obstacle_img1.get_size()[0], obstacle_img1.get_size()[1]
obstacle_x = MAX_WIDTH - obstacle_width
obstacle_y = MAX_HEIGHT - obstacle_height
obstacle_at_bottom = MAX_HEIGHT - obstacle_height

# 공룡 위치
dino_height = dino_img1.get_size()[1]
dino_x = 50
dino_y = MAX_HEIGHT - dino_height
JUMP_UPTO = 200
dino_at_bottom = MAX_HEIGHT - dino_height

is_bottom = True
is_go_up = False


# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print('here')
            if is_bottom:
                is_go_up = True # 올라가는 모드 True
                is_bottom = False   # 바닥에 붙어있는지를 판단

    # 공룡 움직이기
    if is_go_up:
        dino_y -= 8
        if dino_y <= JUMP_UPTO: is_go_up = False
    else:
        if not is_bottom:
            dino_y += 8
            if dino_y >= dino_at_bottom:
                is_bottom = True
                dino_y = dino_at_bottom

    # 공룡 움직임 표현하기
    if not i%DINI_SPEED: img = dino_img1
    elif i%DINI_SPEED == (DINI_SPEED/2): img = dino_img2
    i += 1

    # 장애물 움직이기
    obstacle_x -= 10

    # 장애물 생성하기
    if obstacle_x < 0:
        obstacle_x = MAX_WIDTH - obstacle_width

    screen.fill((255, 255, 255))
    screen.blit(img, (dino_x, dino_y))
    screen.blit(obstacle_img1, (obstacle_x, obstacle_y))

    pygame.display.update()
    fps.tick(60)
