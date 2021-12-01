# Run code concurrently using threading module
# Threading helps in I/O bound operations like downloading files from the internet, network operations

# Threading demo and demo1 are old ways of threading implementation. New way is in demo2 program
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)....")
    time.sleep(seconds)
    print("Done sleeping...")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
