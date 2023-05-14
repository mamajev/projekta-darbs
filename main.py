# Section: import needed libraries
import pygame
import os
import random


# Section: render game over menu when player dies
def game_over_menu(score):
    run = True
    while run:
        win.blit(bg, (0, 0))

        # Inner: draw info
        draw_text(win, "Game Over", WIDTH // 2 - 70, HEIGHT //
                  2, pygame.font.Font(FONT_PATH, 48))
        draw_text(win, f"Score: {score}", WIDTH //
                  2, HEIGHT // 2 - 20, SCORE_FONT)
        draw_text(win, "Press SPACE to play again or ESC to quit", WIDTH //
                  2 - 110, HEIGHT // 2 + 60, pygame.font.Font(FONT_PATH, 18))

        pygame.display.flip()

        # Inner: logic for the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    return True
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return False


# Section: function for drawing text on the screen
def draw_text(surface, text, x, y, font):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


# Info: Initialize Pygame
pygame.init()


# Section: Set up display
# Inner: Define display dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


# Section: Load assets
player_img = pygame.image.load(os.path.join('assets', 'player.png'))
enemy_img = pygame.image.load(os.path.join('assets', 'enemy.png'))
boss_img = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'boss.png')), (96, 96))
bullet_img = pygame.image.load(os.path.join('assets', 'bullet.png'))
obstacle_img = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'skerslis.png')), (96, 96))
bg = pygame.image.load(os.path.join('assets', 'background.jpg'))


# Section: define game variables
PLAYER_SPEED = 5
ENEMY_SPEED = 2
BOSS_SPEED = 3
BULLET_SPEED = 10
ENEMY_BULLET_SPEED = 4
BOSS_BULLET_SPEED = 8
ENEMY_FIRE_RATE = 0.01
BOSS_FIRE_RATE = 0.04
BOSS_LIVES = 15

# Section: set up font
pygame.font.init()
FONT_PATH = os.path.join("assets", "phantomstorm.ttf")
SCORE_FONT = pygame.font.Font(FONT_PATH, 24)
AUTHOR_FONT = pygame.font.Font(FONT_PATH, 16)


# Section: make Player class
class Player(pygame.sprite.Sprite):
    # Inner: initialize Player
    def __init__(self, x, y):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Inner: logic for updating Player position
    def update(self, keys):
        # Info: LEFT
        if keys[pygame.K_LEFT] and self.rect.x - PLAYER_SPEED > 0:
            self.rect.x -= PLAYER_SPEED

        # Info: RIGHT
        if keys[pygame.K_RIGHT] and self.rect.x + PLAYER_SPEED < WIDTH - self.rect.width:
            self.rect.x += PLAYER_SPEED

        # Info: UP
        if keys[pygame.K_UP] and self.rect.y - PLAYER_SPEED > 0:
            self.rect.y -= PLAYER_SPEED

        # Info: DOWN
        if keys[pygame.K_DOWN] and self.rect.y + PLAYER_SPEED < HEIGHT - self.rect.height:
            self.rect.y += PLAYER_SPEED


# Section: make Enemy class
class Enemy(pygame.sprite.Sprite):
    # Inner: initialize Enemy
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.choice([1, 2, 3])

    # Inner: update Enemy position
    def update(self):
        self.rect.y += self.speed


# Section: make Boss class
class Boss(pygame.sprite.Sprite):
    # Inner: initialize Boss
    def __init__(self, x, y):
        super().__init__()
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lives = BOSS_LIVES
        self.direction = 1

    # Inner: update Boss position
    def update(self):
        self.rect.x += self.direction * BOSS_SPEED
        if self.rect.x + self.rect.width >= WIDTH or self.rect.x <= 0:
            self.direction *= -1  # change direction when boss hits screen edge


# Section: make Obstacle class
class Obstacle(pygame.sprite.Sprite):

    # Inner: initialize Obstacle
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(64, WIDTH - 64 - self.rect.width)
        self.rect.y = random.randint(64, HEIGHT - 64 - self.rect.height)


