def cakes(recipe, available):
    cakes_to_make = []
    for key in recipe:
        if key in available:
            if available[key] >= recipe[key]:
                cakes_could_make = available[key] // recipe[key]
                cakes_to_make.append(cakes_could_make)
            else:
                return 0
        else:
            return 0
    return min(cakes_to_make)

def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    recipe = {'cream': 1, 'flour': 3, 'sugar': 1, 'milk': 1, 'oil': 1, 'eggs': 1}
    available = {'sugar': 1, 'eggs': 1, 'flour': 3, 'cream': 1, 'oil': 1, 'milk': 1}
    print(cakes(recipe=recipe, available=available))

if __name__ == '__main__':
    main()