import threading
import time


def monitoring_tea_temp():
    while True:
        print("monitoring tea temprature...")
        time.sleep(2)


# Daemon threads are background thread which automatically sutdown when main thread is gone
threading.Thread(target=monitoring_tea_temp, daemon=False).start()


print("this is main program done!")
# this program is daemon is False, in that case monitoring_tea_temp is calling continuously
