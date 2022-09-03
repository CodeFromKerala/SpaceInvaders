import pygame

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Ship Game")
clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    display.fill((255, 255, 255))
    pygame.display.update()
