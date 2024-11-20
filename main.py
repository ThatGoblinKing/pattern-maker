import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pattern Generator")
CANVAS = pygame.Surface((1200, 800))
CANVAS.fill(pygame.Color('white'))
PREVIEW_SURF = pygame.Surface((1200, 800), pygame.SRCALPHA)
PREVIEW_SURF.set_alpha(50)
from shapes import *

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Starting settings
current_color = RED
current_shape = "triangle"
SHAPE_SIZE = 40

# List of shapes (each shape is: [x, y, size, color, type])
shapeList = [] #this is going to be a LIST of LISTS!

# Initialize font for instructions
font = pygame.font.Font(None, 36)

testStar = Star(8,  10, 30, (0,0,0), (50,50))
testStar.draw(CANVAS)
print(testStar)

# Main game loop-------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                testStar.draw(CANVAS)
                


    screen.blit(CANVAS, (0, 0))
    testStar.moveTo(pygame.mouse.get_pos())
    PREVIEW_SURF.fill(pygame.Color(0,0,0,0))
    testStar.draw(PREVIEW_SURF)
    screen.blit(PREVIEW_SURF, (0, 0))

    # Update the screen
    pygame.display.flip()

pygame.quit()

