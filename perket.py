import itertools

ingredients = []
n = int(input())
for i in range(n):
    ingredients.append(list(map(int,input().split())))
combos = []
for j in range(1,n+1):
    combos.extend([list(x) for x in itertools.combinations(ingredients,j)])
diff = 100000000000
for combo in combos:
    first = combo.pop(0)
    sour = first[0]
    bitter = first[1]
    for ingredient in combo:
        sour *= ingredient[0]
        bitter += ingredient[1]
    diff = min(abs(sour-bitter),diff)
print(diff)
