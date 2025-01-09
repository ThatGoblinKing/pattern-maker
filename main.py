from shapes import Shape, Circle, Rect, NGon, Star
import pygame

pygame.init()

SCREEN_SIZE = (1200, 800)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pattern Generator")
CANVAS = pygame.Surface(SCREEN_SIZE)
CANVAS.fill(pygame.Color('white'))
PREVIEW_SURF = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
PREVIEW_SURF.set_alpha(50)
COLOR_WHEEL_SURF = pygame.image.load('ColorPicker.bmp')
COLOR_WHEEL_RECT = COLOR_WHEEL_SURF.get_rect()
canDraw = True

COLOR_WHEEL_CENTER = (SCREEN_SIZE[0] - COLOR_WHEEL_RECT.width//2, SCREEN_SIZE[1] - COLOR_WHEEL_RECT.height//2)
color_select_pos = COLOR_WHEEL_CENTER
selectedColor = (0,0,0)
# Initialize font for instructions
font = pygame.font.Font(None, 36)

shapes = [Circle(30, (0,0,0), (0,0)),
          Rect(30, (0,0,0), (0,0)),
          NGon(5, 30, (0, 0, 0), (0, 0)),
          Star(5,  .5,  30, (0,0,0), (0,0))]

selectedShape = shapes[0]

# Main game loop-------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] :
                if canDraw:
                    selectedShape.draw(CANVAS)
                else:
                    selectedColor = screen.get_at(pygame.mouse.get_pos())
                    color_select_pos = pygame.mouse.get_pos()
                    for shape in shapes:
                        shape.updateColor(selectedColor)


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
                elif isinstance(selectedShape, NGon):
                    selectedShape.changeValsBy(points=event.y)
            else:
                selectedShape.changeValsBy(radius=event.y * 5)

    screen.blit(CANVAS, (0, 0))
    selectedShape.moveTo(pygame.mouse.get_pos())
    PREVIEW_SURF.fill(pygame.Color(0,0,0,0))
    canDraw = not (abs(pygame.mouse.get_pos()[0] - COLOR_WHEEL_CENTER[0]) < 125 and abs(pygame.mouse.get_pos()[1] - COLOR_WHEEL_CENTER[1]) < 125)

    if canDraw:
        selectedShape.draw(PREVIEW_SURF)


    screen.blit(COLOR_WHEEL_SURF, (SCREEN_SIZE[0] - COLOR_WHEEL_RECT.width, SCREEN_SIZE[1] - COLOR_WHEEL_RECT.height))
    screen.blit(PREVIEW_SURF, (0, 0))
    pygame.draw.circle(screen, selectedColor, color_select_pos, 10)
    pygame.draw.circle(screen, (255, 255, 255),  color_select_pos, 10, 2)

    # Update the screen
    pygame.display.flip()

pygame.quit()

