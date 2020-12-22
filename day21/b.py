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
            break

    new_li = []

    for key in used:
        new_li.append((key, used[key]))

    new_li.sort(key=lambda x: x[1])
    ans = [x[0] for x in new_li]
    tmp_str = ''
    for i in range(len(ans)):
        tmp_str += ans[i] + (',' if i != len(ans)-1 else '')
    return tmp_str

solved = solve(data)
print(solved)