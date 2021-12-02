import concurrent.futures
import time
import random


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result)

end = time.perf_counter()

print(f"Process finished in {end - start} seconds.......")
