#!/usr/bin/env python3
"""Import required module/lib"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)."""
    delay = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    complete = asyncio.as_completed(tasks)
    for task in complete:
        result = await task
        delay.append(result)

    return delay
