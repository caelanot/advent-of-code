from aocd import lines
from collections import defaultdict
import regex


def parse_food(food):
    ingredients, allergens = food.split(' (')
    ingredients = set(ingredients.split(' '))
    allergens = regex.findall(r' (.+?)[,)]', allergens[8:])
    return ingredients, allergens


def part1(input):
    all_ingredients = []
    allergies = defaultdict(set)
    for food in input:
        # Get ingredients and allergens of current food
        ingredients, allergens = parse_food(food)
        # Add current ingredients to the list of all ingredients
        all_ingredients.extend(ingredients)

        # Update current possibilities for ingredient
        for allergen in allergens:
            if allergies[allergen] == set():
                allergies[allergen] = ingredients
            allergies[allergen] = allergies[allergen].intersection(ingredients)

    for allergens in allergies.values():
        all_ingredients = [x for x in all_ingredients if x not in allergens]

    return len(all_ingredients), allergies


def part2(allergies):
    names = {}
    while allergies:
        for f, v in allergies.items():
            if len(v) == 1:
                break
        # set the field for the position
        names[f] = next(iter(allergies[f]))
        # remove the field from all other candidates
        del allergies[f]
        for j in allergies:
            allergies[j].discard(names[f])

    canonical = ""
    for allergen in sorted(names):
        canonical += names[allergen] + ','

    return canonical[:-1]


answer1, allergies = part1(lines)
print(answer1)
print(part2(allergies))
