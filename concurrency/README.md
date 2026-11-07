# Concurrency

The [concurrency example](concurrency.py) compares threads, multiprocessing, and asynchronous tasks using Python 3 standard-library modules. Understanding functions and the basics of Python execution is useful before starting.

From the repository root:

```bash
python concurrency/concurrency.py
```

The example runs all three demonstrations and includes timed waits; process and thread output can appear in different orders.

```mermaid
flowchart TD
    Start[Run concurrency example] --> Threads[Threads]
    Threads --> Processes[Processes]
    Processes --> Async[Asyncio tasks]
    Async --> Done[Complete]
```

[Back to the learning path](../README.md#learning-path)