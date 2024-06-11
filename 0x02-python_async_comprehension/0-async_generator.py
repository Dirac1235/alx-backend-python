#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def number_genertor():
    """ Returns Generator """
    for i in range(10):
        yield i


async def async_generator():
    """ Generates random number between 1 - 10 """
    async for _ in number_genertor():
        yield random.random() * 10
        await asyncio.sleep(1)
