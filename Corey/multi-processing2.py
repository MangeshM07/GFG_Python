import time
import multiprocessing
import random

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(random.randint(1,10))
    print("Done sleeping...")

processes=[]
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()


end = time.perf_counter()

print(f"Process finished in {end - start} seconds.......")