# Section: make Bullet class
class Bullet(pygame.sprite.Sprite):
    # Inner: initialize Bullet
    def __init__(self, x, y, speed, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # Inner: update Bullet position
    def update(self):
        self.rect.y += self.speed


# Section: main game loop
def main():
    clock = pygame.time.Clock()
    run = True

    # Inner: initialize and group game sprites
    player = Player(WIDTH // 2, HEIGHT - 100)
    all_sprites = pygame.sprite.Group(player)
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    boss_bullets = pygame.sprite.Group()
    obstacle = Obstacle()
    all_sprites.add(obstacle)

    boss = None  # boss is initially None
    boss_counter = 0  # counter for how many enemies have been defeated

    # Inner: initialize score
    score = 0

    # Inner: game loop
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        # Info: check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.x + 16,
                                    player.rect.y, -BULLET_SPEED, bullet_img)
                    all_sprites.add(bullet)
                    player_bullets.add(bullet)

        # Info: update player object
        player.update(keys)

        # Info: spawn enemies
        if random.random() < 0.01 and boss is None:  # don't spawn enemies if boss is present
            x = random.randint(0, WIDTH - 64)
            enemy = Enemy(x, 0)
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Section: update and remove player bullets
        for bullet in player_bullets:

            bullet.update()
            # Inner: check if bullet hits obstacle
            if pygame.sprite.collide_rect(obstacle, bullet):
                all_sprites.remove(bullet)
                player_bullets.remove(bullet)

            # Inner: check if bullet is out of screen bounds
            elif bullet.rect.y < -32:
                all_sprites.remove(bullet)
                player_bullets.remove(bullet)

        # Section: update enemies and handle enemy bullets
        for enemy in enemies:
            enemy.update()
            # Inner: check if enemy is out of screen bounds
            if enemy.rect.y > HEIGHT:
                all_sprites.remove(enemy)
                enemies.remove(enemy)

            # Inner: randomly make enemy shoot a bullet
            if random.random() < ENEMY_FIRE_RATE:
                bullet = Bullet(enemy.rect.x + 16, enemy.rect.y,
                                ENEMY_BULLET_SPEED, pygame.transform.rotate(bullet_img, 180))
                all_sprites.add(bullet)
                enemy_bullets.add(bullet)

         # Section: update and remove enemy bullets
        for bullet in enemy_bullets:
            bullet.update()
            # Inner: check if bullet is out of screen bounds
            if bullet.rect.y > HEIGHT:
                all_sprites.remove(bullet)
                enemy_bullets.remove(bullet)

        # Section: update boss and handle boss bullets
        if boss is not None:
            boss.update()
            if random.random() < BOSS_FIRE_RATE:
                bullet = Bullet(boss.rect.x + 16, boss.rect.y,
                                ENEMY_BULLET_SPEED, pygame.transform.rotate(bullet_img, 180))
                all_sprites.add(bullet)
                boss_bullets.add(bullet)

        # Section: update and remove boss bullets
        for bullet in boss_bullets:
            bullet.update()
            # Inner: check if bullet is out of screen bounds
            if bullet.rect.y > HEIGHT:
                all_sprites.remove(bullet)
                boss_bullets.remove(bullet)

        # Section: check for collisions between player bullets and enemies
        hits = pygame.sprite.groupcollide(player_bullets, enemies, True, True)
        # Info: update score if hits occur
        if hits:
            score += len(hits)
            boss_counter += len(hits)
            if boss is None and boss_counter >= 50:
                boss = Boss(WIDTH // 2, 0)
                all_sprites.add(boss)

        # Section: check for collisions between player bullets and boss
        if boss is not None:
            hits = pygame.sprite.spritecollide(boss, player_bullets, True)
            boss.lives -= len(hits)
            if boss.lives <= 0:
                all_sprites.remove(boss)
                boss = None
                boss_counter = 0

        # Section: check for collisions between player and enemy bullets
        player_hit = pygame.sprite.spritecollide(player, enemy_bullets, True)

        # Section: check for collisions between player and boss bullets
        player_hit += pygame.sprite.spritecollide(player, boss_bullets, True)

        # Info: end game if player is hit
        if player_hit:
            play_again = game_over_menu(score)
            if play_again:
                main()
            else:
                return

        # Section: draw game objects

        # Info: draw background
        win.blit(bg, (0, 0))

        # Info: Draw score, high score, and author text
        draw_text(win, f"Score: {score}", WIDTH - 150, 10, SCORE_FONT)
        draw_text(win, "(c) Dmitrijs Mamajevs",
                  32,  HEIGHT-32, AUTHOR_FONT)

        # Info: draw all sprites
        all_sprites.draw(win)
        # Info: update the display
        pygame.display.flip()

    # Section: clean up
    pygame.quit()


# Section: run the game
if __name__ == "__main__":
    main()
