import pygame
import random

pygame.init()

screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0
cellSize = screen.get_width() / 18
circleRadius = 20

currentDirection = None
playerPosition = pygame.Vector2(screen.get_width() / 2 - 20, screen.get_height() / 2 - 20)
foodPosition = pygame.Vector2(random.randint(1, 18) * 40 - 20, random.randint(1, 18) * 40 - 20)


def display_text(text, font_size, x, y):
    font = pygame.font.SysFont("Arial", font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rec = text_surface.get_rect()
    text_rec.center = (x, y)
    screen.blit(text_surface, text_rec)
    pygame.display.flip()


def draw_grid():
    for x in range(0, screen.get_width(), 40):
        pygame.draw.line(screen, "white", (x, 0), (x, screen.get_height()))
    for y in range(0, screen.get_height(), 40):
        pygame.draw.line(screen, "white", (0, y), (screen.get_width(), y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if playerPosition.x <= 0 + circleRadius - 1 or playerPosition.x >= screen.get_width() - circleRadius + 1 or \
       playerPosition.y <= 0 + circleRadius - 1 or playerPosition.y >= screen.get_height() - circleRadius + 1:
        display_text("Game Over", 100, screen.get_width() / 2, screen.get_height() / 2)
        display_text("Press R to restart", 50, screen.get_width() / 2, screen.get_height() / 2 + 100)
        currentDirection = None

    if currentDirection is not None:
        screen.fill("black")

    draw_grid()
    pygame.draw.circle(screen, "green", playerPosition, circleRadius)
    pygame.draw.circle(screen, "red", foodPosition, circleRadius)

    if currentDirection == "left":
        playerPosition.x -= 40
    elif currentDirection == "right":
        playerPosition.x += 40
    elif currentDirection == "up":
        playerPosition.y -= 40
    elif currentDirection == "down":
        playerPosition.y += 40

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        currentDirection = 'up'
    if key[pygame.K_DOWN]:
        currentDirection = 'down'
    if key[pygame.K_LEFT]:
        currentDirection = 'left'
    if key[pygame.K_RIGHT]:
        currentDirection = 'right'
    if key[pygame.K_r]:
        currentDirection = None
        screen.fill("black")
        playerPosition = pygame.Vector2(screen.get_width() / 2 - 20, screen.get_height() / 2 - 20)
        foodPosition = pygame.Vector2(random.randint(1, 18) * 40 - 20, random.randint(1, 18) * 40 - 20)

    pygame.display.flip()

    dt = clock.tick(15) / 1000

pygame.quit()

