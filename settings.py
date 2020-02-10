import pygame
import shelve
SCORE = shelve.open("score.txt")
pygame.init()
SIZE = (700, 500)
pygame.display.set_caption("Pong")
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
DARKBLUE = (0, 0, 20)
font = pygame.font.Font(None, 74)
FPS = 60
# Open game window
