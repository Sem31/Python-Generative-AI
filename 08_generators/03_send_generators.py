def chai_customer():
    print("Welcome! what chai would you like?")
    order = yield
    while True:
        print(f"Preparing your {order}...")
        print(f"Here is your {order}. Enjoy!")
        order = yield


customer = chai_customer()
next(customer)  # Prime the generator

customer.send("Masala Chai")
customer.send("Ginger Chai")
customer.send("Elaichi Chai")
