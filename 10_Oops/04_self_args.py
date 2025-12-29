class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def adding(self):
        return self.a + self.b


opp = Operation(2, 4)

print(f"Adding 2 + 4 = {opp.adding()}")


class Chaicup:
    size = 150  # ml

    def describe(self):
        return f"A {self.size}ml chai cup"


cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))  # passing a context which is class object

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))  # You will see the size 100 ML now
