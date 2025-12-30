# concurrency -> multi-threading
# parallelism -> multiprocessing

# Multithreading: Multiple threads share the same memory and CPU. In Python, the GIL prevents true parallel execution of threads for CPU-bound tasks.due to the GIL (Global Interpreter Lock), only one thread can execute Python bytecode at a time.

# Multiprocessing: Multiple processes run independently with separate memory spaces and CPUs, bypassing the GIL and enabling true parallelism.


# multithreading example

# example -> making two things simantaneouly


import threading
import time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order of #{i}")
        time.sleep(1)


def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)


order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)


order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()
print(f"All orders taken and chai brewed")
