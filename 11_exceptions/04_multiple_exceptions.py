def process_order(item, qty):
    try:
        price = {"masala": 20}[item]
        cost = price * qty
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that is not in menu.")
    except TypeError:
        print("Quantity must be in number")


process_order("ginger", 2)
process_order("masala", "two")
