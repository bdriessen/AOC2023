
class Foton:
    def __init__(self):
        self.pos = [0, 0]
        self.direction = 'E'

    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.pos[1] -= 1
        elif self.direction == 'S':
            self.pos[1] += 1
        elif self.direction == 'E':
            self.pos[0] += 1
        elif self.direction == 'W':
            self.pos[0] -= 1
        else:
            print("Invalid direction")
        # Check if foton is outside the map is done in the map class




