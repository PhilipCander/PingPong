from settings import *
from classes import Paddle, Ball


class PvP:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.scoreA = 0
        self.scoreB = 0
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        self.font = pygame.font.Font(None, 34)
        self.paddleA = Paddle(WHITE, 20, 100)
        self.paddleA.rect.x = 10
        self.paddleA.rect.y = 200

        self.paddleB = Paddle(WHITE, 20, 100)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200

        self.ball = Ball(WHITE, 10, 10)
        self.ball.rect.x = 345
        self.ball.rect.y = 195

        # This will be a list that will contain all the sprites we intend to use in our game.
        self.all_sprites_list = pygame.sprite.Group()
        self.liste1 = pygame.sprite.Group()
        self.liste2 = pygame.sprite.Group()

        self.liste1.add(self.paddleA)
        self.liste2.add(self.paddleB)
        # Add the car to the list of objects
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddleA.moveUp(5)
        if keys[pygame.K_s]:
            self.paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            self.paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            self.paddleB.moveDown(5)

    def update(self):
        self.all_sprites_list.update()
        if self.ball.rect.x >= 680:
            self.scoreA += 1
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.x <= 10:
            self.scoreB += 1
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.y > 490:
            self.ball.velocity[1] = -self.ball.velocity[1]
        if self.ball.rect.y < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

            # Detect collisions between the ball and the paddles
        if pygame.sprite.spritecollide(self.ball, self.liste1, False) and self.ball.velocity[0] < 0:
            print("LEFT  --", self.ball.velocity)
            self.ball.bounce()

        if pygame.sprite.spritecollide(self.ball, self.liste2, False) and self.ball.velocity[0] > 0:
            print("RIGHT  --", self.ball.velocity)
            self.ball.bounce()

    def draw(self):
        self.screen.fill(DARKBLUE)
        pygame.draw.line(self.screen, WHITE, [349, 0], [349, 500], 5)
        self.all_sprites_list.draw(self.screen)

        self.draw_text(f"{self.scoreA}", None, 50, WHITE, 250, 10)
        self.draw_text(f"{self.scoreB}", None, 50, WHITE, 420, 10)

        pygame.display.update()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()
