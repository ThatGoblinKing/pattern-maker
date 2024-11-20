import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pattern Generator")
CANVAS = pygame.Surface((1200, 800))
CANVAS.fill(pygame.Color('white'))
PREVIEW_SURF = pygame.Surface((1200, 800), pygame.SRCALPHA)
PREVIEW_SURF.set_alpha(50)
from shapes import *

# Initialize font for instructions
font = pygame.font.Font(None, 36)

shapes = [Circle(30, (0,0,0), (0,0)),
        Rect(30, (0,0,0), (0,0)),
        nGon(5, 30, (0,0,0), (0,0)),
        Star(5,  .5,  30, (0,0,0), (0,0))]

selectedShape = shapes[0]

# Main game loop-------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                selectedShape.draw(CANVAS)

        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_4:
                temp = selectedShape.getScale()
                selectedShape = shapes[event.key - 49]
                selectedShape.scaleTo(temp)

        elif event.type == pygame.MOUSEWHEEL:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                if isinstance(selectedShape, Star):
                    selectedShape.changeValsBy(pointRatio=event.y/30)
            elif keys[pygame.K_LSHIFT]:
                if isinstance(selectedShape, Rect):
                    selectedShape.changeValsBy(aspectRatio=event.y/10)
                elif isinstance(selectedShape, nGon):
                    selectedShape.changeValsBy(points=event.y)
            else:
                selectedShape.changeValsBy(radius=event.y * 5)

    screen.blit(CANVAS, (0, 0))
    selectedShape.moveTo(pygame.mouse.get_pos())
    PREVIEW_SURF.fill(pygame.Color(0,0,0,0))
    selectedShape.draw(PREVIEW_SURF)
    screen.blit(PREVIEW_SURF, (0, 0))

    # Update the screen
    pygame.display.flip()

pygame.quit()

