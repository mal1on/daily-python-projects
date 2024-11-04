import json


def finder():
    '''
    Python program that takes a list of ingredients from the user and
    displays recipes that can be made using those ingredients.
    '''
    ingredients = input('Enter a list of ingredients separated by commas: ')
    ingredients = map(str.strip, ingredients.split(','))
    ingredients = list(map(str.lower, ingredients))

    with open('recipes.json', 'r') as f:
        recipes = json.load(f)

    possible = []

    for recipe in recipes:
        if all(i in ingredients for i in recipe['ingredients']):
            possible.append(recipe)

    if possible:
        print('Here are some recipes you can make:\n')
        for recipe in possible:
            print(f'Recipe: {recipe["name"]}\nIngredients: \
{", ".join(recipe["ingredients"])}\nInstructions: {recipe["instructions"]}\n')
    else:
        print('No recipes available with the ingredients entered.')


if __name__ == '__main__':
    finder()
