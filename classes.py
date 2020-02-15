from settings import *
from random import randint


class animation:
    def __init__(self, screen, entity):
        self.screen = screen
        self.entity = entity

#TODO making the
class Text:
    def __init__(self, screen, text, font, size, color, x, y):
        self.screen = screen
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.rect = (x, y)
        self.font = pygame.font.Font(self.font, self.size)
        self.surf_rect = self.font.render(self.text, True, self.color)
        self.align = "tl"

    def set_align(self, align="tl"):
        if align == "tl":
            self.surf_rect.topleft = (self.rect[0], self.rect[1])
        if align == "tr":
            self.surf_rect.topright = (self.rect[0], self.rect[1])
        if align == "bl":
            self.surf_rect.bottomleft = (self.rect[0], self.rect[1])
        if align == "br":
            self.surf_rect.bottomright = (self.rect[0], self.rect[1])
        if align == "mt":
            self.surf_rect.midtop = (self.rect[0], self.rect[1])
        if align == "mb":
            self.surf_rect.midbottom = (self.rect[0], self.rect[1])
        if align == "mr":
            self.surf_rect.midright = (self.rect[0], self.rect[1])
        if align == "ml":
            self.surf_rect.midleft = (self.rect[0], self.rect[1])
        if align == "center":
            self.surf_rect.center = (self.rect[0], self.rect[1])

    def draw(self):
        self.set_align(self.align)


class Box:
    def __init__(self, surface, size, rect, color, times, font=None):
        self.screen = surface
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
        self.frame.fill(DARKBLUE)
        for box in self.list:
            self.frame.blit(self.frame, box)
            pygame.draw.rect(self.frame, self.color, box, 5)


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
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2)
                        - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class Paddle(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y > 400:
            self.rect.y = 400


class Ball(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image, WHITE, (int(width/2), int(height/2)), int(width/2))

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)