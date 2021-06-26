#!/bin/env python
import asyncio
import time

def f(future,number):
	for _ in range(3):
		print(number)
		time.sleep(3)
	future.set_result("hello")

loop = asyncio.get_event_loop()
futures = []
for j in range(3):
	future = loop.create_future()
	loop.call_soon(f,future,j)
	futures += [future]
res = loop.run_until_complete(asyncio.gather(*futures))
print(res)
