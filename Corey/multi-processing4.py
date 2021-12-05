import concurrent.futures
import time


def do_something(seconds):
    print(f"Sleeping for {seconds}..")
    time.sleep(seconds)
    print(f"Done sleeping for {seconds}...")


if __name__ == "__main__":
    print("running from multi-processing4")

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

    end = time.perf_counter()

    print(f"Process finished in {round(end - start, 2)} second(s)")
