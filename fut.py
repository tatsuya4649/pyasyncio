#!/bin/env python
import asyncio
import time

def f(future):
	time.sleep(5)
	future.set_result("hello")

future = asyncio.futures.Future()
f(future)

if future.done():
	res = future.result()
	print(res)
