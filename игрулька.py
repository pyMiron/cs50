import pygame
pygame.init()
flRunning = True
W, H = 600, 400
FPS = 60

sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption('моя игра на pygame')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.draw.rect(sc, WHITE, (10, 10, 50, 100), 2)

pygame.draw.line(sc, BLUE, (200, 20), (350, 50))
pygame.draw.aaline(sc, GREEN, (200, 40), (350, 70))

pygame.draw.line(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 2)
pygame.draw.aaline(sc, RED, True, [(300, 80), (350, 80), (400, 200)], 2)

pygame.display.update()
clock = pygame.time.Clock()

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    clock.tick(FPS)
