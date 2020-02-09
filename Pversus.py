from settings import *
from classPaddle import Paddle
from ball import Ball

# initialise from classPaddle
paddleA = Paddle(WHITE, 20, 100)
paddleA.rect.x = 10
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 20, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
liste1 = pygame.sprite.Group()
liste2 = pygame.sprite.Group()

liste1.add(paddleA)
liste2.add(paddleB)
# Add the car to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


run = True

clock = pygame.time.Clock()

# Initialise player scores
scoreA = 0
scoreB = 0

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    # moving players paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

        # --- Game logic should go here
    all_sprites_list.update()

    # Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 680:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 10:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

        # Detect collisions between the ball and the paddles
    if pygame.sprite.spritecollide(ball, liste1, False) and ball.velocity[0] < 0:
        print("LEFT  --", ball.velocity)
        ball.bounce()

    if pygame.sprite.spritecollide(ball, liste2, False) and ball.velocity[0] > 0:
        print("RIGHT  --", ball.velocity)
        ball.bounce()

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill((0, 0, 20))
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # Display scores:
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)