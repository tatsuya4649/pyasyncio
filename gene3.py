#!/bin/env python
import asyncio
import time

def my_sleep(delay):
	def _fu_result(fut):
		fut.set_result("hello")
	loop = asyncio.get_running_loop()
	future = loop.create_future()
	h = loop.call_later(delay,_fu_result,future)
	yield from future

def f(tag):
	for i in range(5):
		yield from my_sleep(1)
		print(f"waiting for {tag}")
	return f"hello {tag}"

loop = asyncio.get_event_loop()
tasks = [f(n) for n in range(3)]
ret = loop.run_until_complete(asyncio.gather(*tasks))
print(ret)
