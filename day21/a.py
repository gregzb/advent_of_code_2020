from collections import defaultdict

data = []

with open('in.txt') as f:
    for line in f:
        ingredients, allergies = line.strip().split(' (')
        ingredients = ingredients.split(' ')
        allergies = allergies[len('contains '):-1].split(', ')
        data.append((ingredients, allergies))

def solve(li):
    allergy_dict = defaultdict(list)
    for ingredients, allergens in li:
        for allergen in allergens:
            allergy_dict[allergen].append(set(ingredients))

    all_ingredients = defaultdict(int)
    for ingredients, allergens in li:
        for ingred in ingredients:
            all_ingredients[ingred] += 1

    # print(len(all_ingredients))

    used = {}

    while True:
        none_1 = True
        all_possible = set()
        for allergen in allergy_dict:
            starting = set()
            for se in allergy_dict[allergen]:
                starting = starting.union(se)

            for key in used:
                starting.discard(key)

            for se in allergy_dict[allergen]:
                starting.intersection_update(se)

            if len(starting) == 1:
                none_1 = False
                used[list(starting)[0]] = allergen
                break
            all_possible = all_possible.union(starting)
        if none_1:
            not_possible = set(all_ingredients.keys()).difference(all_possible).difference(used.keys())
            # print(len(not_possible))
            # print(len())
            return sum(all_ingredients[ingred] for ingred in not_possible)
            break

    # print(used)

    return -1

solved = solve(data)
print(solved)