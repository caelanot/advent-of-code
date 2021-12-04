from aocd import numbers

print(sum(a < b for a, b in zip(numbers, numbers[1:])))
print(sum(a < b for a, b in zip(numbers, numbers[3:])))
