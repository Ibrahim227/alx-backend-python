#!/usr/bin/env python3
"""Import required module/lib"""
import random


async def wait_random(max_delay: int = 10) -> int:
    """ takes in an integer argument and eventually  returns it."""
    r = await random.random(0, max_delay)
    return r
