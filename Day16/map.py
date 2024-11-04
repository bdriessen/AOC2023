from foton import Foton
from icecream import ic

class Map:
    def __init__(self, pattern):
        self.map = pattern
        self.width = len(pattern[0])
        self.height = len(pattern)
        self.fotons = []
        # Create a 2D list with dimensions of pattern and filled with 0.
        self.visited = [[0 for x in range(self.width)] for y in range(self.height)]

    def add_foton(self, foton):
        self.fotons.append(foton)

    def move_fotons(self):
        for foton in self.fotons:
            foton.move()
            # Check if foton is outside the map
            if foton.pos[0] < 0 or foton.pos[0] >= self.width or foton.pos[1] < 0 or foton.pos[1] >= self.height:
                self.fotons.remove(foton)
                continue
            x = foton.pos[0]
            y = foton.pos[1]
            self.visited[y][x] = 1

            if self.map[y][x] == '/':
                if foton.direction == 'N':
                    foton.direction = 'E'
                elif foton.direction == 'S':
                    foton.direction = 'W'
                elif foton.direction == 'E':
                    foton.direction = 'N'
                elif foton.direction == 'W':
                    foton.direction = 'S'
            elif self.map[y][x] == '\\':
                if foton.direction == 'N':
                    foton.direction = 'W'
                elif foton.direction == 'S':
                    foton.direction = 'E'
                elif foton.direction == 'E':
                    foton.direction = 'S'
                elif foton.direction == 'W':
                    foton.direction = 'N'
            elif self.map[y][x] == '|':
                if foton.direction == 'W' or foton.direction == 'E':
                    foton.direction = 'N'
                    # Create a new foton
                    extra_foton = Foton([x, y], 'S')
                    self.add_foton(extra_foton)
            elif self.map[y][x] == '-':
                if foton.direction == 'N' or foton.direction == 'S':
                    foton.direction = 'E'
                    # Create a new foton
                    extra_foton = Foton([x, y], 'W')
                    self.add_foton(extra_foton)
        ic(self.visited)


    def act_fotons(self):
        for foton in self.fotons:
            foton.act(self.map)






