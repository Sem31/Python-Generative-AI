favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai",
]

unique_chais = {chai for chai in favourite_chais}
print(unique_chais)

# Output: {'Masala Chai', 'Lemon Tea', 'Green Tea', 'Elaichi Chai'} # Note: The order of elements in the output set may vary since sets are unordered collections.

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
