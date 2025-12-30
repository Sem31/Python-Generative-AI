from multiprocessing import Process
import time


def cpu_heavy():
    print("Crunching some numbers....")
    total = 0

    for i in range(10**8):
        total += i

    print("Done !")


if __name__ == "__main__":
    start = time.time()
    process = [Process(target=cpu_heavy) for _ in range(2)]
    [p.start() for p in process]
    [p.join() for p in process]

    print(f"Time taken: {time.time() - start:.2f} seconds")

# output ->
# Crunching some numbers....
# Crunching some numbers....
# Done !
# Done !
# Time taken: 5.09 seconds
