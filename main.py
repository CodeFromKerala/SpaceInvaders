# importing pygame
import pygame

# screen loading and fps
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Space Ship Game")

# Player Class
class Player(pygame.Rect):
    def __init__(self):
        self.image = pygame.image.load("./player.png")
    def update(self):
        display.blit(self.image, self)

# Enemy Class
class Enemy(pygame.Rect):
    def __init__(self):
        self.image = pygame.image.load("./enemy.png")
    def update(self):
        display.blit(self.image, self)

# Main game loop
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

# check if the file is not executed by import
if __name__ == "__main__":
    main()