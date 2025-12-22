def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kasar"

    kitchen()
    print(f"Order is: {chai_type}")


update_order()
