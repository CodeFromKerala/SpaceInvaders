# importing pygame

'''

Space Invaders In Python

By CodeFromKerala

'''

import pygame

# screen loading and fps
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Ship Game")
clock = pygame.time.Clock()
FPS = 60
ENEMY = []
LVL = 1

# Player Class
class Player(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.move_left = False
        self.move_right = False
        self.shoot = False
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("./player.png"), (50, 50)), 180)
    def update(self):
        if self.move_left == True:
            self.centerx -= 5
        if self.move_right == True:
            self.centerx += 5
        display.blit(self.image, self)

# Enemy Class
class Enemy(pygame.Rect):
    def __init__(self, x, y):
        self.centerx = x
        self.centery = y
        self.death = False
        self.image = pygame.transform.scale(pygame.image.load("./enemy.png"), (50, 50))
    def update(self):
        if self.death == False:
            if self.x > 0:
                self.x -= 3
            else:
                self.x = 750
                self.y += 10
            display.blit(self.image, self)

# Bullet Class
class Bullet(pygame.Rect):
    def __init__(self, player):
        self.centerx = player.centerx
        self.centery = player.centery
        self.image = pygame.image.load("./bullet.png")
    def update(self):
        if self.y > -20:
            self.y -= 10
        display.blit(self.image, self)
    def check_collision(self, enemy):
        global LVL
        if (self.x >= enemy.x and self.y >= enemy.y) and (self.x <= enemy.x + 50 and self.y <= enemy.y + 50):
            enemy.death = True
            LVL += 1

# spawn enemy function

class EnemyController:
    def spawn_enemy(x, y):
        global ENEMY
        enemy = Enemy(x, y)
        ENEMY.append(enemy)
    


# Main game loop
def main():
    run = True
    player = Player(50, 550)
    spawn_enemy(50, 50)
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
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player)
                    player.shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.move_left = False
                if event.key == pygame.K_RIGHT:
                    player.move_right = False
        display.fill((0, 0, 255))
        player.update()
        if player.shoot == True:
            bullet.update()
            bullet.check_collision(enemy)
        for enemy in ENEMY:
            enemy.update()
        pygame.display.update()

# check if the file is not executed by import
if __name__ == "__main__":
    main()

quit()
# END OF PROGRAM