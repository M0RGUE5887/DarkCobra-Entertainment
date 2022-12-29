##DeathBreach.com
##File: Lanch_Pad
##v1.0.2022
##---------------
##Load Librarys:
#pygame
import pygame
pygame.init()
#pyglet
import pyglet
#usina
from ursina import *
#other librarys
import random

##Preload Variables:
loading_time = random.randint(1200, 2500)
running = True
#Colors:
white = (255, 255, 255)
black = (0, 0, 0)
backround1 = (57, 57, 57)
line1 = (127, 127, 127)
text1 = (266, 266, 266)

##Loading Window:
window_load = pygame.display.set_mode([1500, 1000])
print("Loading...")
pygame.time.wait(loading_time)
print("Done!")

##Main Window:
#Window Disign:
window_lp = pygame.display.set_mode([1500, 1000])
window_lp.fill((backround1))
pygame.draw.line(window_lp, line1, (0,0), (1500, 0))

#Window Run:
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()
    clock.tick(60)

"""
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
"""
##Launch Pad Close:
pygame.quit()
quit()