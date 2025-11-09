import pygame, random, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - Add More Sprites")
font = pygame.font.Font(None, 36)

player = pygame.Rect(370, 480, 50, 50)
enemies = [pygame.Rect(random.randint(0, 750), random.randint(50, 400), 50, 50) for _ in range(7)]
speed = 5
score = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < 550:
        player.y += speed

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 750)
            enemy.y = random.randint(50, 400)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
