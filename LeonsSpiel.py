from settings import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.running = True
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        'Hier lädst du all deine daten wie Bilder'

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        'Hier updatest du all deine Kein Plan'

    def draw(self):
        pygame.display.update()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.event()
            self.update()
            self.draw()


g = Game()

while g.running:
    g.run()

pygame.quit()
