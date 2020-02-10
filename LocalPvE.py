from settings import *

from classPaddle import Paddle
from ball import Ball


class Box:
    def __init__(self, surface, text, size, rect, color, times, font=None):
        self.screen = surface
        self.text = text
        self.font = font
        self.size = size
        self.rect = rect
        self.times = times
        self.color = color
        self.list = []

        self.frame_rect = []
        self.box_rect = [0, 0, self.rect[2], self.rect[3]]
        self.making_boxes()
        self.frame = pygame.Surface((self.frame_rect[2], self.frame_rect[3]))

    def making_boxes(self):
        if self.times > 1:
            self.convrect = list(self.rect)
            for box in range(self.times):
                print("bla")
                box = pygame.Rect(tuple(self.box_rect))
                self.list.append(box)

                self.box_rect[1] += self.rect[3]


                self.convrect[1] += self.rect[3]
                self.convrect[3] += self.rect[3]
            self.frame_rect = tuple(self.convrect)
            print(self.frame_rect)
        else:
            pass

    def draw(self):
        self.screen.blit(self.frame, (self.rect[0], self.rect[1]))
        self.frame.fill(WHITE)
        for box in self.list:
            self.frame.blit(self.frame, box)
            pygame.draw.rect(self.frame, self.color, box, 5)


class PvE:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.countdown = True
        self.end = False
        self.timer_color = WHITE
        self.count = 4
        self.time = 5
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
        try:
            self.score = SCORE["player"]
        except:
            SCORE["player"] = 0
            self.score = SCORE["player"]


        self.score_box = Box(self.screen, "test", 10, (100, 200, 400, 100), RED, 3)


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

        if not self.end:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddleA.moveUp(5)
            if keys[pygame.K_s]:
                self.paddleA.moveDown(5)

        else:
            SCORE["player"] = self.scoreA, self.scoreB

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

        # Here Comes the Bot
        if self.paddleB.rect.y >= self.ball.rect.y:
            self.paddleB.moveUp(5)
        elif self.paddleB.rect.y <= self.ball.rect.y:
            self.paddleB.moveDown(5)

            # Detect collisions between the ball and the paddles
        if pygame.sprite.spritecollide(self.ball, self.liste1, False) and self.ball.velocity[0] < 0:
            print("LEFT  --", self.ball.velocity)
            self.ball.bounce()

        if pygame.sprite.spritecollide(self.ball, self.liste2, False) and self.ball.velocity[0] > 0:
            print("RIGHT  --", self.ball.velocity)
            self.ball.bounce()

    def draw(self):
        self.screen.fill(DARKBLUE)
        if not self.countdown:
            self.draw_text(f"{int((self.time-self.time_remaining)/60)} : {int(self.time-self.time_remaining)%60}",
                           None, 70, self.timer_color, 300, 20)
            if not self.end:
                pygame.draw.line(self.screen, WHITE, [349, 80], [349, 500], 5)
        if not self.end:
            self.all_sprites_list.draw(self.screen)
        if self.countdown:
            self.draw_text(f"{int(self.count-self.seconds)} ", None, 100, WHITE, 330, 100)

        self.draw_text(f"{self.scoreA}", None, 50, WHITE, 220, 10)
        self.draw_text(f"{self.scoreB}", None, 50, WHITE, 450, 10)

        if self.end:
            self.score_box.draw()

        pygame.display.update()

    def run(self):
        self.start_ticks = pygame.time.get_ticks()
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            if not self.countdown and not self.end:

                self.update()
            else:
                self.seconds=(pygame.time.get_ticks()-self.start_ticks) / 1000
                if self.seconds >self.count:
                    self.countdown = False
            if not self.end:
                self.time_remaining = (pygame.time.get_ticks() - self.start_ticks) / 1000

            if self.time - self.time_remaining < 0:
                self.end = True
            if (self.time - self.time_remaining -10) <= 0:
                self.timer_color = RED
            self.draw()