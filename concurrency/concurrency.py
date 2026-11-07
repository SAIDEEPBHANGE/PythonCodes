"""
Concurrency in Python: Multiprocessing, Threading, Asynchrony (AsyncIO), and GIL
"""

import time
import threading
import multiprocessing
import asyncio

# ------------------------------------------
# 1. THREADING EXAMPLE
# ------------------------------------------

def thread_task(name):
    # Simulates a task that takes time (like I/O)
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

def run_threading():
    print("\n--- Threading Example ---")
    threads = []

    for i in range(3):
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed")

# Threading allows concurrency using shared memory
# BUT due to the GIL, threads in CPU-bound tasks won't run in true parallel


# ------------------------------------------
# 2. MULTIPROCESSING EXAMPLE
# ------------------------------------------

def process_task(name):
    print(f"Process {name} starting")
    time.sleep(2)
    print(f"Process {name} finished")

def run_multiprocessing():
    print("\n--- Multiprocessing Example ---")
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")

# Multiprocessing bypasses the GIL by using separate memory space
# Each process runs in parallel, making it ideal for CPU-bound tasks


# ------------------------------------------
# 3. ASYNCHRONY (ASYNCIO) EXAMPLE
# ------------------------------------------

async def async_task(name):
    print(f"Async Task {name} starting")
    await asyncio.sleep(2)  # Non-blocking sleep
    print(f"Async Task {name} finished")

async def run_asyncio():
    print("\n--- AsyncIO Example ---")
    await asyncio.gather(
        async_task(1),
        async_task(2),
        async_task(3)
    )

# AsyncIO is single-threaded, single-process
# But it allows handling thousands of I/O-bound tasks concurrently
# Great for network calls, file I/O, or anything with wait time


# ------------------------------------------
# 4. GIL (Global Interpreter Lock) NOTE
# ------------------------------------------

"""
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects.
This means that only one thread executes Python bytecode at a time.

Implication:
- CPU-bound tasks in threads are not truly concurrent.
- Multiprocessing avoids the GIL by using separate processes.

The GIL doesn't affect asyncio since it switches tasks cooperatively.
"""

# ------------------------------------------
# MAIN FUNCTION TO RUN ALL EXAMPLES
# ------------------------------------------

if __name__ == "__main__":
    run_threading()
    run_multiprocessing()
    asyncio.run(run_asyncio())
