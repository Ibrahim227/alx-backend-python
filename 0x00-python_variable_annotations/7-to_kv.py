#!/usr/bin/env python3
"""Import module/lib"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple"""
    return (k, v**2)
