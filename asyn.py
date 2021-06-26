#!/bin/env python

import asyncio
import time

async def f(tag):
	await asyncio.sleep(1)
	return "fasdf"

asyncio.run(f(1))
