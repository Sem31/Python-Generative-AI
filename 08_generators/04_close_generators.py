def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for order..."
            print(f"Preparing your {order}...")
            print(f"Here is your {order}. Enjoy!")
    except:
        print("Closing the stall. No more orders will be taken.")


stall = chai_stall()
print(next(stall))  # Prime the generator
print(stall.send("Masala Chai"))
print(stall.send("Ginger Chai"))
stall.close()  # Close the generator
