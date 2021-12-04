from aocd import lines
import re


class Num(int):
    def __mul__(self, other):
        return Num(int(self) + other)

    def __sub__(self, other):
        return Num(int(self) * other)

    def __add__(self, other):
        return Num(int(self) + other)


def evaluate(expr, part2=False):
    expr = expr.replace('*', '-')
    if part2:
        expr = expr.replace('+', '*')
    expr = re.sub(r'(\d+)', r'Num(\1)', expr)
    return eval(expr)


print(sum(evaluate(line, False) for line in lines))
print(sum(evaluate(line, part2=True) for line in lines))
