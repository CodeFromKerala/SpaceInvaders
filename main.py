# importing pygame
import pygame

# screen loading and fps
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Ship Game")
clock = pygame.time.Clock()
FPS = 60

# Player Class
class Player(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.move_left = False
        self.move_right = False
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./player.png"), (50, 50)), 180)
    def update(self):
        if self.move_left == True:
            self.centerx -= 10
        if self.move_right == True:
            self.centerx += 10
        display.blit(self.image, self)

# Enemy Class
class Enemy(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.image = pygame.transform.scale(pygame.image.load("./enemy.png"), (50, 50))
    def update(self):
        display.blit(self.image, self)

# Main game loop
def main():
    run = True
    player = Player(50, 550)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left = True
                if event.key == pygame.K_RIGHT:
                    player.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.move_left = False
                if event.key == pygame.K_RIGHT:
                    player.move_right = False
        display.fill((0, 0, 255))
        player.update()
        pygame.display.update()

# check if the file is not executed by import
if __name__ == "__main__":
    main()

quit()
# END OF PROGRAM