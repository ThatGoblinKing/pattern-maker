import pygame
from math import cos, sin, pi as PI


class Shape():
    def __init__(self, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        if max(color) > 255 or min(color) < 0:
            raise ValueError("RGB Values must be between 0 and 255")
        self.color = color
        self.pos = pos
        self.radius = radius
    def draw(self, canvas):
        pass

    def moveTo(self, newPos, *args, **kwargs):
        self.pos = newPos

    def changeValsBy(self, radius):
        self.radius += radius if 0 < self.radius + radius else 0

    def scaleTo(self, newScale: int):
        self.radius = newScale

    def getScale(self):
        return self.radius

    def updateColor(self, newColor):
        self.color = newColor

class Circle(Shape):
    def __init__(self, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        super().__init__(radius, color, pos)
        self.radius = radius

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, self.pos, self.radius)

class NGon(Shape):
    def __init__(self, sides: int, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        super().__init__(radius, color, pos)
        self.sides = sides
        self.radius = radius

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
        pointRads = (2 * PI)/self.sides
        for i in range(self.sides):
            theta = (-PI/2) + (i * pointRads)
            pointCoords.append((int(self.radius * cos(theta) + self.pos[0]), int(self.radius * sin(theta) + self.pos[1])))
        return pointCoords

    def changeValsBy(self, points: int = 0, radius: int = 0):
        self.sides += points if self.sides + points > 2 else 0
        self.radius += radius if self.radius + radius > 0  else 0


class Star(NGon):
    def __init__(self, sides: int, pointCenterRatio: float, radius: int, color: tuple[int, int, int], pos: tuple[int, int]):
        super().__init__(sides, radius, color, pos)
        self.sides = sides
        self.pcRatio = pointCenterRatio

    def __repr__(self):
        return (f"Star Object at <{hex(id(self))}>\n"
                f"\tColor: R: {self.color[0]} G: {self.color[1]} B: {self.color[2]}\n"
                f"\tPoint Count: {self.sides}\n"
                f"\tInner Rad: {self.innerRadius}\n"
                f"\tOuter Rad: {self.radius}\n"
                f"\tPos: {self.pos}\n"
                f"\tPoint Coords: {self.getPointCoords()}")

    def draw(self, canvas):
        pygame.draw.polygon(canvas, self.color, self.getPointCoords())


    def getPointCoords(self) -> list[tuple[int, int]]:
        self.innerRadius = self.radius * self.pcRatio
        offset = 1.5
        pointCoords: list[tuple[int, int]] = []
        pointRads = (2 * PI)/(self.sides * 2)
        for i in range(self.sides * 2):
            theta = (-PI/2) + (i * pointRads)
            if i%2 == 0:
                pointCoords.append((int(self.radius * cos(theta) + self.pos[0]), int(self.radius * sin(theta) + self.pos[1])))
            else:
                pointCoords.append((int(self.innerRadius * cos(theta) + self.pos[0]), int(self.innerRadius * sin(theta) + self.pos[1])))
        return pointCoords

    def changeValsBy(self, points: int = 0, pointRatio: int = 0, radius: int = 0):
        self.sides += points if self.sides + points > 1 else 0
        self.radius += radius if 0 < self.radius + radius else 0
        self.pcRatio += pointRatio if 0 < self.pcRatio + pointRatio < 2 else 0


class Rect(Shape):
    def __init__(self, size: int, color: tuple[int, int, int], pos: tuple[int, int], aspectRatio: int = 1):
        super().__init__(size, color, pos)
        self.aspectRatio = aspectRatio

    def draw(self, canvas):
        if self.aspectRatio < 1:
            height = self.radius * 2
            width = self.radius * self.aspectRatio * 2
        else:
            width = self.radius * 2
            height = self.radius / self.aspectRatio * 2
        center = (self.pos[0] - width // 2, self.pos[1] - height // 2)
        pygame.draw.rect(canvas, self.color, (center[0], center[1], width, height))

    def changeValsBy(self, radius = 0, aspectRatio = 0):
        super().changeValsBy(radius)
        self.aspectRatio += aspectRatio if self.aspectRatio + aspectRatio > 0 else 0