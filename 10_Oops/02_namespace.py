class Chai:
    origin = "India"


print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)
masala = Chai()

# creating object from class chai

masala.is_hot = False
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.flavor = "Masala"
print(f"Flavor {masala.flavor}")
