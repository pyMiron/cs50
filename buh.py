import pygame
pygame.init()

scr = pygame.display.set_mode((700, 600))
pygame.cursors
done = False
red=(255, 100, 100)
font = pygame.font.SysFont("Arial", 80)

text = font.render("Welcome to PyGame", True,red )

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

            done = True

    scr.fill((0, 0, 0))

    scr.blit(text,(320 - text.get_width()//2, 240 - text.get_height() // 2))

    pygame.display.flip()