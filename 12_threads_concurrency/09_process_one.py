import threading
import time


def cpu_heavy():
    print("Crunching some numbers....")
    total = 0

    for i in range(10**8):
        total += i

    print("Done !")


start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken: {time.time() - start:.2f} seconds")


# output ->
# Crunching some numbers....
# Crunching some numbers....
# Done !
# Done !
# Time taken: 9.50 sec


# this is taking 9.50 sec, can we impove that using process, check time 10_process_two.py
