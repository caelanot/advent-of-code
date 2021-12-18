from aocd import data


class Packet():
    version_sum = 0

    def __init__(self, version, type_id, val, packs):
        self.version = version
        self.type = type_id
        self.val = val
        self.packs = packs
        Packet.version_sum += version

    def eval(self):
        match self.type:
            case 0: return sum(p.eval() for p in self.packs)
            case 1:
                x = 1
                for p in self.packs:
                    x *= p.eval()
                return x
            case 2: return min(p.eval() for p in self.packs)
            case 3: return max(p.eval() for p in self.packs)
            case 4: return self.val
            case 5: return self.packs[0].eval() > self.packs[1].eval()
            case 6: return self.packs[0].eval() < self.packs[1].eval()
            case 7: return self.packs[0].eval() == self.packs[1].eval()


def parse():
    global bits

    version, bits = int(bits[:3], 2), bits[3:]
    type_id, bits = int(bits[:3], 2), bits[3:]
    n = None
    subpackets = []

    if type_id == 4:
        n = ""
        while bits[0] == "1":
            n, bits = n + bits[1:5], bits[5:]
        n, bits = n + bits[1:5], bits[5:]
        n = int(n, 2)
    else:
        length_id, bits = bits[:1], bits[1:]
        if length_id == "0":
            length, bits = int(bits[:15], 2), bits[15:]
            start = len(bits)

            while start - len(bits) < length:
                subpackets.append(parse())
        else:
            num, bits = int(bits[:11], 2), bits[11:]
            for _ in range(num):
                subpackets.append(parse())

    return Packet(version, type_id, n, subpackets)


bits = f'{int(data, 16):0{4*len(data)}b}'
x = parse()
print(Packet.version_sum)
print(x.eval())
