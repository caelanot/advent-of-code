from aocd import lines
from sympy.ntheory.modular import crt


timestamp = int(lines[0])
buses = lines[1].split(',')

minwait = (0, timestamp)
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        time = (timestamp // bus) * bus + bus
        if time - timestamp < minwait[1]:
            minwait = (bus, time - timestamp)

residue = []
modulus = []
for index, item in enumerate(buses):
    if item == "x":
        continue
    residue.append(int(item) - index)
    modulus.append(int(item))


print(minwait[0]*minwait[1])
print(crt(modulus, residue)[0])
