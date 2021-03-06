import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)....")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # use this line , results are printed in the order of completion
    # results = [executor.submit(do_something, sec)  for sec in secs]

    # Now if you want to print in the same order of execution of functions, use map
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
