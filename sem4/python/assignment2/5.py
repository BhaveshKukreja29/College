import threading
import time

def print_message():
    time.sleep(3)
    print("Thread message after 3 seconds")

threads = []
for _ in range(5):
    t = threading.Thread(target=print_message)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads finished.")
