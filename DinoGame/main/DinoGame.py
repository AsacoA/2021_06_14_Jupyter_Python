import pygame
import sys

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

pygame.display.set_caption(TITLE)
pygame.display.set_icon(dino_img1)

# 공룡 위치

dino_height = dino_img1.get_size()[1]
dino_x = 50
dino_y = MAX_HEIGHT - dino_height
JUMP_UPTO = 200
dino_at_bottom = MAX_HEIGHT - dino_height   # dino가 맨 아래에 [있을

is_bottom = True
is_go_up = False

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
    #공룡 움직이기
            if is_bottom:
                is_go_up = True # 올라가는 모드 True
                is_bottom = False   # 바닥에 붙어있는지를 판단
    if is_go_up: dino_y -= 10
    elif not is_go_up and not is_bottom: dino_y += 10

    if is_go_up and dino_y <= JUMP_UPTO: is_go_up = False

    if not is_bottom and dino_y >= dino_at_bottom:
        is_bottom = True
        dino_y = dino_at_bottom
        screen.fill((255, 255, 255))
        screen.blit(dino_img1, (dino_x, dino_y))
        pygame.display.update()

####################################################################################################