from aocd import lines
from dataclasses import dataclass


@dataclass
class badDiver:
    position: int = 0
    depth: int = 0

    def move(self, direction, value):
        match direction:
            case "forward":
                self.position += value
            case "up":
                self.depth -= value
            case "down":
                self.depth += value


@dataclass
class Diver:
    position: int = 0
    depth: int = 0
    aim: int = 0

    def move(self, direction, value):
        match direction:
            case "forward":
                self.position += value
                self.depth -= self.aim * value
            case "up":
                self.aim += value
            case "down":
                self.aim -= value


p1 = badDiver()
p2 = Diver()
for line in lines:
    direction, number = line.split(' ')
    number = int(number)
    p1.move(direction, number)
    p2.move(direction, number)
print(p1.position * p1.depth, p2.position * p2.depth)
