import random
from enum import Enum, unique
import pygame

@unique
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Cube(object):

    def __init__(self, pos, direction = None):
        self.pos = pos
        self.direction = direction

    def move(self):
        self.pos = (self.pos[0] + self.direction.value[0], self.pos[1] + self.direction.value[1])

    def draw(self, surface, length, color, eyes=False):
        x_coordinate = self.pos[0] * (length + 1) + 1
        y_coordinate = self.pos[1] * (length + 1) + 1

        pygame.draw.rect(surface, color, (x_coordinate, y_coordinate, length, length))
        if eyes:
            self._draw_eyes(surface, x_coordinate, y_coordinate, length)

    def _draw_eyes(self, surface, x_coordinate, y_coordinate, length):
        center = length // 2
        radius = 3

        circle_middle = (x_coordinate + center - radius, y_coordinate + center + 8)
        circle_middle2 = (x_coordinate +  2 * radius, y_coordinate + 8)

        color = (0, 255, 0)

        pygame.draw.circle(surface, color, circle_middle, radius)
        pygame.draw.circle(surface, color, circle_middle2, radius)


class Snake(object):

    def __init__(self, pos, direction):
        self._body = []
        self._turns = {}

        self._head = Cube(pos, direction)
        self._body.append(self._head)

    def _detect_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._turns[self._head.pos] = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self._turns[self._head.pos] = Direction.RIGHT
        elif keys[pygame.K_UP]:
            self._turns[self._head.pos] = Direction.UP
        elif keys[pygame.K_DOWN]:
            self._turns[self._head.pos] = Direction.DOWN

    def move(self):
        self._detect_event()

        for i, cube in enumerate(self._body):
            pos = cube.pos[:]
            if pos in self._turns.keys():
                cube.direction = self._turns[pos]
                if i == len(self._body) - 1:
                    self._turns.pop(pos)
            cube.move()

    def add_cube(self):
        tail = self._body[-1]

        cube_pos = ()
        cube_direction = tail.direction

        if cube_direction is Direction.RIGHT:
            cube_pos = (tail.pos[0] - 1, tail.pos[1])
        elif cube_direction is Direction.LEFT:
            cube_pos = (tail.pos[0] + 1, tail.pos[1])
        elif cube_direction is Direction.UP:
            cube_pos = (tail.pos[0], tail.pos[1] + 1)
        elif cube_direction is Direction.DOWN:
            cube_pos = (tail.pos[0], tail.pos[1] - 1)

        cube = Cube(cube_pos, cube_direction)
        self._body.append(cube)

    def draw(self, surface, length, color):
        for i, cube in enumerate(self._body):
            cube.draw(surface, length, color, i == 0)

    def contains(self, pos):
        return len(list(filter(lambda cube: cube.pos == pos, self._body))) != 0

    def can_eat(self, pos):
        return self._head.pos == pos

    def is_fail(self, rows):
        pos = self._head.pos
        if pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >=  rows:
            return True

        if len(list(filter(lambda cube: cube.pos == pos, self._body[1:]))) != 0:
            return True

        return False

class Screen(object):

    _WHITE_COLOR  = (255, 255, 255)

    _RED_COLOR = (255, 0, 0)

    def __init__(self, width, rows):
        self._gap = width // rows
        self._width =  self._gap * rows + rows + 1
        self._rows = rows
        self._snake = Snake((rows // 2, rows // 2), self._random_direction())
        self._snack = self._random_snack()

        pygame.font.init()
        self._font = pygame.font.SysFont(None, 72)

        self._surface = pygame.display.set_mode((self._width, self._width))
        pygame.display.set_caption('Snake')     

    def _draw(self):
        self._surface.fill((0, 0, 0))
        space = 0
        while space <= self._width:
            pygame.draw.line(self._surface, self._WHITE_COLOR, (space, 0), (space, self._width))
            pygame.draw.line(self._surface, self._WHITE_COLOR, (0, space), (self._width, space))
            space+= self._gap + 1

        self._snack.draw(self._surface, self._gap, self._RED_COLOR)
        self._snake.draw(self._surface, self._gap, self._RED_COLOR)
        pygame.display.update()

    def _random_snack(self):
        while True:
            pos = (random.randrange(self._rows),random.randrange(self._rows))
            if not self._snake.contains(pos):
                break
        return Cube(pos)

    def _random_direction(self):
        return random.choice(list(Direction))

    def _eat_snack(self):
        pos = self._snack.pos
        if not self._snake.can_eat(pos):
            return
        self._snake.add_cube()
        self._snack = self._random_snack()

    def play(self):
        clock = pygame.time.Clock()
        while True:
            pygame.time.delay(120)
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                    
            if self._snake.is_fail(self._rows):
                self._snake = Snake((self._rows // 2, self._rows // 2), self._random_direction())
                continue

            self._snake.move()
            self._eat_snack()

            self._draw()


screen = Screen(600, 30)
screen.play()
