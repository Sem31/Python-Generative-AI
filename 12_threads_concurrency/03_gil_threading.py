import threading
import time


def brew_chai():
    print(f"{threading.current_thread().name} started brewing....")
    count = 0
    for _ in range(100_100_100):
        count += 1

    print(f"{threading.current_thread().name} finishing brewing....")


thread1 = threading.Thread(target=brew_chai, name="Ginger chai - 1")
thread2 = threading.Thread(target=brew_chai, name="Eliachi chai - 2")


start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds..")
