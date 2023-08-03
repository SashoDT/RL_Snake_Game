import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

currentDirection = None
playerPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
foodPosition = pygame.Vector2()


def display_text(text, font_size, x, y):
    font = pygame.font.SysFont("Arial", font_size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rec = text_surface.get_rect()
    text_rec.center = (x, y)
    screen.blit(text_surface, text_rec)
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if playerPosition.x <= 0 or playerPosition.x >= screen.get_width() or \
       playerPosition.y <= 0 or playerPosition.y >= screen.get_height():
        display_text("Game Over", 100, screen.get_width() / 2, screen.get_height() / 2)
        display_text("Press R to restart", 50, screen.get_width() / 2, screen.get_height() / 2 + 100)
        currentDirection = None

    if currentDirection is not None:
        screen.fill("black")

    pygame.draw.circle(screen, "green", playerPosition, 10)

    if currentDirection == "left":
        playerPosition.x -= 300 * dt
    elif currentDirection == "right":
        playerPosition.x += 300 * dt
    elif currentDirection == "up":
        playerPosition.y -= 300 * dt
    elif currentDirection == "down":
        playerPosition.y += 300 * dt

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
        screen.fill("black")
        playerPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

