from aocd import lines
import re

pattern = r'\b([a-z]+)\b'

count = value = 0
for line in lines:
    line = re.findall(pattern, line)
    signals = line[:-4]
    outputs = line[-4:]

    code = {
        length: set(signal)
        for signal in signals
        if (length := len(signal)) in (2, 4)
    }

    num = ""
    for o in outputs:
        match len(o):
            case 2: num += "1"
            case 3: num += "7"
            case 4: num += "4"
            case 5:
                if len(code[2] & set(o)) == 2:
                    num += "3"
                elif len(code[4] & set(o)) == 3:
                    num += "5"
                else:
                    num += "2"
            case 6:
                if len(code[4] & set(o)) == 4:
                    num += "9"
                elif len(code[2] & set(o)) == 2:
                    num += "0"
                else:
                    num += "6"
            case 7: num += "8"
    count += sum(len(x) in (2, 3, 4, 7) for x in outputs)
    value += int(num)

print(count)
print(value)
