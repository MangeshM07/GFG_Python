# Run code concurrently using threading module
# Threading helps in I/O bound operations like downloading files from the internet, network operations
import threading
import time

start = time.perf_counter()


def do_something():
    print("sleeping 1 second....")
    time.sleep(1)
    print("Done sleeping")


# do_something()
# do_something()
# Instead of executing the function twice , create 2 threads for both of these

t1 = threading.Thread(target=do_something)  # we don't want to execute the function, hence no ()
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# we are using so that threads will not execute rest of the code below start() until t1 and t2 are finished
t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
