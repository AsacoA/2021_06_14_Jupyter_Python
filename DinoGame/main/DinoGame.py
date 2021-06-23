import pygame

pygame.init()

WHITE = (255, 255, 255) # RGB

#게임 화면 크기
MAX_WIDTH, MAX_HEIGHT = 800, 400
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

# FPS - 설정
fps = pygame.time.Clock()
