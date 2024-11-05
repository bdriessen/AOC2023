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
        self.visited_north = [[0 for x in range(self.width)] for y in range(self.height)]
        self.visited_south = [[0 for x in range(self.width)] for y in range(self.height)]
        self.visited_east = [[0 for x in range(self.width)] for y in range(self.height)]
        self.visited_west = [[0 for x in range(self.width)] for y in range(self.height)]

    def add_foton(self, foton):
        self.fotons.append(foton)

    def init_fotons(self, foton):
        # Enter the first foton
        row = foton.pos[0]
        col = foton.pos[1]
        dir = foton.direction
        self.visited[row][col] = 1
        if dir == 'N':
            self.visited_north[row][col] = 1
        elif dir == 'S':
            self.visited_south[row][col] = 1
        elif dir == 'E':
            self.visited_east[row][col] = 1
        elif dir == 'W':
            self.visited_west[row][col] = 1

        if self.map[row][col] == '|':
            if dir == 'W' or dir == 'E':
                foton.direction = 'N'
                # Create a new foton
                extra_foton = Foton([row, col], 'S')
                self.add_foton(extra_foton)
                self.visited_south[row][col] = 1
        elif self.map[row][col] == '-':
            if dir == 'N' or dir == 'S':
                foton.direction = 'E'
                # Create a new foton
                extra_foton = Foton([row, col], 'W')
                self.add_foton(extra_foton)
                self.visited_west[row][col] = 1
        elif self.map[row][col] == '/':
            if dir == 'N':
                foton.direction = 'E'
            elif dir == 'S':
                foton.direction = 'W'
            elif dir == 'E':
                foton.direction = 'N'
            elif dir == 'W':
                foton.direction = 'S'
        elif self.map[row][col] == '\\':
            if dir == 'N':
                foton.direction = 'W'
            elif dir == 'S':
                foton.direction = 'E'
            elif dir == 'E':
                foton.direction = 'S'
            elif dir == 'W':
                foton.direction = 'N'


    def move_fotons(self):
        for foton in self.fotons:
            # Update position of foton
            foton.move()
            row = foton.pos[0]
            col = foton.pos[1]
            # Check if foton is outside the map
            if foton.pos[0] < 0 or foton.pos[0] >= self.height or foton.pos[1] < 0 or foton.pos[1] >= self.width:
                self.fotons.remove(foton)
                continue
            # Check if foton has already visited this cell in given directions
            if self.visited_north[row][col] == 1 and foton.direction == 'N':
                self.fotons.remove(foton)
                continue
            if self.visited_south[row][col] == 1 and foton.direction == 'S':
                self.fotons.remove(foton)
                continue
            if self.visited_east[row][col] == 1 and foton.direction == 'E':
                self.fotons.remove(foton)
                continue
            if self.visited_west[row][col] == 1 and foton.direction == 'W':
                self.fotons.remove(foton)
                continue

            self.visited[row][col] = 1
            if foton.direction == 'N':
                self.visited_north[row][col] = 1
            elif foton.direction == 'S':
                self.visited_south[row][col] = 1
            elif foton.direction == 'E':
                self.visited_east[row][col] = 1
            elif foton.direction == 'W':
                self.visited_west[row][col] = 1


            # Update direction of foton

            if self.map[row][col] == '/':
                if foton.direction == 'N':
                    foton.direction = 'E'
                elif foton.direction == 'S':
                    foton.direction = 'W'
                elif foton.direction == 'E':
                    foton.direction = 'N'
                elif foton.direction == 'W':
                    foton.direction = 'S'
            elif self.map[row][col] == '\\':
                if foton.direction == 'N':
                    foton.direction = 'W'
                elif foton.direction == 'S':
                    foton.direction = 'E'
                elif foton.direction == 'E':
                    foton.direction = 'S'
                elif foton.direction == 'W':
                    foton.direction = 'N'
            elif self.map[row][col] == '|':
                if foton.direction == 'W' or foton.direction == 'E':
                    foton.direction = 'N'
                    # Create a new foton
                    extra_foton = Foton([row, col], 'S')
                    self.add_foton(extra_foton)
                    self.visited_south[row][col] = 1
            elif self.map[row][col] == '-':
                if foton.direction == 'N' or foton.direction == 'S':
                    foton.direction = 'E'
                    # Create a new foton
                    extra_foton = Foton([row, col], 'W')
                    self.add_foton(extra_foton)
                    self.visited_west[row][col] = 1
        ic(self.visited)




