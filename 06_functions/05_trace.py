def add_vat(price, vat_rate):
    return price + (price * vat_rate / 100)


orders = [100, 150, 200]

for order in orders:
    total_price = add_vat(order, 10)
    print(f"Total price for order {order} with VAT: {total_price}")
