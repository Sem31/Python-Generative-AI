menu = ["Green", "Lemon", "Spiced", "Mint"]
order = ["$30", "$50", "$80", "$100"]
# print("abc", zip(menu, order))
# print("agd", list(zip(menu, order)))

for item, amount in zip(menu, order):
    print(f"{item} chai costs {amount}")
