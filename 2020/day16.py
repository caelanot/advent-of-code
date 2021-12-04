from aocd import data


def parse_field(field):
    name, valid = field.split(':')
    valid = [tuple(map(int, r)) for r in
             (r.split('-') for r in valid.split(' or '))]
    return name, valid


def read_ticket(ticket):
    return list(map(int, ticket.split(',')))


def valid_value(value):
    return any(r[0] <= value <= r[1] for v in fields.values() for r in v)


fields, ticket, nearby = data.split('\n\n')

fields = {f[0]: f[1] for f in (parse_field(z) for z in fields.splitlines())}
ticket = read_ticket(ticket.splitlines()[1])
nearby = [read_ticket(t) for t in nearby.splitlines()[1:]]


def part1():
    return sum(n for t in nearby for n in t if not valid_value(n))


def part2():
    # Get valid tickets
    valid = [t for t in nearby if all(valid_value(n) for n in t)]

    # collect the fields that match the values in every position
    candidates = {}
    for i in range(len(ticket)):
        candidates[i] = set()
        for f, v in fields.items():
            if all(any(r[0] <= t[i] <= r[1] for r in v) for t in valid):
                candidates[i].add(f)

    # reduce every set of candidates to a single field
    names = {}
    while candidates:
        # find the position with a single candidate
        for f, v in candidates.items():
            if len(v) == 1:
                break
        # set the field for the position
        names[f] = next(iter(candidates[f]))
        # remove the field from all other candidates
        del candidates[f]
        for j in candidates:
            candidates[j].discard(names[f])

    departures = 1
    for i, n in enumerate(ticket):
        if names[i].startswith("departure"):
            departures *= n
    return departures


print(part1())
print(part2())
