from settings import *
from LocalPvP import PvP
from LocalPvE import PvE

pygame.init()

running = True

clock = pygame.time.Clock()


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.onlinePvPrun = False
        self.localPvErun = False
        self.screen = pygame.display.set_mode(SIZE)
        self.running = True
        self.localPvPrun = False
        self.clock = pygame.time.Clock()
        self.button = Button
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
        self.yes1 = pygame.image.load("rec/yes.png")
        self.yes2 = pygame.image.load("rec/yes2.png")
        self.no1 = pygame.image.load("rec/no.png")
        self.no2 = pygame.image.load("rec/no2.png")
        self.localPvP_button = Button("LocalPvP", 10, 10, RED)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.localPvErun = True
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.test = self.localPvP_button.click((self.mouse[0], self.mouse[1]))
        if self.test and self.click:
            print(self.click)
            self.localPvPrun = True

    def update(self):
        """
        Updating all sprites or checking for collides
        """

    def draw(self):
        # Filling the Background
        self.screen.fill(DARKBLUE)
        self.localPvP_button.draw(self.screen)
        self.draw_text(f"{int(self.dt*1000.0)}", None, 25, RED, 0, 0)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            if self.localPvPrun:
                self.game = PvP(self.screen)
                self.game.load_data()
                self.game.run()
                if not self.game.running:
                    self.localPvPrun = False
            if self.localPvErun:
                self.game = PvE(self.screen)
                self.game.load_data()
                self.game.run()
                if not self.game.running:
                    self.localPvErun = False
            if self.onlinePvPrun:
                pass

            self.events()
            self.update()
            self.draw()


g = Game()
g.load_data()
while g.running:
    g.run()

pygame.quit()
