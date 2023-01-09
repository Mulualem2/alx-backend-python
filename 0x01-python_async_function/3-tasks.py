#!/usr/bin/env python3
""" Takes int arg, returns random delay """

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Waits for random delay then returns asyncio.Task object """
    return asyncio.create_task(wait_random(max_delay))
