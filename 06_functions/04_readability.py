def calculate_bills(cups, price_per_cup):
    total = cups * price_per_cup
    print(f"Total bill for {cups} cups is ${total:.2f}")  # 2f for 2 decimal places


calculate_bills(3, 2.5)
calculate_bills(5, 3.0)
calculate_bills(2, 4.0)
