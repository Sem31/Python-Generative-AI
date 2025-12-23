def infinite_chai():
    count = 1
    while True:
        yield f"Cup {count}: Refil Chai"
        count += 1


refill = infinite_chai()
user = infinite_chai()

for _ in range(3):
    print(next(refill))

for _ in range(5):
    print(next(user))
