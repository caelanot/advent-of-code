from aocd import data
import regex


rules, messages = data.split('\n\n')
rules = rules.splitlines()
messages = messages.splitlines()


def compile_regex(rule_number, part2=False):
    if rule_number == 8 and part2:
        return compile_regex(42, part2) + '+'

    if rule_number == 11 and part2:
        r42 = compile_regex(42, part2)
        r31 = compile_regex(31, part2)
        return f'(?<X11>{r42}(?&X11){r31}|{r42}{r31})'

    if '"' in regex_rules[rule_number]:
        return eval(regex_rules[rule_number])

    res = []
    for side in regex_rules[rule_number].split(' | '):
        x = ''.join(compile_regex(int(num), part2) for num in side.split())
        res.append(x)
    return '(' + '|'.join(res) + ')'


def part1():
    count = 0
    regex_match = '^' + compile_regex(0) + '$'
    for message in messages:
        count += regex.match(regex_match, message) is not None

    return count


def part2():
    count = 0
    regex_rules[8] = '42 | 42 8'
    regex_rules[11] = '42 31 | 42 11 31'
    regex_match = '^' + compile_regex(0, part2=True) + '$'
    for message in messages:
        count += regex.match(regex_match, message) is not None

    return count


regex_rules = {}
for rule in rules:
    number, pattern = rule.split(': ')
    regex_rules[int(number)] = pattern


print(part1())
print(part2())
