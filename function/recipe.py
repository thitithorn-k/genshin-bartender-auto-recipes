
def get_recipe(drink_id):
    if drink_id == -1:
        return -1
    recipes = []
    if drink_id == 0:
        recipes.append([0, 3])
    elif drink_id == 1:
        recipes.append([0, 1])
        recipes.append([3, 1])
        recipes.append([5, 1])
    elif drink_id == 2:
        recipes.append([0, 2])
        recipes.append([6, 1])
    elif drink_id == 3:
        recipes.append([0, 2])
        recipes.append([3, 1])
    elif drink_id == 4:
        recipes.append([0, 1])
        recipes.append([3, 1])
        recipes.append([4, 1])
    elif drink_id == 5:
        recipes.append([0, 1])
        recipes.append([3, 2])
    elif drink_id == 5:
        recipes.append([0, 1])
        recipes.append([3, 2])
    elif drink_id == 6:
        recipes.append([1, 1])
        recipes.append([3, 1])
        recipes.append([8, 1])
    elif drink_id == 7:
        recipes.append([1, 1])
        recipes.append([3, 2])
    elif drink_id == 8:
        recipes.append([1, 1])
        recipes.append([3, 1])
        recipes.append([4, 1])
    elif drink_id == 9:
        recipes.append([1, 1])
        recipes.append([3, 1])
        recipes.append([5, 1])
    elif drink_id == 10:
        recipes.append([1, 3])
    elif drink_id == 11:
        recipes.append([1, 2])
        recipes.append([3, 1])
    elif drink_id == 12:
        recipes.append([1, 2])
        recipes.append([7, 1])
    elif drink_id == 13:
        recipes.append([2, 1])
        recipes.append([6, 1])
        recipes.append([8, 1])
    elif drink_id == 14:
        recipes.append([2, 2])
        recipes.append([7, 1])
    elif drink_id == 15:
        recipes.append([2, 2])
        recipes.append([6, 1])
    elif drink_id == 16:
        recipes.append([2, 3])
    elif drink_id == 17:
        recipes.append([2, 2])
        recipes.append([3, 1])
    elif drink_id == 18:
        recipes.append([2, 1])
        recipes.append([3, 2])
    elif drink_id == 19:
        recipes.append([2, 2])
        recipes.append([1, 1])
    elif drink_id == 20:
        recipes.append([0, 1])
        recipes.append([1, 1])
        recipes.append([3, 1])

    return [drink_id, recipes]
