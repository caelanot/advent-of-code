from aocd import data
import re


def simulate(vel_x, vel_y, target_x, target_y):
    x, y = 0, 0
    while True:
        if vel_x == 0 and not (target_x[0] <= x <= target_x[1]):
            return False
        if y < target_y[0] or x > target_x[1]:
            return False
        if (target_x[0] <= x <= target_x[1]
                and target_y[0] <= y <= target_y[1]):
            return True

        x, y = x + vel_x, y + vel_y
        if vel_x > 0:
            vel_x -= 1
        vel_y -= 1


(x1, x2), (y1, y2) = re.findall(r'(-?\d+)..(-?\d+)', data)
x1, x2 = map(int, (x1, x2))
y1, y2 = map(int, (y1, y2))

lower_x = 0
while lower_x*(lower_x + 1)//2 < x1:
    lower_x += 1

upper_y = (-y1 - 1)
print(upper_y * (upper_y+1)//2)
print(sum(simulate(x, y, (x1, x2), (y1, y2))
          for x in range(lower_x, x2+1)
          for y in range(y1, upper_y+1)))
