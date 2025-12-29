class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# Inheritance bwith code duplication
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# Inheritance with Explict call
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


# Inheritance with super keyword
class GingerChai(Chai):

    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
