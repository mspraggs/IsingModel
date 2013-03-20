import lattice
import pygame

pygame.init()
fpsClock = pygame.time.Clock()

screen_size = (640,640)
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Ising Model')
screen = pygame.display.get_surface()

