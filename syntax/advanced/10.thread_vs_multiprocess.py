from multiprocessing import Process
import os
import time

def square_num(i):
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count() # -- This will return the number of CPUs in the system
for i in range(num_processes): # -- This will create a process for each CPU
    sq_process = Process(target=square_num) #We would add args as a tuple as args=(i,) --> comma after i because it is a single element tuple
    processes.append(sq_process)

# Start all processes
for p in processes:
    p.start()

# Join all processes
for p in processes:
    p.join()

print("Multiprocessing complete") # This will print Multiprocessing complete
# or
print("End of script") # This will print End of script

# This could result in 11 processes running concurrently

"""THREADS"""

# Threads are used to execute multiple tasks concurrently. They are lightweight and do not require separate memory space.

# The following code shows how to create a thread:
from threading import Thread
import os
import time

def square_num(i):
    for i in range(100):
        i * i
        time.sleep(0.1)
if __name__ == "__main__":
    threads = []
    num_threads = os.cpu_count() # -- This will return the number of CPUs in the system

    for i in range(num_threads): # -- This will create a thread for each CPU
        sq_thread = Thread(target=square_num) #We would add args as a tuple as args=(i,) --> comma after i because it is a single element tuple
        threads.append(sq_thread)

    # Start all threads
    for t in threads:
        t.start()

    # Join all threads --> This will wait for all threads to complete before moving on to the next line of code in the script
    for t in threads:
        t.join()

print("Threading complete") # This will print Threading complete
# or
print("End of script") # This will print End of script

# This could result in one process with say 11 threads    


"""MULTITHREADING"""

database_val = 0

if __name__ == "__main__":
    def increase():
        """
        1. The increase function increments the global variable database_val by 1.
        2. It creates a local copy of the global variable and increments it by 1.
        3. It then assigns the local copy back to the global variable.
        4. The time.sleep(0.1) statement is used to simulate a delay.
        5. The database_val variable is a shared resource that is accessed by multiple threads.
        6. The increase function is called by two threads, thread1 and thread2.
        7. The threads increment the database_val variable concurrently.
        8. The database_val variable is expected to be incremented by 2.
        9. The output shows the start and end values of the database_val variable.
        10. The start value is 0, and the end value is 2.
        11. The end value is less than the expected value of 2.
        12. This is because the threads are accessing the shared resource concurrently.
        13. The threads are not synchronized, and the increment operation is not atomic.
        """
        global database_val
        local_copy = database_val
        local_copy += 1
        time.sleep(0.1)
        database_val = local_copy

    print("Start value:", database_val)

    thread1 = Thread(target=increase) # -- This will create a thread for each CPU
    thread2 = Thread(target=increase) # -- This will create a thread for each CPU

    thread1.start() # -- This will start the thread
    thread2.start() # -- This will start the thread

    thread1.join() # -- This will wait for all threads to complete before moving on to the next line of code in the script
    thread2.join() # -- This will wait for all threads to complete before moving on to the next line of code in the script

    print("End value:", database_val)

"""
Output will be: 
Start value: 0
End value: 1 --> This is 1 and not 2 because the threads are accessing the shared resource concurrently.
                 In this case only one thread is able to increment the value of the shared resource. 
                 thread1 increments the value of the shared resource and then thread2 increments the value of the shared resource.
                 This results in the end value being 1 instead of 2.
"""