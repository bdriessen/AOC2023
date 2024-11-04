import map

class Foton:
    def __init__(self, map):
        self.pos = [0, 0]
        self.direction = 'E'
        self.map = map

    def __init__(self, map, pos, direction):
        self.pos = pos
        self.direction = direction

    def move(self, direction):
        if direction == 'N':
            self.pos[1] += 1
        elif direction == 'S':
            self.pos[1] -= 1
        elif direction == 'E':
            self.pos[0] += 1
        elif direction == 'W':
            self.pos[0] -= 1
        else:
            print("Invalid direction")
        # Check if foton is outside the map is done in the map class



    def act(self, map):
        x = self.pos[0]
        y = self.pos[1]
        if map[y][x] == '/':
            if self.direction == 'N':
                self.direction = 'E'
            elif self.direction == 'S':
                self.direction = 'W'
            elif self.direction == 'E':
                self.direction = 'N'
            elif self.direction == 'W':
                self.direction = 'S'
        elif map[y][x] == '\\':
            if self.direction == 'N':
                self.direction = 'W'
            elif self.direction == 'S':
                self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'S'
            elif self.direction == 'W':
                self.direction = 'N'
        elif map[y][x] == '|':
            if self.direction == 'W' or self.direction == 'E':
                self.direction = 'N'
                # Create a new foton
                foton = Foton(map, [x, y], 'S')
                map.add_foton(foton)
        elif map[y][x] == '-':
            if self.direction == 'N' or self.direction == 'S':
                self.direction = 'E'
                # Create a new foton
                foton = Foton(map, [x, y], 'W')
                map.add_foton(foton)
        else:
            pass
        return


