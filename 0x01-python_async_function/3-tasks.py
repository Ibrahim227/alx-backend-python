#!/usr/bin/env python3
"""Import reqiured module/lib"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns An asyncio.Task object that represents the execution"""
     return asyncio.create_task(wait_random(max_delay))
