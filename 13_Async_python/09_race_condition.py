import threading

chai_stock = 0


def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1


threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Chai stock: ", chai_stock)

# this is the output, which means there is race condition like which threading is increasing or updating chai_stock value
# Chai stock:  200000
# Chai stock:  164640
