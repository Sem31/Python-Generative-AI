def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low")  # positional
make_chai(tea="Green", sugar="Medium", milk="No")  # keywords


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)


special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")
