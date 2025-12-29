class TeaLeaf:
    def __init__(self, age, size):
        self._age = age
        self._size = size

    @property
    def age(self):
        return self._age + 2

    @property
    def size_data(
        self,
    ):  # getter function, modify any variable in class using property decorator
        return self._size * 5

    @size_data.setter
    def size_matters(self, size):
        self._size = size

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


leaf = TeaLeaf(2, 10)
print(leaf.age)
print(leaf.size_data)
# leaf.age = 6
# print(leaf.age)
