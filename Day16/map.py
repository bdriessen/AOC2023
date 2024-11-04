import foton

class map:
    def __init__(self, pattern):
        self.map = pattern
        self.width = len(pattern[0])
        self.height = len(pattern)
        self.fotons = []

    def add_foton(self, foton):
        self.fotons.append(foton)

    def move_fotons(self):
        for foton in self.fotons:
            foton.move()

            # Check if foton is outside the map
            if foton.pos[0] < 0 or foton.pos[0] >= self.width or foton.pos[1] < 0 or foton.pos[1] >= self.height:
                self.fotons.remove(foton)

    def act_fotons(self):
        for foton in self.fotons:
            foton.act(self.map)






