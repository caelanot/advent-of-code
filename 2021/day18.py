from aocd import lines
from itertools import permutations
from math import floor, ceil, perm


class Snailfish():
    def __init__(self, data, parent=None):
        if isinstance(data, int):
            self.parent = parent
            self.data = data
            self.left = None
            self.right = None
        else:
            self.parent = parent
            self.data = None
            if isinstance(data[0], Snailfish):
                self.left = data[0]
                self.left.parent = self
                self.right = data[1]
                self.right.parent = self
            else:
                self.left = Snailfish(data[0], self)
                self.right = Snailfish(data[1], self)

    def explode(self, depth=0):
        if depth == 4 and self.data is None:
            left = self.left.data
            right = self.right.data

            self.explosion_add("left", left)
            self.explosion_add("right", right)

            self.data = 0
            self.left = None
            self.right = None

            return True

        elif self.data is None:
            if self.left.explode(depth + 1):
                return True
            if self.right.explode(depth + 1):
                return True

            return False
        return False

    def explosion_add(self, attr, val):
        opp = "left" if attr == "right" else "right"
        prev = self
        while (self := self.parent) and prev is getattr(self, attr):
            prev = self
        if self is not None:
            self = getattr(self, attr)
            while self.data is None:
                self = getattr(self, opp)
            self.data += val

    def splitting(self, attr=None):
        if self.data is not None and self.data > 9:
            data = [floor(self.data / 2), ceil(self.data / 2)]
            setattr(self.parent, attr, Snailfish(data, parent=self.parent))
            return True
        elif self.data is None:
            if self.left.splitting("left"):
                return True
            if self.right.splitting("right"):
                return True
        return False

    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.splitting():
                continue
            break
        return self

    def mag(self):
        if self.data is not None:
            return self.data
        return 3*self.left.mag() + 2*self.right.mag()

    def __add__(self, oth):
        data = [self, oth]
        return Snailfish(data).reduce()

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        return f"[{str(self.left)}, {str(self.right)}]"


snail = Snailfish(eval(lines[0]))
for s in lines[1:]:
    snail += Snailfish(eval(s))

print(snail.mag())
print(max((Snailfish(eval(a))+Snailfish(eval(b))).mag()
          for a, b in permutations(lines, 2)))
