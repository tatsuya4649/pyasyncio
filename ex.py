#!/bin/env python
import asyncio
import time

# this function is called from `call_hello`
async def hello(n):
	await asyncio.sleep(1)
	print(f"Hello World {n}")

async def call_hello():
	print("call_hello")
	# awai => future or coroutine
	await hello(1)

async def call_hello2():
	print("call_hello2")
	await hello(2)

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.create_task(call_hello())
	loop.run_until_complete(call_hello2())
