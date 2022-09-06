import pygame

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Ship Game")
clock = pygame.time.Clock()
FPS = 60

class Player(pygame.Rect):
    def __init__(self):
        self.image = pygame.image.load("./player.png")
    def update(self):
        display.blit(self.image, self)

class Enemy(pygame.Rect):
    def __init__(self):
        self.image = pygame.image.load("./enemy.png")
    def update(self):
        display.blit(self.image, self)


def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        display.fill((255, 255, 255))
        pygame.display.update()

if __name__ == "__name__":
    main()
