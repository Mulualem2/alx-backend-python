#!/usr/bin/env python3
""" Measures total execution time """

import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ Returns total_time / n for wait_n() execution """

    elapsed_time: float

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
