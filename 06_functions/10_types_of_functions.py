def pure_chai(cups):
    return cups * 10


total_chai = 0


# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
    return total_chai


def numeric_table(number, index=1):
    if index > 10:
        return "Table complete"
    print(f"{number} x {index} = {number * index}")
    return numeric_table(number, index + 1)


numeric_table(509)


chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))
print(strong_chai)
