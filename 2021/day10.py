from aocd import lines

points = 0
score = []

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}
errors = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete = {"(": 1, "[": 2, "{": 3, "<": 4}
for line in lines:
    stack = []

    for char in line:
        if char in "([{<":
            stack.append(char)
        else:
            if chunks[stack.pop()] != char:
                points += errors[char]
                break
    else:
        autocomplete = 0
        for char in reversed(stack):
            autocomplete = autocomplete * 5 + complete[char]
        score.append(autocomplete)

print(points)
score.sort()
print(score[len(score)//2])
