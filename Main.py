from settings import *

from LocalPvP import PvP
from LocalPvE import PvE
from onlinePvP import oPvP
from classes import Button
pygame.init()

running = True

clock = pygame.time.Clock()


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
        self.localPvE_button = Button("LocalPvE", 170, 10, RED)
        self.onlinePvP_button = Button("OnlinePvP", 330, 10, RED)

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
        self.test2 = self.localPvE_button.click((self.mouse[0], self.mouse[1]))
        self.test3 = self.onlinePvP_button.click((self.mouse[0], self.mouse[1]))

    def update(self):
        if self.test and self.click[0] >= 1:
            print(self.click)
            self.localPvPrun = True
        if self.test2 and self.click[0] >= 1:
            print(self.click)
            self.localPvErun = True
        if self.test3 and self.click[0] >= 1:
            print(self.click)
            self.onlinePvPrun = True

    def draw(self):
        # Filling the Background
        self.screen.fill(DARKBLUE)
        self.localPvP_button.draw(self.screen)
        self.localPvE_button.draw(self.screen)
        self.onlinePvP_button.draw(self.screen)
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
                self.game = oPvP(self.screen)
                self.game.load_data()
                self.game.run()
                if not self.game.running:
                    self.onlinePvPrun = False

            self.events()
            self.update()
            self.draw()


g = Game()
g.load_data()
while g.running:
    g.run()

SCORE.close()
pygame.quit()
