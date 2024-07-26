import pygame
import random
import os

# place Pygame window at a specific location
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

class Vehicle:
    def __init__(self) -> None:
        self.img_path = "sedan_red.png"
        self.location = 400, 400
        self.draw()
        
    def draw(self):
        # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location
        
# pygame settings
pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

car = Vehicle()
# set background colour
screen.fill("white")
# place image on the screen
screen.blit(car.img, car.img_location)

car.draw()

# start game loop
while running:
    # if we click on the "exit" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # stop game loop
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

