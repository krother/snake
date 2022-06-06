
from dataclasses import dataclass
from random import randint


@dataclass
class PlayingField:

    size: (int, int)
    food: (int, int) = None

    @property
    def xsize(self):
        return self.size[0]

    @property
    def ysize(self):
        return self.size[1]
        
    def add_food(self, x, y):
        if not (x, y) in self.walls:
            self.food = x, y
        else:
            self.food = None

    def add_random_food(self):
        x, y = (
            randint(1, self.xsize - 1),
            randint(1, self.ysize - 1)
        )
        self.add_food(x, y)

    @property
    def walls(self):
        for x in range(self.xsize):
            yield (x, 0)
        for y in range(1, self.ysize - 1):
            yield 0, y
            yield self.xsize - 1, y
        for x in range(self.xsize):
            yield (x, self.ysize - 1)


if __name__ == '__main__':
    # test code
    pf = PlayingField((10, 10))
    print(pf)
    print(pf.size)

    print(pf.get_walls())