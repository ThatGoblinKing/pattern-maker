import pygame
from math import cos, sin, pi as PI
class Shape():
    def __init__(self, color: tuple[int, int, int], pos: tuple[int, int]):
        if max(color) > 255 or min(color) < 0:
            raise ValueError("RGB Values must be between 0 and 255")
        self.color = color
        self.pos = pos
    def draw(self, canvas):
        pass

    def moveTo(self, newPos):
        self.pos = newPos


class Circle(Shape):
    def __init__(self, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        super().__init__(color, pos)
        self.radius = radius

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, self.pos, self.radius)

class Star(Circle):
    def __init__(self, points: int, innerRadius: int, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        super().__init__(radius, color, pos)
        self.points = points
        self.innerRadius = innerRadius

    def __repr__(self):
        return (f"Star Object at <{hex(id(self))}>\n"
                f"\tColor: R: {self.color[0]} G: {self.color[1]} B: {self.color[2]}\n"
                f"\tPoint Count: {self.points}\n"
                f"\tInner Rad: {self.innerRadius}\n"
                f"\tOuter Rad: {self.radius}\n"
                f"\tPos: {self.pos}\n"
                f"\tPoint Coords: {self.getPointCoords()}")

    def draw(self, canvas):
        pygame.draw.polygon(canvas, self.color, self.getPointCoords())


    def getPointCoords(self) -> list[tuple[int, int]]:
        offset = 1.5
        pointCoords: list[tuple[int, int]] = []
        pointRads = (2 * PI)/(self.points * 2)
        for i in range(self.points * 2):
            theta = (-PI/2) + (i * pointRads)
            if i%2 == 0:
                pointCoords.append((int(self.radius * cos(theta) + self.pos[0]), int(self.radius * sin(theta) + self.pos[1])))
            else:
                pointCoords.append((int(self.innerRadius * cos(theta) + self.pos[0]), int(self.innerRadius * sin(theta) + self.pos[1])))
        return pointCoords

    def changeValsBy(self, points: int = 0, innerRadius: int = 0, radius: int = 0):
        self.points += points
        self.innerRadius += innerRadius
        self.radius += radius